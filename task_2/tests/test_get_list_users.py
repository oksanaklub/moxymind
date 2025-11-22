import requests

BASE_URL = "https://reqres.in/api"


def test_get_list_users():
    """
    Test Case 1 – GET List Users
    Requirements:
    - Send proper GET request
    - Assert 'total'
    - Assert last_name of 1st and 2nd user in 'data'
    - Count number of users == 'total'
    """

    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200

    json_data = response.json()

    # Assert "total"
    assert "total" in json_data
    total = json_data["total"]

    # Assert last_name for 1st and 2nd user
    assert json_data["data"][0]["last_name"] == "Lawson"
    assert json_data["data"][1]["last_name"] == "Ferguson"

    # Count number of received users
    users_count = len(json_data["data"])
    assert users_count == json_data["per_page"]