

def test_login_success(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    assert page.url.endswith("/inventory.html")


def test_login_wrong_password(login_page):
    login_page.login("standard_user", "wrong_password")

    assert login_page.error_message.is_visible()
    assert "Username and password do not match" in (
        login_page.error_message.inner_text()
    )


def test_products_display(inventory_page):
    assert inventory_page.get_product_count() > 0


def test_add_product_to_cart(inventory_page):
    inventory_page.add_first_product_to_cart()
    assert inventory_page.get_cart_count() == 1


def test_remove_product_from_cart(inventory_page, cart_page):
    inventory_page.add_first_product_to_cart()
    cart_page.open()

    assert cart_page.is_product_visible("Sauce Labs Backpack")

    cart_page.remove_first_product()
    assert inventory_page.get_cart_count() == 0



def test_login_empty_username(login_page):
    login_page.login("", "secret_sauce")

    assert login_page.error_message.is_visible()
    assert "Username is required" in (
        login_page.error_message.inner_text()
    )


def test_login_empty_password(login_page):
    login_page.login("standard_user", "")

    assert login_page.error_message.is_visible()
    assert "Password is required" in (
        login_page.error_message.inner_text()
    )


def test_cart_contains_added_product(inventory_page, cart_page):
    first_product = inventory_page.products.first
    product_name = first_product.locator(
        ".inventory_item_name"
    ).inner_text()

    inventory_page.add_first_product_to_cart()
    cart_page.open()

    assert cart_page.is_product_visible(product_name)