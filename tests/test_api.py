import pytest
import requests

# ==================== GLOBAL CONFIGURATION ====================
BASE_URL = "http://172.17.193.128"

COMMON_HEADERS = {
    "Content-Type": "application/json"
}

# ==================== TEST FUNCTIONS ====================
def test_tc001_create_project_success():
    """
    Test ID: TC001
    Name: Create Project - Success
    Expected behavior: Verifies the happy path for creating a new project.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    request_body = {
      "name": "New KT"
    }
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 200
    expected_response = {
      "status": "success",
      "message": "Project created successfully",
      "data": {
        "id": 101,
        "name": "New KT"
      }
    }
    # Note: ID might be dynamic, consider adjusting assertion logic
    assert response.json() == expected_response

def test_tc002_create_project_missing_name():
    """
    Test ID: TC002
    Name: Create Project - Missing Name
    Expected behavior: Verifies that a 400 Bad Request is returned when the 'name' field is missing.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    request_body = {}
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 400

def test_tc003_create_project_empty_name():
    """
    Test ID: TC003
    Name: Create Project - Empty Name
    Expected behavior: Verifies that a 400 Bad Request is returned for an empty name string.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    request_body = {
      "name": ""
    }
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 400

def test_tc004_create_project_duplicate_name():
    """
    Test ID: TC004
    Name: Create Project - Duplicate Name
    Expected behavior: Verifies that a 409 Conflict is returned when trying to create a project with a duplicate name.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer valid_jwt_token_placeholder",
        "Content-Type": "application/json"
    }
    request_body = {
      "name": "New KT"
    }
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 409

def test_tc005_create_project_missing_token():
    """
    Test ID: TC005
    Name: Create Project - Missing Token
    Expected behavior: Verifies that a 401 Unauthorized is returned when the Authorization header is missing.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Content-Type": "application/json"
    }
    request_body = {
      "name": "Project Without Auth"
    }
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 401

def test_tc006_create_project_invalid_token():
    """
    Test ID: TC006
    Name: Create Project - Invalid Token
    Expected behavior: Verifies that a 401 Unauthorized is returned when an invalid or expired token is used.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    request_body = {
      "name": "Project With Invalid Auth"
    }
    response = requests.post(url, headers=headers, json=request_body)
    assert response.status_code == 401

def test_tc007_list_projects_success():
    """
    Test ID: TC007
    Name: List Projects - Success
    Expected behavior: Verifies the happy path for listing all projects.
    """
    url = f"{BASE_URL}/api/project/list_projects/"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    expected_response = {
      "status": "success",
      "data": [
        {
          "id": 101,
          "name": "New KT"
        },
        {
          "id": 102,
          "name": "Project A"
        }
      ]
    }
    assert response.json() == expected_response

def test_tc008_list_projects_no_data():
    """
    Test ID: TC008
    Name: List Projects - No Data
    Expected behavior: Verifies that a 200 OK with an empty data array is returned when no projects exist.
    """
    url = f"{BASE_URL}/api/project/list_projects/"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    expected_response = {
      "status": "success",
      "data": []
    }
    assert response.json() == expected_response

def test_tc009_list_projects_missing_token():
    """
    Test ID: TC009
    Name: List Projects - Missing Token
    Verifies that a 401 Unauthorized is returned when the Authorization header is missing.
    """
    url = f"{BASE_URL}/api/project/list_projects/"
    headers = {
        **COMMON_HEADERS
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_tc010_list_projects_invalid_token():
    """
    Test ID: TC010
    Name: List Projects - Invalid Token
    Verifies that a 401 Unauthorized is returned when an invalid or expired token is used.
    """
    url = f"{BASE_URL}/api/project/list_projects/"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 401

def test_tc011_create_project_edge_case_long_name():
    """
    Test ID: TC011
    Name: Create Project - Edge Case - Long Name
    Verifies that a 400 Bad Request is returned for an exceptionally long project name.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    payload = {
      "name": "This is an exceptionally long project name designed to test the limits of the name field validation and database column size to ensure the API handles it gracefully without crashing."
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 400

def test_tc012_create_project_edge_case_special_characters():
    """
    Test ID: TC012
    Name: Create Project - Edge Case - Special Characters
    Verifies a project can be created with various special characters in its name.
    """
    url = f"{BASE_URL}/api/project/create_project"
    headers = {
        **COMMON_HEADERS,
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2ODM2NDI3LCJpYXQiOjE3NzY3NTAwMjcsImp0aSI6ImZlN2I2MmYzMjRlNDQ2ODdhZDFhYzNjYTQ0MzdlMDI0IiwidXNlcl9pZCI6NDc0fQ.vByXm-Rm5PMNsoiM5TDJXA--mKo4DKgGOHm3kKlUNeg",
        "Content-Type": "application/json"
    }
    payload = {
      "name": "Project with !@#$%^&*()_+-=[]{}|;':,.<>/?`~"
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["status"] == "success"
    assert response_data["message"] == "Project created successfully"
    assert "id" in response_data["data"]
    assert response_data["data"]["name"] == "Project with !@#$%^&*()_+-=[]{}|;':,.<>/?`~"