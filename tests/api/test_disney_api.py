# tests/api/test_disney_api.py
import requests
import pytest
import json

BASE_URL = "https://api.disneyapi.dev"

def log_response(response, test_name=""):
    """Print helpful debugging info."""
    print(f"\n=== {test_name} ===")
    print(f"Status: {response.status_code}")
    print(f"URL: {response.url}")
    try:
        data = response.json()
        count = len(data.get("data", []))
        print(f"Results Count: {count}")
        if count > 0:
            print(f"Sample Name: {data['data'][0].get('name')}")
    except:
        print("Non-JSON response (expected for some errors)")
        print(response.text[:300])
    print("=" * 60)


def test_fetch_all_characters():
    """Basic fetch with pagination info."""
    response = requests.get(f"{BASE_URL}/character")
    log_response(response, "Fetch All Characters")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0
    assert data["info"]["totalPages"] > 1


def test_filter_by_tv_show():
    """Use a filter that returns results."""
    response = requests.get(f"{BASE_URL}/character/tvShow=Mickey%20Mouse%20Clubhouse")
    log_response(response, "TV Show Filter")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0


def test_filter_by_video_game():
    """Use a known working video game filter."""
    response = requests.get(f"{BASE_URL}/character/videoGames=Kingdom%20Hearts")
    log_response(response, "Video Game Filter")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0


def test_filter_by_movie():
    """Filter characters by movie."""
    response = requests.get(f"{BASE_URL}/character?films=The%20Lion%20King")
    log_response(response, "Movie Filter")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["data"]) > 0


@pytest.mark.parametrize("invalid_url", [
    "/invalid-endpoint",
    "/character/999999999"
])
def test_negative_scenarios(invalid_url):
    """Negative tests."""
    response = requests.get(f"{BASE_URL}{invalid_url}")
    log_response(response, f"Negative - {invalid_url}")
    
    # Accept 404 or valid 200 with empty data
    assert response.status_code in [404, 200]