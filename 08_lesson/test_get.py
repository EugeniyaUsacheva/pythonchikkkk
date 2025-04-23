import requests

url = "https://ru.yougile.com/api-v2/projects"
token = "kmyp0O4SWpnY0ec3J+390o617naNk0cQ1Xf0+MrT23FfgwSFdEcBvrR653lAp9oH"
invalid_token = "invalid_token_for_testing"


# Функция для создания проекта
def create_project(title, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    project_data = {
        "title": title
    }

    response = requests.post(url, headers=headers, json=project_data)

    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(
            f"Ошибка создания проекта: {response.status_code}, {response.text}"
        )


# Позитивный тест для создания проекта
def test_create_project():
    project_title = "Мой проект"
    try:
        project = create_project(project_title, token)
        assert "id" in project, (
            "Ожидалось поле 'id' в ответе, но оно отсутствует"
        )
        print(f"Проект '{project_title}' создан успешно с ID: {project['id']}")
    except Exception as e:
        print(f"Ошибка при создании проекта: {e}")


# Негативный тест для создания проекта с неправильным токеном
def test_create_project_negative():
    project_title = "Мой проект"
    try:
        response = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {invalid_token}",
                "Content-Type": "application/json"
            },
            json={"title": project_title}
        )

        assert response.status_code != 201, (
            f"Ожидалось, что статус код не будет 201, но получен "
            f"{response.status_code}"
        )

        assert response.status_code in [401, 403], (
            f"Ожидался статус 401 или 403, но получен {response.status_code}"
        )
        print(
            f"Негативный тест прошел успешно. Получен статус код: "
            f"{response.status_code}"
        )

    except Exception as e:
        print(f"Ошибка в негативном тесте: {e}")


# Основная функция
def main():
    test_create_project()  # Позитивный тест
    test_create_project_negative()  # Негативный тест


# Запуск основного процесса
if __name__ == "__main__":
    main()
