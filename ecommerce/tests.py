# from django.test import TestCase
# from django.urls import reverse

# from .models import Product


# def create_product(title_prod, description_prod, price_prod):
#     """
#     Create a product with the given info
#     """
#     product_inst = Product.objects.create(title=title_prod, description=description_prod, price=price_prod)
#     return product_inst


# class ProductModelTests(TestCase):
#     def test_product_was_not_created(self):
#         """
#         Check that a product with a price below 50 it is not created
#         """
#         inst_product = create_product("producto con precio bajo", "descripcion dummy", 30)
#         self.assertIs(inst_product.was_created(), False)

#     def test_product_was_created(self):
#         """
#         Check that a product with a price equal or above 50 it is created
#         """
#         inst_product = create_product("producto con precio aceptable", "descripcion dummy", 50)
#         self.assertIs(inst_product.was_created(), True)


# class ProductHomeTests(TestCase):
#     def test_no_products(self):
#         """
#         If no products exist, the page should be empty.
#         """
#         response = self.client.get(reverse("ecommerce:home"))
#         self.assertEqual(response.status_code, 200)
#         self.assertQuerysetEqual(response.context["products"], [])

    # TESTS DEPRECADOS PORQUE YA NO NOS FIJAMOS EN EL PRECIO, SINO EN LA DISPONIBILIDAD!
    # def test_product_wrong_price(self):
    #     """
    #     If the product has a price below 50, should not appear in the home
    #     """
    #     product_inst = create_product("Title", "Description", 5)
    #     response = self.client.get(reverse("ecommerce:home"))
    #     self.assertQuerysetEqual(response.context["products"], [])

    # def test_product_right_price(self):
    #     """
    #     If the product has a price equal or above 50, it should in the home
    #     """
    #     product_inst = create_product("Product with right price", "Description", 50)
    #     response = self.client.get(reverse("ecommerce:home"))
    #     self.assertQuerysetEqual(response.context["products"], ["<Product: Product with right price>"])

    # def test_two_products_right_and_wrong(self):
    #     """
    #     Two products are created, one with a low price, and the other with an acceptable price
    #     It should only appear the product which price is above or equal 50
    #     """
    #     wrong_product = create_product("Producto no aceptado", "descripcion dummy", 49)
    #     right_product = create_product("Producto aceptable", "descripcion dummy", 50)
    #     response = self.client.get(reverse("ecommerce:home"))
    #     self.assertQuerysetEqual(response.context["products"], ["<Product: Producto aceptable>"])

    # def test_two_right_products(self):
    #     """
    #     Two products are created, one with a low price, and the other with an acceptable price
    #     It should only appear the product which price is above or equal 50
    #     """
    #     wrong_product = create_product("Producto aceptable 1", "descripcion dummy", 67)
    #     right_product = create_product("Producto aceptable 2", "descripcion dummy", 50)
    #     response = self.client.get(reverse("ecommerce:home"))
    #     self.assertQuerysetEqual(
    #         response.context["products"],
    #         ["<Product: Producto aceptable 1>", "<Product: Producto aceptable 2>"],
    #         ordered=False,
    #     )

    # def test_two_wrong_products(self):
    #     """
    #     Two products are created, one with a low price, and the other with an acceptable price
    #     It should only appear the product which price is above or equal 50
    #     """
    #     wrong_product = create_product("Producto no aceptado 1", "descripcion dummy", 20)
    #     right_product = create_product("Producto no aceptado 2", "descripcion dummy", 49)
    #     response = self.client.get(reverse("ecommerce:home"))
    #     self.assertQuerysetEqual(response.context["products"], [])
