import allure
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from data import INGREDIENTS_FOR_BURGER, USER_DATA_FOR_CREATE_ORDER, INGREDIENTS_FOR_BURGER_EMPTY, \
    INGREDIENTS_FOR_BURGER_INCORRECT


class TestGetOrder:

    @allure.title('Проверяем, получение заказов конкретного пользователя (неавторизованный пользователь).')
    @allure.description('Проверяем, что при попытке получить заказы без авторизации, получаем ошибку.')
    def test_get_orders_without_auth_fails(self):
        order_api = OrderMethods()
        response = order_api.get_user_orders('')
        assert response.status_code == 401, f"Ожидался код 401, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get(
            'success') is False, f"Ожидалось success=False, но получили {response_json.get('success')}"
        expected_message = "You should be authorised"
        assert response_json.get(
            'message') == expected_message, f'Ответ API:{response_json}'

    @allure.title('Проверяем, получение заказов конкретного пользователя (авторизованный пользователь).')
    @allure.description('Проверяем, что при попытке получить заказы c авторизованным пользователем, получаем заказы.')
    def test_get_orders_with_auth_success(self):
        user_api = UserMethods()
        response_user = user_api.login_user(USER_DATA_FOR_CREATE_ORDER)
        token = user_api.get_access_token(response_user)
        order_api = OrderMethods()
        response_order = order_api.get_user_orders(token)
        assert response_order.status_code == 200, f"Ожидался код 200, но получили {response_order.status_code}"
        response_order_json = response_order.json()
        assert response_order_json.get('success') == True, f"Ответ API: {response_order_json}"
        assert "orders" in response_order_json, "Ключ 'orders' отсутствует в ответе"
