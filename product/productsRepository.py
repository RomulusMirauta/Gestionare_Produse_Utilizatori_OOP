from repositoryInterface import RepositoryInterface
from product.product import Product


class ProductsRepository:
    def __init__(self):
        self.products = []

    def create(self, data):
        product_id = len(self.products) + 1
        new_product = Product(product_id, data["name"], data["price"], data["quantity"])
        self.products.append(new_product)

    def read(self, entry_id):
        for product in self.products:
            if product.product_id == entry_id:
                print("Produsul a fost gasit, mai jos avem detaliile produsului")
                print("Numele produsului este:", product.name)
                print("Pretul este: ", product.price)
                print("Cantitatea de produs este: ", product.quantity)
                break
        else:
            print(f"The product with id {entry_id} is not available.")

    def update(self, entry_id, new_data):
        for product in self.products:
            if product.product_id == entry_id:
                # product.product_id = new_data['entry_id']
                product.name = new_data['name']
                product.price = new_data['price']
                product.quantity = new_data['quantity']
                print("Produsul a fost actualizat")
                break
        else:
            print("Produsul nu a fost updatat deoarece nu a fost gasit!")

    def delete(self, entry_id):
        for product in self.products:
            if product.product_id == entry_id:
                self.products.remove(product)
                print("Produsul a fost sters")
                break
        else:
            print("Produsul nu a fost sters deoarece nu a fost gasit!")









    # def read(self):
    #     print(f"Produsele sunt: {str(self.products)}")
    #     # if len(self.products) == 0:
    #     #     print(f"Produsele sunt: {self.products}")
    #     #     # de implementat citirea unui produs specific / produsul adaugat ultima data
    #     # else:
    #     #     print("Nu exista produse!")





    # def update(self, data):
    #     product_id_update = int(input("Introduceti ID-ul produsului pe care doriti sa il modificati: \n"))
    #
    #     while len(self.products) > 0:
    #         if 0 < product_id_update < len(self.products):
    #             product_id = len(self.products) + 1
    #             new_product = Product(product_id, data["name"], data["price"], data["quantity"])
    #             self.products.append(new_product)
    #             self.products[0]
    #         else:
    #             print("ID produs invalid!")
    #     else:
    #         print("Nu exista produse!")






    # def delete(self, data):
    #     print(f"Produsele sunt: {self.products}")


# create User package, class User, create usersRepository.py
# continue CRUD
