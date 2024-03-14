import os

prompt = input("Введите запрос: ")

if "." in prompt:
    os.system("nohup chromium --app="+prompt+">>/dev/null &")
elif prompt[:3] == "yt ":
    os.system("nohup chromium --app=https://youtube.com/results?search_query="+prompt[3:].replace(" ", "+")+">>/dev/null &")
elif prompt[:3] in ["tr ", "тр "]:
    if prompt[4].lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        os.system("nohup chromium --app=https://translate.yandex.ru/?source_lang=ru&target_lang=en&text="+prompt[3:].replace(" ", "+")+">>/dev/null &")
    else:
        os.system("nohup chromium --app=https://translate.yandex.ru/?source_lang=en&target_lang=ru&text="+prompt[3:].replace(" ", "+")+">>/dev/null &")

else:
    os.system("nohup chromium --app=https://google.com/search?q="+prompt.replace(" ", "+")+">>/dev/null &")
quit()

