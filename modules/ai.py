r"""
    ## Модуль для роботи з API штучного інтелекту(OpenAI)
    ### у цьому файли генерувати відповіді від ШІ 
"""
import openai
import dotenv, os

# завантажує змінні з файлу .env (файл для зберігання змінних віртуального середовища)
dotenv.load_dotenv()
OPENAI_SECRETKEY = os.getenv("OPENAI_SECRETKEY")

# ми асинхронно підключаємо chatgpt до коду і зберігаючи змінну (client_openai) використовуючи спеціальний ключ "OPENAI_SECRETKEY"
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRETKEY)

# створюємо асинхронну функцію для обміну даних із chatgpt
async def get_responce_from_ai(request: str):
    # надсилаємо запит до chatgpt а потім отримуємо відповідь
    response = await client_openai.chat.completions.create(
        model="gpt-4o-mini", # вказуємо модель chatgpt, яку будемо використовувати
        messages = [{
            "role": "user", # вказуємо те як буде бачити нас chatgpt "користувач"
            "content": request, #вказуємо текст, який ми відправимо chatgpt
        }]
    )
    # отримуємо та повертаємо текст написаний chatgpt
    return response.choices[0].message.content
        

