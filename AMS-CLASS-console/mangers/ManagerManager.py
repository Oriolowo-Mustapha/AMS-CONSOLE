from models.Manager import Manager


class ManagerManager:
    manager: Manager

    def create_manager(self, email: str, password: str, first_name: None, last_name: None, phone: None):
        self.manager = Manager(email=email, password=password)
        self.manager.first_name = first_name
        self.manager.last_name = last_name
        self.manager.phone = phone
        return True

    def view_details(self):
        print(self.manager.id, '.', ' ', self.manager.first_name, ' ', self.manager.last_name,
              '\t', self.manager.email, ' ', self.phone)

    def update_manager(self, email: str, first_name: None, last_name: None, phone: None):
        if self.manager != None:
            self.manager.email = email
            self.manager.first_name = first_name
            self.manager.last_name = last_name
            self.manager.phone = phone
            return True
        else:
            return False
