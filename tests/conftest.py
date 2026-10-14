
import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        yield page

        browser.close()


@pytest.fixture
def logged_in_page(page, login_page):
    login_page.login("standard_user", "secret_sauce")

    page.locator(".inventory_item").first.wait_for(state="visible")

    return page


@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(logged_in_page):
    return InventoryPage(logged_in_page)

@pytest.fixture
def cart_page(logged_in_page):
    return CartPage(logged_in_page)