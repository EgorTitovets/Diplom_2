import allure
from methods.user_methods import UserMethods
from data import NEW_USER, EXISTING_USER, USER_DATA_NO_PASSWORD


class TestCreateUser:

    @allure.title('Проверяем, что можно создать уникального пользователя.')
    @allure.description('Создаем нового пользователя, с новыми/корректными данными.')
    def test_create_user_success(self):
        user_api = UserMethods()
        response = user_api.create_user(NEW_USER)
        assert response.status_code == 200, f"Ожидался код 200, но получили {response.status_code}"
        response_json = response.json()  # Преобразуем response в JSON
        assert response_json.get('success') == True, f"Ответ API: {response_json}"
        # Достаем accessToken и убираем "Bearer "
        access_token = response_json["accessToken"].split(" ")[1]
        # Удаляем пользователя
        user_api.delete_user(access_token)

    @allure.title('Проверяем, что нельзя создать пользователя, который уже зарегистрирован.')
    @allure.description(
        'Создаем нового пользователя, с данными которые уже есть у существующего/зарегистрированного пользователя.')
    def test_create_existing_user_fails(self):
        user_api = UserMethods()
        response = user_api.create_user(EXISTING_USER)
        assert response.status_code == 403, f"Ожидался код 403, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get(
            'success') is False, f"Ожидалось success=False, но получили {response_json.get('success')}"
        assert response_json.get(
            'message') == "User already exists", f'Ожидалось "message": "User already exists", но получили {response_json.get('message')}'

    @allure.title('Проверяем, что нельзя создать пользователя, без одного из обязательных полей.')
    @allure.description(
        'Создаем нового пользователя, без указания пароля.')
    def test_create_user_without_password_fails(self):
        user_api = UserMethods()
        response = user_api.create_user(USER_DATA_NO_PASSWORD)
        assert response.status_code == 403, f"Ожидался код 403, но получили {response.status_code}"
        response_json = response.json()
        assert response_json.get(
            'success') is False, f"Ожидалось success=False, но получили {response_json.get('success')}"
        expected_message = "Email, password and name are required fields"
        assert response_json.get(
            'message') == expected_message, f'Ответ API:{response_json}'
