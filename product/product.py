class Product:
    def __init__(self, product_id, name, price, quantity=1):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Produs: ID {self.product_id} Nume: {self.name} Pret: {self.price} Cantitate: {self.quantity}"
