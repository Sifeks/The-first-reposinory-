import ctypes
import pyaudio
import pyautogui
import random
import datetime
import pygame
import pyjokes as pyjokes
import pyttsx3
import webbrowser
import os
import requests
import wikipedia as wikipedia
import credits
import time
import g4f
import json
import win32com.client as wincl
import re
from translate import Translator
import tkinter as tk
from threading import Thread
import keyboard
import mouse
import pywhatkit
import cv2
from vosk import Model, KaldiRecognizer
import speedtest
from fuzzywuzzy import fuzz



model = Model(r'C:\Program Files (x86)\vosk-model-small-ru-0.22')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate = 16000, input=True, frames_per_buffer=8000)
stream.start_stream()

isClicking = False

try:
    st = speedtest.Speedtest()
except AttributeError:
    print('Ошибка епта')
except speedtest.ConfigRetrievalError:
    print('Ошибка')



VA_CMD_LIST ={
        "ctime": ('текущее время','сейчас времени','который час','быстро сказал время'),
        "zaguglu": ('загугли','найди в гугле','окей гугл'),
        "anekdot": ('расскажи анекдот','рассмеши меня','ты знаешь анекдоты','расскажи шутку','пошути')
    }

activation_phrase = "джарвис"

def jarvis_say():
    def play_random_sound(folder_path):
        # Инициализируем Pygame
        pygame.init()

        # Получаем список файлов в указанной папке
        files = os.listdir(folder_path)

        # Фильтруем только файлы со звуками (поддерживаемые расширения)
        sound_files = [file for file in files if file.endswith((".mp3", ".wav"))]

        if sound_files:
            # Выбираем случайный звук из списка
            random_sound = random.choice(sound_files)

            # Строим путь к выбранному звуку
            sound_path = os.path.join(folder_path, random_sound)

            # Воспроизводим звук
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость

            while pygame.mixer.music.get_busy():
                continue  # Ждем, пока звук воспроизводится

            return

        else:
            print("Нет звуковых файлов в указанной папке.")

        # Выходим из Pygame
        pygame.quit()

    # Путь к папке со звуками
    folder_path = r"C:\Program Files (x86)\Фразы.Джарвис"
    play_random_sound(folder_path)

def proepta():
    def prochanie(folder_path):
        pygame.init()

        # Получаем список файлов в указанной папке
        files = os.listdir(folder_path)

        # Фильтруем только файлы со звуками (поддерживаемые расширения)
        sound_files = [file for file in files if file.endswith((".mp3", ".wav"))]

        if sound_files:
            # Выбираем случайный звук из списка
            random_sound = random.choice(sound_files)

            # Строим путь к выбранному звуку
            sound_path = os.path.join(folder_path, random_sound)

            # Воспроизводим звук
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость

            while pygame.mixer.music.get_busy():
                continue  # Ждем, пока звук воспроизводится

            return

        else:
            print("Нет звуковых файлов в указанной папке.")

        pygame.quit()

    folder_path = r"C:\Program Files (x86)\прощание"
    prochanie(folder_path)

def dobroe():
    def ytro(folder_path):
        pygame.init()

        # Получаем список файлов в указанной папке
        files = os.listdir(folder_path)

        # Фильтруем только файлы со звуками (поддерживаемые расширения)
        sound_files = [file for file in files if file.endswith((".mp3", ".wav"))]

        if sound_files:
            # Выбираем случайный звук из списка
            random_sound = random.choice(sound_files)

            # Строим путь к выбранному звуку
            sound_path = os.path.join(folder_path, random_sound)

            # Воспроизводим звук
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость

            while pygame.mixer.music.get_busy():
                continue  # Ждем, пока звук воспроизводится

            return

        else:
            print("Нет звуковых файлов в указанной папке.")

        pygame.quit()

    folder_path = r"C:\Program Files (x86)\Доброе утро"
    ytro(folder_path)



def check_activation_phrase(text, cut=0):
    ratio = fuzz.ratio(text.lower(), VA_CMD_LIST)
    if ratio >= 70:
        cut += 1
        return True
    else:
        return False

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.setProperty('rate', 150)
    engine.runAndWait()


def translate_text(text, source_lang, target_lang):
    translator = Translator(to_lang=target_lang, from_lang=source_lang)
    translation = translator.translate(text)
    return translation


def open_monetka():
    monetkas = random.randint(1,2)
    if monetkas == 1:
        speak('Орёл')
        print('Орёл')
    else:
        speak('Решка')
        print('Решка')
    return monetkas

