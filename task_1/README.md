# Moxymind Technical Task – UI Automation  
### **Python + Selenium + Pytest**

This repository contains an automated UI test suite for **SauceDemo** (https://www.saucedemo.com/) implemented as part of the Moxymind technical assignment.

The test suite validates core e-commerce flows using Selenium WebDriver, Pytest, and Python.

---

## 🚀 **Tech Stack**

- **Python 3.11**
- **Pytest**
- **Selenium WebDriver**
- **webdriver-manager**
- **Chrome / Safari support**

---

## 📁 **Project Structure**

```
task_1/
│
├── README.md              # Project documentation
├── conftest.py            # Browser setup & fixtures
├── requirements.txt       # Dependencies
│
└── tests/
    ├── test_simple.py     # Sanity test
    └── test_saucedemo.py  # Main UI automation scenarios
```

---

## ⚙️ **Installation**

### Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

---

# 🌐 **Browser Configuration**

## **Chrome**

Runs by default.  

## **Safari (macOS only)**

To run tests in Safari you must enable automation:

### 1. Enable Developer mode in Safari:
```
Safari → Settings → Advanced → Show Develop menu
```

### 2. Allow remote automation:
```
Develop → Allow Remote Automation
```

### 3. Enable safaridriver:
```bash
safaridriver --enable
```

---

# 🧪 **Running Tests**

### **Run all tests in Chrome (default):**
```bash
python3 -m pytest -v
```

### **Run tests in Safari:**
```bash
python3 -m pytest -v --browser=safari
```

---

# 🧠 **Implemented Test Scenarios**

### ✔️ 1. Successful Login  
Validates login with a valid user and checks product list visibility.

### ✔️ 2. Login with Locked-Out User  
Ensures correct error handling and user-friendly message.

### ✔️ 3. Add Items to Cart & Complete Checkout  
Covers:
- login  
- adding items  
- verifying cart  
- checkout steps  
- order confirmation page

### ✔️ 4. Remove Items From Cart  
Confirms that a user can remove items and the cart becomes empty.