import allure
from methods.user_methods import UserMethods
from data import USER_DATA_FOR_LOGIN_EXISTING, USER_INVALID_CREDENTIALS


class TestLoginUser:

    @allure.title('Проверяем логин под существующим пользователем.')
    @allure.description('Авторизуемся под существующим пользователем.')
    def test_login_user_success(self):
        user_api = UserMethods()
        response = user_api.login_user(USER_DATA_FOR_LOGIN_EXISTING)
        assert response.status_code == 200, f"Ожидался код 200, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get('success') == True, f"Ответ API: {response_json}"

    @allure.title('Проверяем логин с неверным логином и паролем.')
    @allure.description('Авторизуемся с неверным логином и паролем.')
    def test_login_with_invalid_credentials_fails(self):
        user_api = UserMethods()
        response = user_api.login_user(USER_INVALID_CREDENTIALS)
        assert response.status_code == 401, f"Ожидался код 401, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get(
            'success') is False, f"Ожидалось success=False, но получили {response_json.get('success')}"
        assert response_json.get(
            'message') == "email or password are incorrect", f'Ожидалось "message": "email or password are incorrect", но получили {response_json.get('message')}'