def open_steam():
    path_to_steam = "C:\\Program Files (x86)\\Steam\\steam.exe"
    os.startfile(path_to_steam)

def open_zoom():
    path_to_zoom = r'C:\Users\ivane\AppData\Roaming\Zoom\bin\Zoom.exe'
    os.startfile(path_to_zoom)

def start_timer(seconds):
    print("Есть, сэр.")
    speak('Таймер установлен,сэр')
    time.sleep(seconds)
    print("ДЗЫЫЫЫНЬ!!! Время прошло.")
    speak("ДЗЫЫЫЫНЬ!!! Время прошло.")

def open_youtube():
    url = "https://www.youtube.com/"
    webbrowser.open(url)

def increase_volume_by(amount):
    current_volume = get_current_volume()
    new_volume = current_volume + amount
    set_volume(new_volume)
    speak(f"Сэр, я повысил громкость на {amount}")

def get_current_volume():
    result = os.popen("nircmd.exe changesysvolume 0").read()
    match = re.search(r"\d+", result)
    if match:
        return int(match.group())
    return 0

def set_volume(volume):
    os.system(f"nircmd.exe setsysvolume {volume}")

def atmoshper_zvyki():
    zzvyki = r"C:\Users\ivane\OneDrive\Рабочий стол\Атмосферные.звуки"
    sound_files = os.listdir(zzvyki)
    random_zzvuki = random.choice(sound_files)
    os.system(f"start {os.path.join(zzvyki, random_zzvuki)}")
    pyautogui.getActiveWindow().minimize()

def wiki(query):
    wikipedia.set_lang("ru")
    try:
        page = wikipedia.page(query)
        summary = wikipedia.summary(query,sentences=3)
        speak(f'**{summary}**\n\n\nRead more: {page.url}')
        print(f'**{summary}**\n\n\nRead more: {page.url}')
    except wikipedia.exceptions.PageError:
        speak('Страница не найдена')
        print('Страница не найдена')
    except wikipedia.exceptions.DisambiguationError as e:
        speak(f'Уточните ваш запрос: {e.options}')
        print(f'Уточните ваш запрос: {e.options}')

def get_weather(city, WEATHER_KEY = '93794f148ba34e3a0692df62930d38c8'):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    resp = requests.get(base_url, params={
        'q': city,
        'appid': WEATHER_KEY,
        'units': 'metric',
        'lang': 'ru'
    })

    temp = resp.json()
    return temp


def detect_face():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    start_time = time.time()
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, 'OK', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) == ord('q') or time.time() - start_time > 30:
            break

    cap.release()
    cv2.destroyAllWindows()

def listen():
    while True:
        datas = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(datas)) and (len(datas) > 0):
            otvet = json.loads(rec.Result())
            if otvet['text']:
                yield otvet['text']


def mozgi():
    prosto = " ".join(list(listen.split(" ")[2::]))
    print(prosto)
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prosto}],
    )
    print(response)
    speak(response)

def calc():
    try:
        list_of_nums = listen().split()
        num_1, num_2 = int((list_of_nums[-3]).strip()), int((list_of_nums[-1]).strip())
        opers = [list_of_nums[0].strip(), list_of_nums[-2].strip()]
        for i in opers:
            if 'дел' in i or 'множ' in i or 'лож' in i or 'приба' in i or 'выч' in i or i == 'x' or i == '/' or i == '+' or i == '-' or i == '*':
                oper = i
                break
            else:
                oper = opers[1]
            if oper == "+" or 'слож' in oper:
                ans = num_1 + num_2
            elif oper == "-" or 'выче' in oper:
                ans = num_1 - num_2
            elif oper == "х" or 'множ' in oper:
                ans = num_1 * num_2
            elif oper == "/" or 'дел' in oper:
                if num_2 != 0:
                    ans = num_1 / num_2
                else:
                    speak("Делить на ноль невозможно")
            elif "степен" in oper:
                ans = num_1 ** num_2
            speak("{0} {1} {2} = {3}".format(list_of_nums[-3], list_of_nums[-2], list_of_nums[-1], ans))
    except:
        speak("Скажите, например: Сколько будет 5+5?")

def weather_handler():
    pogoda = listen().split()
    data = get_weather(str(pogoda))
    weather_description = data['weather'][0]['description']
    temperature_feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    msg = f"В настоящий момент {weather_description}\n" \
          f"Температура ощущается, как {temperature_feels_like}\n" \
          f"Влажность {humidity}%"
    print(msg)
    speak(msg)

