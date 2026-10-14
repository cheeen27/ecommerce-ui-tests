
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def get_product_count(self):
        return self.products.count()

    def add_first_product_to_cart(self):
        self.products.first.locator("button").click()

    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self):
        self.cart_link.click()
