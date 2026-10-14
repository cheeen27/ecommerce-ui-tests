
class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.remove_button = page.get_by_role(
            "button", name="Remove"
        )

    def open(self):
        self.cart_link.click()

    def is_product_visible(self, product_name):
        return self.page.get_by_text(
            product_name, exact=True
        ).is_visible()

    def remove_first_product(self):
        self.remove_button.click()
