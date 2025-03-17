import allure
import requests

from urls import Urls


class OrderMethods:

    @allure.step('Получение данных об ингредиентах')
    def get_ingredients_data(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.INGREDIENT_URL}')
        print(response.json())
        return response

    @allure.step('Создаем заказ, указывая нужные ингредиенты Без авторизации')
    def create_order_without_auth(self, order_data):
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_URL}', json=order_data)
        # print(response.json())
        return response

    @allure.step('Создаем заказ, указывая нужные ингредиенты C авторизацией')
    def create_order_with_auth(self, order_data, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDERS_URL}', json=order_data, headers=headers)
        print(response.json())
        return response

    @allure.step('Получаем заказы конкретного пользователя:')
    def get_user_orders(self, token):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDERS_URL}', headers=headers)
        print(response.json())
        return response
