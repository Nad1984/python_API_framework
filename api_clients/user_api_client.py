from api_clients.abstract_api_client import AbstractApiClient


class UserApiClient(AbstractApiClient):
    def create_user(self, user_data: dict):
        return self.post("user", user_data)

    def create_users_list(self, user_data: dict):
        return self.post("user/createWithList", user_data)

    def user_login(self, user_name, user_pass):
        return self.get("user/login", username=user_name, password=user_pass)

    def user_logout(self):
        return self.get("user/logout")

    def find_user_by_name(self, user_name):
        return self.get("user/" + str(user_name))




