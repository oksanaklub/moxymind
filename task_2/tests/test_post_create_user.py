import json
import requests
import re
import time

BASE_URL = "https://reqres.in/api"


def load_test_data():
    with open("data/users.json", "r") as f:
        return json.load(f)


def test_post_create_user():
    """
    Test Case 2 – POST Create User
    Requirements:
    - Send request
    - Assert HTTP status
    - Assert id & createdAt timestamp
    - Data-driven using external JSON
    - Assert response time < limit
    """
    test_data = load_test_data()

    for user in test_data:
        start_time = time.time()
        response = requests.post(f"{BASE_URL}/users", json=user)
        duration_ms = (time.time() - start_time) * 1000

        assert response.status_code == 201

        json_body = response.json()

        # "id" exists and is string/integer
        assert "id" in json_body
        assert isinstance(json_body["id"], (str, int))

        # "createdAt" exists and matches ISO 8601 timestamp
        assert "createdAt" in json_body
        assert re.match(r"\d{4}-\d{2}-\d{2}T", json_body["createdAt"])

        # Response time < 100 ms
        assert duration_ms < 100, f"Response took {duration_ms} ms"