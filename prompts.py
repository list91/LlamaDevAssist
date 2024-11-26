PROMPTS = {
    # Базовое объяснение кода - объясняет, что делает код
    "explain_code": """Пожалуйста, объясни простыми словами, что делает этот код:
<*^$YOURPROMPT$^*>""",

    # Проверка кода - анализирует код на наличие проблем и возможных улучшений
    "code_review": """Проанализируй этот код и укажи:
1. Потенциальные баги
2. Проблемы с производительностью
3. Проблемы с безопасностью
4. Улучшения стиля кода
5. Нарушения лучших практик

Код для проверки:
<*^$YOURPROMPT$^*>""",

    "result cmd command": """"
    I will provide you with text representing the output of a command executed in the console. Your task is to classify this text as follows: if it indicates successful execution of the command, return the number 1. If it indicates an error or failure, return the number 0. Please do not add any additional comments or explanations—just provide the number (1 or 0) in response. Note that the text to classify is enclosed between the markers '>&&63542764hsadnfhsksanjdH'. Here is the text for classification: [>&&63542764hsadnfhsksanjdH<*^$YOURPROMPT$^*>>&&63542764hsadnfhsksanjdH]
    """,

    # Генерация документации - создает документацию или комментарии
    "generate_docs": """Создай подробную документацию для этого кода, включая:
- Назначение функции/класса
- Параметры
- Возвращаемые значения
- Примеры использования
- Важные примечания

Код для документирования:
<*^$YOURPROMPT$^*>""",

    # Генерация модульных тестов - создает тестовые случаи
    "generate_tests": """Создай модульные тесты для следующего кода. Включи:
- Тесты стандартного поведения
- Граничные случаи
- Обработку ошибок
- Проверку входных данных

Код для тестирования:
<*^$YOURPROMPT$^*>""",

    # Исправление багов - помогает найти и исправить проблемы
    "fix_bug": """В этом коде есть баг. Помоги найти и исправить его:
1. Объясни, что не так
2. Предоставь исправленный код
3. Объясни, почему исправление работает

Код с багом:
<*^$YOURPROMPT$^*>""",

    # Оптимизация кода - предлагает улучшения производительности
    "optimize_code": """Проанализируй этот код на производительность и предложи оптимизации:
1. Найди узкие места в производительности
2. Предложи конкретные улучшения
3. Предоставь оптимизированную версию

Код для оптимизации:
<*^$YOURPROMPT$^*>""",

    # Дизайн API - помогает спроектировать REST API
    "design_api": """Спроектируй REST API эндпоинт для этого требования:
<*^$YOURPROMPT$^*>

Включи:
1. HTTP метод
2. Путь эндпоинта
3. Формат запроса/ответа
4. Коды состояния
5. Обработку ошибок""",

    # Оптимизация запросов к базе данных - помогает с SQL
    "optimize_query": """Оптимизируй этот запрос к базе данных:
<*^$YOURPROMPT$^*>

Учитывай:
1. Использование индексов
2. Структуру запроса
3. Влияние на производительность
4. Возможные альтернативы""",

    # Проверка безопасности - фокусируется на аспектах безопасности
    "security_review": """Выполни проверку безопасности этого кода:
<*^$YOURPROMPT$^*>

Проверь на:
1. Распространенные уязвимости
2. Валидацию входных данных
3. Проблемы с аутентификацией
4. Риски утечки данных
5. Лучшие практики безопасности""",

    # Рефакторинг кода - предлагает структурные улучшения
    "refactor_code": """Предложи как отрефакторить этот код для улучшения:
1. Читаемости
2. Поддерживаемости
3. Модульности
4. Использования паттернов проектирования

Код для рефакторинга:
<*^$YOURPROMPT$^*>""",

    # Обработка ошибок - улучшает обработку исключений
    "error_handling": """Улучши обработку ошибок в этом коде:
<*^$YOURPROMPT$^*>

Включи:
1. Конкретные исключения
2. Сообщения об ошибках
3. Стратегии восстановления
4. Предложения по логированию""",

    # Завершение кода - помогает дополнить частичный код
    "complete_code": """Заверши этот фрагмент кода, следуя тому же стилю и логике:
<*^$YOURPROMPT$^*>""",

    # Проектирование архитектуры - помогает с дизайном системы
    "design_architecture": """Спроектируй программную архитектуру для этого требования:
<*^$YOURPROMPT$^*>

Включи:
1. Компоненты
2. Взаимодействия
3. Поток данных
4. Технологии
5. Компромиссы""",
}

# Пример использования:
if __name__ == "__main__":
    # Импортируем функцию запроса к Ollama
    from main import query_ollama
    
    # Пример: Получаем объяснение кода
    code_to_explain = """
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    """
    
    prompt = PROMPTS["explain_code"].replace("<*^$YOURPROMPT$^*>", code_to_explain)
    response = query_ollama(prompt)
    print("Объяснение:", response)
