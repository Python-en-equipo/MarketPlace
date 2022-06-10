from collections import defaultdict


class ShoppingCart:
    # TODO: add object session
    def __init__(self,) -> None:
        self.cart = defaultdict(dict)

    def add_product(self, product):
        if product["id"] not in self.cart.keys():
            self.cart[product["id"]] = {
                "product_id": product["id"],
                "title": product["title"],
                "description": product["description"],
                "quantity": 1,
                "price": product["price"],
            }
        else:
            self.increment_product(product)

    def delete_product(self, product):
        product_id = product["id"]
        old_product = self.cart.get(product_id, None)
        if old_product is not None:
            del self.cart[product_id]

    def decrement_product(self, product):
        product_id = product["id"]
        old_product = self.cart.get(product_id, None)
        if old_product is None:
            print("El producto no existe en el carrito de compras")
            return

        if old_product["quantity"] > 1:
            old_product["quantity"] -= 1
        else:
            self.delete_product(product)

    def increment_product(self, product):
        product_id = product["id"]
        old_product = self.cart[product_id]
        old_product["quantity"] += 1
        self.cart[product_id] = old_product

    def reset_cart(self):
        self.cart = defaultdict(dict)

    def save(self):
        pass


# product1 = {
#     "id": 1,
#     "title": "Sandalia gucci",
#     "description": "Las sandalias gucci de cartier",
#     "quantity": 1,
#     "price": 18.9,
# }
# product2 = {
#     "id": 1,
#     "title": "Sandalia gucci",
#     "description": "Las sandalias gucci de cartier black",
#     "quantity": 1,
#     "price": 18.9,
# }
# product3 = {
#     "id": 1,
#     "title": "Sandalia gucci Rojas",
#     "description": "Las sandalias gucci de cartier Rojas",
#     "quantity": 2,
#     "price": 18.9,
# }
# product4 = {
#     "id": 2,
#     "title": "Suerter Polo Azul",
#     "description": "Sueter Polo Azul de algodon 100% puro",
#     "quantity": 2,
#     "price": 50.23,
# }
# product5 = {
#     "id": 2,
#     "title": "Suerter Polo Azul",
#     "description": "Sueter Polo Azul de algodon 100% puro",
#     "quantity": 2,
#     "price": 50.23,
# }
# shopping_cart = ShoppingCart()
# shopping_cart.add_product(product1)
# shopping_cart.add_product(product2)
# shopping_cart.add_product(product3)
# pprint(shopping_cart.cart)
# shopping_cart.decrement_product(product1)
# # shopping_cart.reset_cart()
# shopping_cart.add_product(product4)
# # print(shopping_cart.cart)
# pprint(shopping_cart.cart)
