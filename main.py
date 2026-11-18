import speech_recognition as sr
import subprocess
import webbrowser

recognizer = sr.Recognizer()

def listen_command():
    with sr.Microphone() as source:
        print("Слушаю команду...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Вы сказали: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Не удалось распознать команду.")
        return ""
    except sr.RequestError:
        print("Сер, ошибка сервиса распознавания речи.")
        return ""

while True:
    text = listen_command()

    if "джарвис папка" in text or "папки" in text:
        print("Открываю Проводник...")
        subprocess.Popen("explorer")
    elif "джарвис гугл" in text or "интернет" in text:
        print("Открываю браузер...")
        webbrowser.open("https://www.google.com")
    elif "джарвис гитхаб" in text or "github" in text:
        print("Открываю GitHub...")
        webbrowser.open("https://github.com/")
    elif "джарвис ютуб" in text or "youtube" in text:
        print("Открываю YouTube...")
        webbrowser.open("https://www.youtube.com/")

    

    elif "джарвис выход" in text or "джарвис стоп" in text:
        print("Завершаю работу.")
        break