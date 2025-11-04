from typing import List

import product


class Store:
    def __init__(self, product_list):
        self.product = product_list

    def add_product(self, product):
        self.product.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        try:
            self.product.remove(product)
        except ValueError:
            print(f"Product {product.name} not found in store.")

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in the store."""
        return sum(products.get_quantity() for products in self.product)

    def get_all_products(self) -> List[product.Product]:
        """Return a list of all active products in the store."""
        return [products for products in self.product if products.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0
        for products, quantity in shopping_list:
            try:
                total_price += products.buy(quantity)
            except Exception as e:
                print(f"Could not buy {products.name}: {e}")
        return total_price