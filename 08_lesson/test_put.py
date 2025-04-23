import requests

base_url = "https://ru.yougile.com/api-v2/projects"
token = "kmyp0O4SWpnY0ec3J+390o617naNk0cQ1Xf0+MrT23FfgwSFdEcBvrR653lAp9oH"
project_id = "415d5be0-1407-4400-9e8a-ebbfe78280c7"
invalid_project_id = "00000000-0000-0000-0000-000000000000"


# Функция для изменения проекта
def update_project(project_id, new_title, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    update_data = {
        "title": new_title
    }

    update_url = f"{base_url}/{project_id}"

    response = requests.put(update_url, headers=headers, json=update_data)

    return response


# Функция для получения проекта по ID
def get_project(project_id, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    get_url = f"{base_url}/{project_id}"

    response = requests.get(get_url, headers=headers)

    return response

# Позитивный тест для изменения проекта
def test_update_project_positive():
    new_project_title = "Измененный проект"
    try:
        response = update_project(project_id, new_project_title, token)

        print(f"Ответ от сервера на PUT-запрос: {response.status_code} - {response.text}")

        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

        project_details_response = get_project(project_id, token)

        print(
            f"Ответ от сервера на GET-запрос: {project_details_response.status_code} - {project_details_response.text}")

        project_details = project_details_response.json()
        assert project_details[
                   "title"] == new_project_title, f"Ожидалось, что имя проекта будет '{new_project_title}', но получено '{project_details['title']}'"

        print(f"Проект успешно изменен на: {project_details['title']}")

    except Exception as e:
        print(f"Ошибка при изменении проекта: {e}")


# Негативный тест для изменения проекта (с несуществующим ID)
def test_update_project_negative():
    new_project_title = "Измененный проект"
    try:
        response = update_project(invalid_project_id, new_project_title, token)

        print(f"Ответ от сервера: {response.status_code} - {response.text}")

        assert response.status_code == 404, f"Ожидался статус 404, но получен {response.status_code}"

        print(f"Проект с ID '{invalid_project_id}' не найден. Негативный тест прошел успешно.")

    except Exception as e:
        print(f"Ошибка при выполнении негативного теста: {e}")


# Основная функция
def main():
    print("Запуск позитивного теста:")
    test_update_project_positive()

    print("\nЗапуск негативного теста:")
    test_update_project_negative()


# Запуск основного процесса
if __name__ == "__main__":
    main()