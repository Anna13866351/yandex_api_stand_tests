# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# def get_logs():
#      return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})
# response = get_logs()
# print(response.status_code)
# print(response.headers) 

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
# print(response)
# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя

def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#  # Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
#  response = post_new_user(data.user_body)

# # Вывод HTTP-статус кода ответа на запрос
# # Код состояния указывает на результат обработки запроса сервером
# print(response.status_code)
# print(response.json())

def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids)
response = post_products_kits(data.products_ids)
print(response.status_code)
print(response.json())