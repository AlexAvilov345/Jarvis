import speech_recognition as sr
import subprocess
import webbrowser
import threading
import customtkinter as ctk

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  

class JarvisApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Джарвис 2.0")
        self.geometry("450x550")
        self.resizable(False, False)

        self.recognizer = sr.Recognizer()

        self.chat_box = ctk.CTkTextbox(self, width=410, height=420, font=("Arial", 14), wrap="word")
        self.chat_box.pack(pady=20, padx=20)
        self.chat_box.configure(state="disabled")  

        self.listen_btn = ctk.CTkButton(
            self, 
            text="Сказать команду", 
            font=("Arial", 16, "bold"),
            height=50,
            width=250,
            command=self.start_listening_thread
        )
        self.listen_btn.pack(pady=10)

        self.add_message("Джарвис", "Система готова к работе, сэр. Нажмите кнопку и говорите.")

    def add_message(self, sender, text):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", f"{sender}: {text}\n\n")
        self.chat_box.see("end") 
        self.chat_box.configure(state="disabled")

    def start_listening_thread(self):
        self.listen_btn.configure(state="disabled", text="Слушаю...")
        thread = threading.Thread(target=self.process_voice, daemon=True)
        thread.start()

    def process_voice(self):
        text = self.listen_command()
        
        if text:
            self.add_message("Вы", text)
            self.execute_command(text)
        
        self.listen_btn.configure(state="normal", text="Сказать команду")

    def listen_command(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:

                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio, language="ru-RU")
                return command.lower()
            except sr.WaitTimeoutError:
                self.add_message("Система", "Вы ничего не сказали.")
                return ""
            except sr.UnknownValueError:
                self.add_message("Джарвис", "Не удалось распознать команду, сэр.")
                return ""
            except sr.RequestError:
                self.add_message("Джарвис", "Сэр, ошибка сервиса распознавания речи.")
                return ""

    def execute_command(self, text):
        if "джарвис папка" in text or "папки" in text:
            self.add_message("Джарвис", "Открываю Проводник...")
            subprocess.Popen("explorer")
            
        elif "джарвис гугл" in text or "джарвис google" in text:
            self.add_message("Джарвис", "Открываю браузер...")
            webbrowser.open("https://www.google.com")
            
        elif "джарвис гитхаб" in text or "джарвис github" in text:
            self.add_message("Джарвис", "Открываю GitHub...")
            webbrowser.open("https://github.com/")
            
        elif "джарвис ютуб" in text or "джарвис youtube" in text:
            self.add_message("Джарвис", "Открываю YouTube...")
            webbrowser.open("https://www.youtube.com/")
            
        elif "джарвис выход" in text or "джарвис стоп" in text:
            self.add_message("Джарвис", "Завершаю работу. До свидания, сэр.")
            self.after(1500, self.destroy) 
            
        else:
            self.add_message("Джарвис", "Команда не распознана.")

if __name__ == "__main__":
    app = JarvisApp()
    app.mainloop()
