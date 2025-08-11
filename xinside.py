import pandas as pd
import polars as pl
import io
import os
from openai import OpenAI

data_file_path = input("Введите путь к *.csv файлу с данными: ") # 'data/freelancer_earnings_bd.csv'

df_pandas = pd.read_csv(data_file_path)

df_decribe = io.StringIO()
df_pandas.info(buf=df_decribe)
info = df_decribe.getvalue()

api_key = os.getenv("XINSIDE_OPENROUTER_KEY")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

while True:
  query = input("Введите запрос к данным, либо quit для выхода: ")

  assert query.strip() != "", "Запрос не может быть пустым."
  if query == "quit":
     break

  prompt_polars = f"""У тебя есть следующее описание датафрейма Pandas с данными "{info}". 
  Датафрейм хранится в переменной `df`.
  Также у тебя есть следующий запрос пользователя на естественном языке:
  "{query}".

  Выведи запрос на SQL, который можно передать в метод `sql` библиотеки polars, чтобы получить ответ на запрос пользователя.
  Выведи ТОЛЬКО код на SQL, без каких-либо пояснений.""" 


  print("Отправка запроса к LLM...")

  completion = client.chat.completions.create(
    extra_headers={
    },
    extra_body={},
    model="qwen/qwen-2.5-coder-32b-instruct:free",
    messages=[
      {
        "role": "user",
        "content": prompt_polars
      }
    ],
    temperature=0.0,
  )



  df = pl.read_csv(data_file_path)

  sql_query = completion.choices[0].message.content.strip().strip('```sql').strip('```')
  print("Сгенерированный SQL запрос:")
  print(sql_query)

  try:
      output = pl.sql(sql_query).collect()
      print("Ответ на запрос:")
      print(output)
  except Exception as e:
      print(e)
      print(f"Ошибка! Попробуйте переформулировать вопрос.")