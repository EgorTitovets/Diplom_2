import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from data import INGREDIENTS_FOR_BURGER, USER_DATA_FOR_CREATE_ORDER, INGREDIENTS_FOR_BURGER_EMPTY, \
    INGREDIENTS_FOR_BURGER_INCORRECT


class TestCreateOrder:

    @allure.title('Проверяем, что можно создать заказ. (без авторизации)')
    @allure.description('Создаем новый заказ без авторизации.')
    def test_create_order_without_auth_success(self):
        order_api = OrderMethods()
        response = order_api.create_order_without_auth(INGREDIENTS_FOR_BURGER)
        assert response.status_code == 200, f"Ожидался код 200, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get('success') == True, f"Ответ API: {response_json}"

    @allure.title('Проверяем, что можно создать заказ. (c авторизацией)')
    @allure.description('Создаем новый заказ с авторизацией.')
    def test_create_order_with_auth_success(self):
        user_api = UserMethods()
        response_user = user_api.login_user(USER_DATA_FOR_CREATE_ORDER)
        token = user_api.get_access_token(response_user)
        order_api = OrderMethods()
        response_order = order_api.create_order_with_auth(INGREDIENTS_FOR_BURGER, token)
        assert response_order.status_code == 200, f"Ожидался код 200, но получили {response_order.status_code}"
        response_order_json = response_order.json()  # Преобразуем response в JSON
        assert response_order_json.get('success') == True, f"Ответ API: {response_order_json}"

    @allure.title('Проверяем, что нельзя создать заказ без ингредиентов.')
    @allure.description('Создаем новый заказ без ингредиентов.')
    def test_create_order_without_ingredients_fails(self):
        order_api = OrderMethods()
        response = order_api.create_order_without_auth(INGREDIENTS_FOR_BURGER_EMPTY)
        assert response.status_code == 400, f"Ожидался код 400, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get(
            'success') is False, f"Ожидалось success=False, но получили {response_json.get('success')}"
        expected_message = "Ingredient ids must be provided"
        assert response_json.get(
            'message') == expected_message, f'Ответ API:{response_json}'

    @allure.title('Проверяем, что нельзя создать заказ с неверным хешем ингредиентов.')
    @allure.description('Создаем новый заказ с неверным хешем ингредиентов.')
    def test_create_order_with_incorrect_ingredients_fails(self):
        order_api = OrderMethods()
        response = order_api.create_order_without_auth(INGREDIENTS_FOR_BURGER_INCORRECT)
        assert response.status_code == 500, f"Ожидался код 500, но получили {response.status_code}"
