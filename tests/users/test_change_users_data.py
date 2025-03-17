import allure
from methods.user_methods import UserMethods
from data import USER_DATA_FOR_CHANGE_CREATE, USER_DATA_CHANGE_EMAIL, USER_DATA_CHANGE_NAME


class TestChangeUserData:

    @allure.title('Проверяем изменение данных пользователя (email). С авторизацией.')
    @allure.description('Изменяем у пользователя email.')
    def test_change_users_email_success(self):
        user_api = UserMethods()
        response = user_api.create_user(USER_DATA_FOR_CHANGE_CREATE)
        access_token = user_api.get_access_token(response)
        change_data = user_api.change_user_data(USER_DATA_CHANGE_EMAIL, access_token)
        assert change_data.status_code == 200, f"Ожидался код 200, но получили {change_data.status_code}"
        change_data_json = change_data.json()
        expected_email = USER_DATA_CHANGE_EMAIL["email"]
        assert change_data_json["user"][
                   "email"] == expected_email, f"Ожидался email {expected_email}, но получили {change_data_json['user']['email']}"
        user_api.delete_user(access_token)

    @allure.title('Проверяем изменение данных пользователя (name). С авторизацией.')
    @allure.description('Изменяем у пользователя name.')
    def test_change_users_name_success(self):
        user_api = UserMethods()
        response = user_api.create_user(USER_DATA_FOR_CHANGE_CREATE)
        access_token = user_api.get_access_token(response)
        change_data = user_api.change_user_data(USER_DATA_CHANGE_NAME, access_token)
        assert change_data.status_code == 200, f"Ожидался код 200, но получили {change_data.status_code}"
        change_data_json = change_data.json()
        expected_name = USER_DATA_CHANGE_NAME["name"]
        assert change_data_json["user"][
                   "name"] == expected_name, f"Ожидалось name {expected_name}, но получили {change_data_json['user']['name']}"
        user_api.delete_user(access_token)

    @allure.title('Проверяем изменение данных пользователя. Без авторизации.')
    @allure.description('Проверяем, что без авторизации данные не изменить и получаем ошибку.')
    def test_change_user_data_without_auth_fails(self):
        user_api = UserMethods()
        response = user_api.create_user(USER_DATA_FOR_CHANGE_CREATE)
        access_token = user_api.get_access_token(response)
        access_token_empty = ' '
        change_data = user_api.change_user_data(USER_DATA_CHANGE_NAME, access_token_empty)
        assert change_data.status_code == 401, f"Ожидался код 401, но получили {change_data.status_code}"
        change_data_json = change_data.json()
        expected_success = False
        expected_error_message = "You should be authorised"
        assert change_data_json.get(
            'success') is expected_success, f"Ожидалось success={expected_success}, но получили {change_data_json.get('success')}"
        assert change_data_json.get(
            'message') == expected_error_message, f'Ожидалось "message": {expected_error_message}", но получили {change_data_json.get('message')}'
        user_api.delete_user(access_token)