def check_command(text):
    for command, description in text.items():
        if fuzz.ratio(text.lower(), command.lower()) >= 70:
            return description
    return "Неизвестная команда"

def sifeks():
    global time
    dobroe()
    for text in listen():
        print(text)
        command = text
        if "открой discord" in command or 'открой дискомфорт' in command or 'открой диск орт' in command or 'открой эскорт' in command:
            jarvis_say()
            webbrowser.open("https://discord.com/channels/1101886770397855855/1101886770850844735")
        elif 'открой steam' in command.lower() or 'открой с ним' in command or 'открой с тим' in command or 'открой стин' in command or 'открой с тем' in command:
            print('Открываю Steam')
            jarvis_say()
            open_steam()

        elif 'закрой steam' in command or 'закрой с тем' in command or 'закрой с ним' in command or 'закрой ским' in command:
            os.system("taskkill /im steam.exe /f")
            print('Steam успешно закрыт')
            jarvis_say()

        elif 'сколько время' in command or 'текущее время' in command or 'который час' in command:
            now = datetime.datetime.now()
            time = "Сейчас " + now.strftime("%H:%M")
            speak(time)
        elif 'открой youtube' in command.lower() or 'открой эту' in command or 'открой ютуб' in command:
            print('Открываю ютуб')
            jarvis_say()
            open_youtube()

        elif "закрой браузер" in command:
            os.system("taskkill /im browser.exe /f")
            jarvis_say()
            print('Закрываю браузер')

        elif 'как дела' in command.lower():
            print('Все отлично,сэр')
            speak('Все отлично,сэр')

        elif 'есть проблемы' in command.lower():
            print('Никак нет,сэр')
            speak('Никак нет,сэр')

        elif 'открой вставлял ку' in command.lower():
            webbrowser.open('https://pastebin.com/')
            print('Открываю pastebin')
            jarvis_say()

        elif 'монетка' in command:
            open_monetka()

        elif 'дай викторину' in command or 'да викторина' in command or 'да викторину' in command:
            count = 0
            questions = [
                {"question": "Какая столица Франции?", "answer": "Париж"},
                {"question": "Сколько планет в Солнечной системе?", "answer": "Восемь"},
                {"question": "Как называется самая большая пустыня в мире?", "answer": "Сахара"},
                {"question": "Кто написал роман 'Преступление и наказание'?", "answer": "Фёдор Достоевский"},
                {"question": "Как называется самое высокое горное образование на Земле?", "answer": "Эверест"},
            ]
            for i, question in enumerate(questions, start=1):
                print(f"Вопрос {i}: {question['question']}")
                speak(f"Вопрос {i}: {question['question']}")

                start_time = time.time()
                users_answer = listen()
                end_time = time.time()

                if end_time - start_time > 10:  # Проверяем, прошло ли 10 секунд
                    print("Время истекло!")
                    speak(["answer"])


                if users_answer.lower() == question["answer"].lower():
                    count += 1


            print(f"Вы ответили правильно на {count} из {len(questions)} вопросов.")
            speak(f"Вы ответили правильно на {count} из {len(questions)} вопросов.")


        elif 'расскажи шутку' in command or 'расскажи анекдот' in command:
            try:
                source_text = pyjokes.get_joke()
                target_text = translate_text(source_text, "en", "ru")
                print(target_text)
                speak(target_text)
            except requests.exceptions.ConnectionError:
                print('У вас нету интернета,сэр')
                speak('У вас нету интернета,сэр')



        elif 'спишь' in command:
            speak('Никак нет.Всегда готов к вашим услугам,сэр')
            print('Никак нет.Всегда готов к вашим услугам,сэр')

        elif 'открой google' in command or 'открой гугл' in command or 'открой гуго' in command:
            webbrowser.open('https://www.google.ru/')
            jarvis_say()
            print('Открываю гугл,сэр')

        elif 'открой чат гпт' in command:
            webbrowser.open('https://discord.com/channels/1101886770397855855/1101886839255736330')
            jarvis_say()
            print('Открываю чат гпт,сэр')

        elif 'спасибо' in command:
            speak("Не за что,сэр.Всегда готов к вашим услугам,сэр")
            print("Не за что,сэр.Всегда готов к вашим услугам,сэр")

        elif 'открой конференцию' in command or 'открой zoom' in command or 'открой зум' in command:
            jarvis_say()
            open_zoom()

        elif 'закрой конференцию' in command or 'закрой zoom' in command or 'закрой зум' in command:
            jarvis_say()
            os.system("taskkill /im zoom.exe /f")
            print('Zoom успешно закрыт')

        elif 'открой урок epica' in command:
            webbrowser.open('https://epic.whereby.com/182')
            jarvis_say()
            print('Удачного обучения,сэр')

        elif 'открой epic' in command:
            webbrowser.open('https://epic-school.ru/')
            jarvis_say()
            print('Эпик открыт')

        elif 'сделай погромче' in command or 'громче сделай' in command:
            pyautogui.press("volumeup")
            jarvis_say()
            print('Громче сделано,сэр')

        elif 'сделай потише' in command or 'тише сделай' in command:
            pyautogui.press("volumedown")
            jarvis_say()
            print('Тише сделано,сэр')

        elif 'выключи звук' in command or 'мут звука' in command:
            pyautogui.press("volumemute")
            print('Звук успешно выключен')
            jarvis_say()

        elif 'курсор влево' in command:
            print("Будет сделано,сэр")
            jarvis_say()
            pyautogui.dragTo(300, 300, duration=4)
            print('Работа сделана,сэр')

        elif "узнай размер окна" in command:
            print('Будет сделано,сэр')
            jarvis_say()
            size = pyautogui.size()
            print("Готово сэр", size)
            speak(size)

        elif 'скопируй' in command:
            pyautogui.hotkey('ctrl','c')
            jarvis_say()
            print('Скопировано,сэр')

        elif 'сделай скриншот' in command:
            pyautogui.press('PrtSc')
            jarvis_say()
            print('Сделано,сэр')

        elif 'увеличь окно' in command:
            print("Есть,сэр")
            jarvis_say()
            pyautogui.getActiveWindow().maximize()
            print('Сделано,сэр')

        elif 'сверни окно' in command:
            print("Вы сказали свернуть окно \n сейчас ваше окно свернется")
            jarvis_say()
            pyautogui.getActiveWindow().minimize()
            print('Окно свернуто,сэр')


        elif 'закрой приложение' in command:
            jarvis_say()
            print('Секунду,сэр')
            pyautogui.hotkey('alt','fn','f4')
            print('Готово,сэр')


        elif 'включи атмосферный звук' in command:
            print('Секунду,сэр')
            jarvis_say()
            atmoshper_zvyki()

        elif command.lower().startswith("википедия"):
            jarvis_say()
            print('Без проблем,сэр')
            wikipedia.set_lang("ru")
            try:
                page = wikipedia.page(command)
                summary = wikipedia.summary(command, sentences=5)
                print(f'**{summary}**\n\n\nRead more: {page.url}')
                speak(f'**{summary}**\n\n\n')
            except wikipedia.exceptions.PageError:
                speak('Страница не найдена')
                print('Страница не найдена')
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f'Уточните ваш запрос: {e.options}')
                print(f'Уточните ваш запрос: {e.options}')
            except requests.exceptions.ConnectionError:
                print('Нету интернета')
                speak('У вас отсутствует интернет,сэр')

        elif 'найди видео' in command or 'найди на youtube' in command or 'найди на ютуби' in command or 'найди на ютубе' in command:
            jarvis_say()
            print('Секунду,сэр')
            search_query = command.replace("найди видео" or 'найди на youtube' or 'найди на ютуби' or 'найди на ютубе', "").strip()
            webbrowser.open("https://www.youtube.com/results?search_query=" + search_query)
            print("Открываю " + search_query + " на YouTube")

        elif 'загугли' in command or 'за гугле' in command:
            jarvis_say()
            print('Делаю,сэр')
            search_google = command.replace('за гугле', '').strip()
            webbrowser.open('https://www.google.ru/search?q=' + search_google)
            print("Загуглил" + search_google)


        elif 'переводчик' in command:
            speak('Пару секунд,сэр')
            print('Пару секунд,сэр')
            try:
                source_text =  " ".join(list(command.split(" ")[1::]))
                target_text = translate_text(source_text, "ru", "en")
                print(target_text)
                speak(target_text)
            except requests.exceptions.ConnectionError:
                print('У вас нету интернета,сэр')
                speak('У вас нету интернета,сэр')

        elif 'калькулятор' in command:
            calc()

        elif 'включи мозги' in command or 'расскажи мне ' in command or 'что такое' in command:
            jarvis_say()
            try:
                if 'включи мозги' in command:
                    prosto = " ".join(list(command.split(" ")[2::]))
                    print(prosto)
                    response = g4f.ChatCompletion.create(
                        model=g4f.models.gpt_4,
                        messages=[{"role": "user", "content": prosto}],
                    )
                    print(response)
                    speak(response)
                else:
                    prostos = " ".join(list(command.split(" ")[2::]))
                    responses = g4f.ChatCompletion.create(
                        model=g4f.models.gpt_4,
                        messages=[{"role": "user", "content": prostos}],
                    )
                    print(responses)
                    speak(responses)

            except RuntimeError:
                from g4f import RetryProvider
                print('У вас проблемы с интернетом, сэр')
                speak('У вас проблемы с интернетом, сэр')




        elif 'повысить громкость на' in command:
            amount = int(re.search(r'\d+', command).group())
            increase_volume_by(amount)

        elif 'понизить громкость на' in command:
            tixost = command.split('понизить громкость на', 1)[1].strip()
            speak('Понижаю громкость на ' + tixost)
            for i in range(tixost):
                pyautogui.press("volumedown")

        elif 'закрой вкладку' in command:
            pyautogui.hotkey('ctrl', 'f4')
            print('Вкладка закрыта,сэр')
            jarvis_say()

        elif 'закрой все вкладки' in command or 'закрой все вкладке' in command or 'закрой вклад' in command:
            pyautogui.hotkey('ctrl', 'shift', 'w')
            print('Все вкладки закрыты,сэр')
            jarvis_say()

        elif 'верни вкладку' in command or 'вернее вкладку' in command or 'верни вкладка' in command:
            pyautogui.hotkey('ctrl', 'shift', 'T')
            print('Не за что,сэр')
            jarvis_say()

        elif 'создай вкладку' in command:
            pyautogui.hotkey('ctrl', 't')
            print('Всегда к вашим услугам,сэр')
            jarvis_say()

        elif 'погода' in command:
            weather_handler()

        elif 'xbox game bar' in command or 'икс бокс гейм бар' in command:
            pyautogui.hotkey('win', 'g')
            print('Готово,сэр')
            jarvis_say()

        elif 'открой диспетчер задач' in command:
            pyautogui.hotkey('ctrl', 'shift', 'esc')
            print('Диспетчер задач открыт,сэр')
            jarvis_say()

        elif 'открой minecraft' in command or 'открой майнкрафт' in command:
            path_to_minecraft = r"C:\Users\ivane\AppData\Roaming\.minecraft\TLauncher.exe"
            os.startfile(path_to_minecraft)
            jarvis_say()
            print('Minecraft запущен,сэр')

        elif 'закрой minecraft' in command or 'закрой майнкрафт' in command:
            os.system("taskkill /im TLauncher.exe/f")
            jarvis_say()
            print('Minecraft закрыт,сэр')

        elif 'открой альтернативу steam' in command or 'открой альтернативу с ним' in command:
            path_to_epic_games = "https://store.epicgames.com/ru/"
            os.startfile(path_to_epic_games)
            print('Epic games открыт')
            jarvis_say()

        elif 'закрой альтернативу steam' in command or 'закрой альтернативу с ним' in command:
            os.system("taskkill /im https://store.epicgames.com/ru/")
            jarvis_say()
            print('EpicGames закрыт,сэр')

        elif 'таймер' in command:
            try:
                seconds = int(command.split(" ")[1])
                start_timer(seconds)
            except (IndexError, ValueError):
                print("Некорректное время")
                speak('Некорректное время')

        elif "где на карте" in command:
            karta_nahoy = command.replace("где на карте", "")
            location = karta_nahoy
            jarvis_say()
            webbrowser.open("https://www.google.ru/maps/search/" + location + "")

        elif 'заблокируй windows' in command or 'заблокируй виндоус' in command:
            print("Блокирую,сэр")
            jarvis_say()
            ctypes.windll.user32.LockWorkStation()

        elif "войди в сон" in command or "не слушай" in command:
            print("Скажите,на сколько вы хотите,чтобы я ушел в сон,только число в секундах")
            speak("Скажите,на сколько вы хотите,чтобы я ушел в сон,только число в секундах")
            a = int(command)
            time.sleep(a)
            print(a)

        elif 'отчисть историю браузера' in command or 'чистка истории браузера' in command:
            pyautogui.hotkey('ctrl', 'h')
            print('Готово,сэр')
            jarvis_say()

        elif 'открой окно загрузок' in command or 'окно загрузок' in command:
            pyautogui.hotkey('ctrl', 'j')
            print('Окно загрузок открыто,сэр')
            jarvis_say()

        elif 'открой командную строку' in command:
            jarvis_say()
            comand_stroka = r'C:\Users\ivane\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk'
            os.startfile(comand_stroka)
            print('Командная строка открыта,сэр')


        elif 'пауза' in command:
            jarvis_say()
            pyautogui.press('space')
            print('Пауза поставлена')

        elif 'автокликер' in command or 'поставь автокликер' in command or 'включи авто клинкер' in command:
            def toggle_autoclick():
                global isClicking
                if isClicking:
                    isClicking = False
                    status_label.config(text='Автокликер выключился')
                else:
                    isClicking = True
                    autoclick_thread = Thread(target=autoclick)
                    autoclick_thread.start()

            def autoclick():
                while isClicking:
                    mouse.double_click(button='right')
                    time.sleep(0.01)

            def stop_autoclick(event):
                global isClicking
                if event.name == 'q' and isClicking:
                    isClicking = False
                    status_label.config(text='Автокликер выключился')

            root = tk.Tk()
            root.title('Автокликер', )
            root.geometry('300x300')

            status_label = tk.Label(root, text='Нажми q чтобы выключить автокликер')
            status_label.pack(pady=10)

            toggle_button = tk.Button(root, text='Нажми эту кнопку чтобы включить автокликер', command=toggle_autoclick)
            toggle_button.pack(pady=10)

            keyboard.on_press_key('q' or 'й', stop_autoclick)

            root.mainloop()

        if 'проиграй музыку' in command:
            jarvis_say()
            song = command.replace("проиграй музыку", "").strip()
            pywhatkit.playonyt(song)
            pyautogui.getActiveWindow().minimize()

        if 'проверка на лицо' in command:
            jarvis_say()
            print('Готово,сэр. Нажмите q чтобы отключить')
            detect_face()

        if 'проверка скорости скачивания' in command or 'проверка скорость скачивания' in command:
            print('Секунду,сэр')
            jarvis_say()
            skorost_skachki = st.download()
            print(st.download())
            speak(skorost_skachki)

        if 'проверка скорости загрузки' in command or 'проверка скорость загрузки' in command:
            print('Проверяю,сэр')
            jarvis_say()
            skorost_zagruzki = st.upload()
            print(st.upload())
            speak(skorost_zagruzki)

        if 'проверка пинга' in command or 'проверка кинга' in command or 'проверка пинка' in command:
            servernames = []
            st.get_servers(servernames)
            print('Хорошо,сэр')
            jarvis_say()
            skorost_pinga = st.results.ping
            print(st.results.ping)
            speak(skorost_pinga)

        if 'спавн' in command or 'спаун' in command:
            jarvis_say()
            pyautogui.hotkey('t','/','s','p','a','w','n','enter')

        if 'приколы хакера' in command or 'приколы хакеры' in command:
            jarvis_say()
            comand_stroka = r'C:\Users\ivane\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk'
            os.startfile(comand_stroka)
            time.sleep(1)
            pyautogui.hotkey('c','o','l','o','r','space','2','enter')
            pyautogui.hotkey('d','i','r','/','s','enter')

        if 'следующая вкладка' in command or 'следующее вкладка' in command:
            jarvis_say()
            pyautogui.hotkey('Ctrl','Tab')
            print('Следующая вкладка открыта,сэр')

        if 'предыдущая вкладка' in command:
            jarvis_say()
            pyautogui.hotkey('Ctrl', 'Shift', 'Tab')
            print('Предыдущая вкладка открыта,сэр')

        if 'открой проводник' in command:
            jarvis_say()
            pyautogui.hotkey('Win', 'e')
            print('Проводник открыт')

        if 'смени раскладку' in command or 'поменяй язык' in command:
            jarvis_say()
            pyautogui.hotkey('ctrl', 'shift')
            print('Раскладка сменена')

        if 'протокол выключение' in command:
            jarvis_say()
            os.system('shutdown -s')

        if 'запусти террарию' in command or 'запусти террариум' in command or 'запусти плоский майнкрафт' in command:
            jarvis_say()
            os.startfile(r'C:\Users\ivane\OneDrive\Рабочий стол\Terraria.url')

        if "отключись" in command:
            proepta()
            break

sifeks()








