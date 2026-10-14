
def test_login_success(page):
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    assert page.url.endswith("/inventory.html")


def test_login_wrong_password(page):
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()
    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()
    assert "Username and password do not match" in error_message.inner_text()


def test_products_display(logged_in_page):
    products = logged_in_page.locator(".inventory_item")
    products.first.wait_for(state="visible")
    assert products.count() > 0


def test_add_product_to_cart(logged_in_page):
    logged_in_page.locator(".inventory_item").first.locator("button").click()
    cart_badge = logged_in_page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "1"


def test_remove_product_from_cart(logged_in_page):
    logged_in_page.locator(".inventory_item").first.locator("button").click()
    logged_in_page.locator(".shopping_cart_link").click()

    product = logged_in_page.get_by_text("Sauce Labs Backpack", exact=True)
    assert product.is_visible()

    logged_in_page.get_by_role("button", name="Remove").click()
    assert logged_in_page.locator(".shopping_cart_badge").count() == 0


def test_login_empty_username(page):
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()
    assert "Username is required" in error_message.inner_text()


def test_login_empty_password(page):
    page.locator("#user-name").fill("standard_user")
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")
    assert error_message.is_visible()
    assert "Password is required" in error_message.inner_text()
