# Аналитическая система извлечения данных с помощью естественного языка.

## Инструкция для установки и запуска
1. Зарегистрируйтесь на сайте https://openrouter.ai
2. Получите Api ключ для доступа к языковым моделям (или запросите его у автора  этой программы)
3. Инициализируйте Api ключ для работы с программой:

На Windows (PowerShell)
`$env:XINSIDE_OPENROUTER_KEY = "<OPENROUTER_API_KEY>"`

На Linux:
`export XINSIDE_OPENROUTER_KEY=<OPENROUTER_API_KEY>`

4. Установите окружение
```
python -m venv venv
source venv/bin/activate # На Windows: venv\Scripts\activate
pip install -r requirements.txt
``` 

Запустите программу, и задавайте вопросы по таблице с информацией о доходах фрилансеров:

`python xinside.py`