import requests

base_url = "https://ru.yougile.com/api-v2/projects"
token = "kmyp0O4SWpnY0ec3J+390o617naNk0cQ1Xf0+MrT23FfgwSFdEcBvrR653lAp9oH"
project_id = "415d5be0-1407-4400-9e8a-ebbfe78280c7"
invalid_project_id = "00000000-0000-0000-0000-000000000000"
invalid_token = "invalid_token_example"


# Функция для получения проекта по ID
def get_project_by_id(project_id, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    get_url = f"{base_url}/{project_id}"

    response = requests.get(get_url, headers=headers)

    return response


# Позитивный тест для получения проекта по ID
def test_get_project_positive():
    try:
        response = get_project_by_id(project_id, token)

        print(f"Ответ от сервера на GET-запрос: {response.status_code} - {response.text}")

        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

        project_details = response.json()
        print(f"Детали проекта: {project_details}")

        assert "id" in project_details, "Проект не содержит поля 'id'"
        print(f"Проект с ID '{project_details['id']}' получен успешно.")

    except Exception as e:
        print(f"Ошибка при получении проекта: {e}")


# Негативный тест для получения проекта с несуществующим ID
def test_get_project_negative_not_found():
    try:
        response = get_project_by_id(invalid_project_id, token)

        print(f"Ответ от сервера на запрос с несуществующим ID: {response.status_code} - {response.text}")

        assert response.status_code == 404, f"Ожидался статус 404, но получен {response.status_code}"

        print(f"Проект с ID '{invalid_project_id}' не найден. Негативный тест прошел успешно.")

    except Exception as e:
        print(f"Ошибка при выполнении негативного теста: {e}")


# Негативный тест для получения проекта с невалидным токеном
def test_get_project_negative_invalid_token():
    try:
        response = get_project_by_id(project_id, invalid_token)

        print(f"Ответ от сервера на запрос с невалидным токеном: {response.status_code} - {response.text}")

        assert response.status_code == 401, f"Ожидался статус 401, но получен {response.status_code}"

        print(f"Токен невалиден. Негативный тест прошел успешно.")

    except Exception as e:
        print(f"Ошибка при выполнении негативного теста: {e}")


# Основная функция
def main():
    print("Запуск позитивного теста:")
    test_get_project_positive()

    print("\nЗапуск негативных тестов:")
    test_get_project_negative_not_found()
    test_get_project_negative_invalid_token()


# Запуск основного процесса
if __name__ == "__main__":
    main()