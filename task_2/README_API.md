# Moxymind Technical Task #2 – API Automation  
### Python + Pytest + Requests

This project contains automated API tests for **Reqres API** (https://reqres.in), implemented as part of the Moxymind technical assignment.  
The test suite covers GET and POST scenarios required in the assignment and demonstrates data-driven testing, schema validation, and response time checks.

## 🚀 Tech Stack
- Python 3.11
- Pytest
- Requests
- JSON test data

## 📁 Project Structure
```
task_2/
│
├── README.md
├── requirements.txt
│
├── data/
│   └── users.json
│
└── tests/
    ├── test_get_list_users.py
    └── test_post_create_user.py
```

## ⚙️ Installation
```
python3 -m pip install -r requirements.txt
```

## 🧪 Running Tests
```
python3 -m pytest -v
```

## 🧠 Implemented Scenarios

### ✔️ GET – List Users
- Validate status code
- Validate `total`
- Validate user last names
- Validate number of users

### ✔️ POST – Create User (Data-Driven)
- Validate status code
- Validate `id` and `createdAt`
- Timestamp format check
- Response time < 100 ms
- Data-driven JSON input

## ✔️ Conclusion
This API automation suite demonstrates clean, maintainable REST API test design with data-driven execution, schema validation, and time-based assertions.
