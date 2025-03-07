import requests
import allure
from urls import Urls


class UserMethods:

    @allure.step("Создаем пользователя")
    def create_user(self, params):
        response = requests.post(f'{Urls.BASE_URL}{Urls.REGISTER_USER_URL}', json=params)
        print(response.json())
        return response

    @allure.step("Авторизуемся. Логин пользователя")
    def login_user(self, params):
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_USER_URL}', json=params)
        print(response.json())
        return response

    @allure.step("Изменяем данные пользователя")
    def change_user_data(self, params, token):
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.patch(f'{Urls.BASE_URL}{Urls.USER_URL}', json=params, headers=headers)
        print(response.json())
        return response

    @allure.step("Получаем данные о пользователе")
    def get_user_data(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(f'{Urls.BASE_URL}{Urls.USER_URL}', headers=headers)
        print(response.json())
        return response

    @allure.step("Удаляем пользователя")
    def delete_user(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.delete(f'{Urls.BASE_URL}{Urls.USER_URL}', headers=headers)
        print(response.json())
        return response


