import requests
import json
from utilities.filereader import readconfigfile
import pytest
from models.githubstatus import StatusResponseModel

def test_getapi():
    base_url = readconfigfile()
    response = requests.get(base_url)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"



def test_verify_github_status_schema():
    # 1. This mimics the actual dict you get back from 'response.json()'
    api_response_json = {
        "ok": True,
        "data": {
            "slug": "github",
            "name": "GitHub",
            "category": "cloud",
            "logo_url": "https://t3.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://github.com&size=128",
            "status": "operational",
            "official_indicator": None,
            "report_count_1h": 0,
            "report_count_24h": 0,
            "status_page_url": "https://isitdownstatus.com/en/status/github",
            "updated_at": "2026-06-28T17:49:45.193Z"
        }
    }
    
    # 2. Validate the complete schema
    try:
        # The ** unpacks the dictionary into the Pydantic validator
        validated_data = StatusResponseModel(**api_response_json)
        
    except Exception as e:
        # If a single key is missing or data type is corrupted, the test fails explicitly here
        pytest.fail(f"Schema validation failed! Errors found: {e}")
        
    # 3. Optional: You can now access data cleanly using dot notation for specific assertions
    assert validated_data.ok is True
    assert validated_data.data.slug == "github"
    assert validated_data.data.report_count_1h == 0