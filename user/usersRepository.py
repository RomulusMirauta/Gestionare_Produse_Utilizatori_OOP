from repositoryInterface import RepositoryInterface
from user.user import User


class UsersRepository:
    def __init__(self):
        self.users = []

    def create(self, data):
        user_id = len(self.users) + 1
        new_user = User(user_id, data["username"], data["email"], data["password"])
        self.users.append(new_user)

    def read(self, entry_id):
        for user in self.users:
            if user.user_id == entry_id:
                print("Utilizatorul a fost gasit, mai jos avem detaliile utilizatorului")
                print("Numele utilizatorului este:", user.username)
                print("Email-ul este: ", user.email)
                print("Parola este: ", user.password) # de implementat afisare cu stelute
                break
        else:
            print(f"The user with id {entry_id} is not available.")

    def update(self, entry_id, new_data):
        for user in self.users:
            if user.user_id == entry_id:
                # user.user_id = new_data['entry_id']
                user.username = new_data['username']
                user.email = new_data['email']
                user.password = new_data['password']
                print("Datele utilizatorului au fost actualizate")
                break
        else:
            print("Datele utilizatorului nu au fost actualizate deoarece utilizatorul nu a putut fi gasit!")

    def delete(self, entry_id):
        for user in self.users:
            if user.user_id == entry_id:
                self.users.remove(user)
                print("Utilizatorul a fost sters")
                break
        else:
            print("Utilizatorul nu a fost sters deoarece nu a fost gasit!")