from product.product import Product
from product.productsRepository import ProductsRepository
from user.user import User
from user.usersRepository import UsersRepository


product_repository1 = ProductsRepository()
product_repository1.create({"name": "orhidee", "price": 60, "quantity": 3})
product_repository1.create({"name": "crin", "price": 15, "quantity": 2})
product_repository1.create({"name": "trandafir", "price": 50, "quantity": 10})

# product_repository1.read(1)
# product_repository1.read(2)
# product_repository1.read(3)
# product_repository1.read(4)
# product_repository1.read(10)



# product_repository1.read(3)
# print("---" * 25)
#
# product_repository1.update(3, {"name": "bujor", "price": 10, "quantity": 5})
#
# product_repository1.read(3)


# product_repository1.read(2)
# print("---" * 25)
# product_repository1.delete(2)
# print("---" * 25)
# product_repository1.read(2)


# print("---" * 25)
# product_repository1.read(1)
#
# product_repository1.update(1, {"name": "lalea", "price": 9, "quantity": 29})
# print("---" * 25)
# product_repository1.read(1)






user_repository1 = UsersRepository()
user_repository1.create({"username": "primul_utilizator", "email": "primul_utilizator@gmail.com", "password": "12345"})
user_repository1.create({"username": "user2", "email": "user2@gmail.com", "password": "abc123"})
user_repository1.create({"username": "user3", "email": "random123@gmail.com", "password": "qwerty123"})

# user_repository1.read(1)
# user_repository1.read(2)
# user_repository1.read(3)



# user_repository1.read(0)
# user_repository1.update(1, {"username": "primul_utilizator", "email": "primul_utilizator@gmail.com", "password": "12345"})
# user_repository1.delete(0)

# user_repository1.read(1)
# user_repository1.update(1, "username": "primul_utilizator", "email": "primul_utilizator@gmail.com", "password": "12345")
# user_repository1.read(1)









# product_repository1.update(3, {"nume": "bujor", "price": 10, "quantity": 5})


# TEMA: sa nu ne mai dea erori - pentru "nume" in loc de "name"
