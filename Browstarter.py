import os

prompt = input("Введите запрос: ")

if "." in prompt:
    os.system("ungoogled-chromium --kiosk --new-window \""+prompt+"\"")
elif prompt[:3] == "yt ":
    os.system("ungoogled-chromium --kiosk --new-window \"https://youtube.com/results?search_query="+prompt[3:].replace(" ", "+")+"\"")
elif prompt[:3] in ["tr ", "тр "]:
    if prompt[4].lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        os.system("chromium --kiosk --new-window \"https://translate.yandex.ru/?source_lang=ru&target_lang=en&text="+prompt[3:].replace(" ", "+")+"\"")
    else:
        os.system("chromium --kiosk --new-window \"https://translate.yandex.ru/?source_lang=en&target_lang=ru&text="+prompt[3:].replace(" ", "+")+"\"")

else:
    os.system("ungoogled-chromium --kiosk --new-window \"https://google.com/search?q="+prompt.replace(" ", "+")+"\"")
quit()

