import sender_stand_request
import data

def get_new_user_token():
    #Создаёт нового пользователя и возвращает его authToken
    user_body = data.user_body.copy()
    user_response = sender_stand_request.post_new_user(user_body)
    return user_response.json()["authToken"]

def get_kit_body(name):
    #Возвращает копию шаблона с подставленным name
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body, auth_token):
    #Позитивная проверка: набор создан, name совпадает.
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body, auth_token):
    #Негативная проверка: код ответа 400.
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# 1. Допустимое количество символов (1): "a"
def test_01_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body("a"), auth_token)

# 2. Допустимое количество символов (511)
def test_02_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body(data.KIT_NAME_511), auth_token)

# 3. Количество символов меньше допустимого (0): ""
def test_03_create_kit_empty_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400(get_kit_body(""), auth_token)

# 4. Количество символов больше допустимого (512)
def test_04_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400(get_kit_body(data.KIT_NAME_512), auth_token)

# 5. Разрешены английские буквы: "QWErty"
def test_05_create_kit_english_letters_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body("QWErty"), auth_token)

# 6. Разрешены русские буквы: "Мария"
def test_06_create_kit_russian_letters_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body("Мария"), auth_token)

# 7. Разрешены спецсимволы: "\"№%@\","
def test_07_create_kit_special_symbols_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body('"№%@",'), auth_token)

# 8. Разрешены пробелы: " Человек и КО "
def test_08_create_kit_spaces_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body(" Человек и КО "), auth_token)

# 9. Разрешены цифры: "123"
def test_09_create_kit_digits_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert(get_kit_body("123"), auth_token)

# 10. Параметр не передан в запросе: {} (нет поля name)
def test_10_create_kit_no_name_get_error_response():
    auth_token = get_new_user_token()
    # НЕ используем get_kit_body — нужно тело без поля name
    kit_body = {}
    negative_assert_code_400(kit_body, auth_token)

# 11. Передан другой тип параметра (число): {"name": 123}
def test_11_create_kit_numeric_name_get_error_response():
    auth_token = get_new_user_token()
    # НЕ используем get_kit_body — там всегда строка
    kit_body = {"name": 123}
    negative_assert_code_400(kit_body, auth_token)