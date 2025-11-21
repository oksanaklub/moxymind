import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com"


def login(driver, username: str, password: str):
    """log in function."""
    driver.get(BASE_URL)

    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys(username)

    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').clear()
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)

    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()


@pytest.mark.usefixtures("driver")
class TestSauceDemo:
    """
    Technical test(Moxymind) –  https://www.saucedemo.com
    Python + Selenium + pytest.
    """

    def test_successful_login_valid_user(self, driver):
        """
        Check that user can login succesfully.
        """
        login(driver, "standard_user", "secret_sauce")

        # Waiting "Products" title is available
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        assert "inventory.html" in driver.current_url
        assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(inventory_items) > 0

    def test_locked_out_user_cannot_login(self, driver):
        """
        Checking that blocked user is not able to login.
        """
        login(driver, "locked_out_user", "secret_sauce")

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
        )

        assert "locked out" in error.text.lower()
        # Leaving the log in page
        assert driver.current_url.startswith(BASE_URL)

    def test_add_to_cart_and_successful_checkout(self, driver):
        """
        Checking the main basket flow:
        - log in
        - Adding goods
        - switching to the basket
        - checkout
        - confirmation the order.
        """
        login(driver, "standard_user", "secret_sauce")

        # Adding twp items
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]'
        ).click()

        # Waiting the icon with number "2"
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "2"

        # Switching to the basket
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        assert "cart.html" in driver.current_url

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 2

        # Checkout
        driver.find_element(By.CSS_SELECTOR, '[data-test="checkout"]').click()

        # Wating till the page checkout step one will be loaded
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-one")
        )

        # Waiting untill fields will be clickable
        first_name_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="firstName"]'))
        )
        last_name_input = driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]')
        postal_code_input = driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]')

        first_name_input.send_keys("Oksana")
        last_name_input.send_keys("Lname")
        postal_code_input.send_keys("04001")


        driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()

        # Waiting until URL wil change to 2 checkout
        WebDriverWait(driver, 10).until(
            EC.url_contains("checkout-step-two")
        )
        assert "checkout-step-two" in driver.current_url

        # Check subtotal / total available
        total_label = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        assert "Total" in total_label

        # Finishing order
        driver.find_element(By.CSS_SELECTOR, '[data-test="finish"]').click()
        assert "checkout-complete.html" in driver.current_url

        header = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert header == "Thank you for your order!"

    def test_remove_items_from_cart(self, driver):
        """
        Checking that user can remove the added goods and basket is empty.
        """
        login(driver, "standard_user", "secret_sauce")

        # Adding two items to basket
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bike-light"]'
        ).click()

        # Cheking that icon with number 2 is displayed
        badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        assert badge.text == "2"

        # Switching to the basket
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("cart")
        )

        # Checking that two positions are displayed in the basket
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 2

        # Removing the items from the basket
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="remove-sauce-labs-backpack"]'
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, '[data-test="remove-sauce-labs-bike-light"]'
        ).click()

        # Cheking that basket is empty
        cart_items_after = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items_after) == 0
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0