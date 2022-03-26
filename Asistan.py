from cProfile import run
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import date, datetime
import random
from random import choice
import webbrowser
import psutil
from plyer import notification
import time
import pywhatkit as k


r = sr.Recognizer()

def record(ask=False):
    playsound(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\Asistan\\DING.mp3")
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım")
        except sr.RequestError:
            speak("Sistem çalışmıyor")
        return voice


def response(voice):
    if "merhaba" in voice:
        speak("sana da merhaba dostum")
    if "naber" in voice:
        speak("iyi senden naber")
    if "beni duyuyor musun" in voice:
        speak("Evet duyuyorum")
    if "teşekkür ederim" in voice or "teşekkürler" in voice:
        speak("rica ederim")
    if "görüşürüz" in voice or "bay bay" in voice or "kapan" in voice or "baybay" in voice:
        speak("görüşürüz dostum!")
        exit()

    if "hangi gündeyiz" in voice or "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)

    if "saat kaç" in voice:
        clock = datetime.now().strftime("%H:%M")
        speak(clock)

    if "pil" in voice:
        pil = psutil.sensors_battery()
        yuzde = pil.percent
        speak(f"Kalan pil: yüzde{yuzde}")

    if "bilgisayarı yeniden başlat" in voice or "bilgisayar yeniden başlat" in voice or "pc reset" in voice:
        speak("Bilgisayarı yeniden başlatma mı ister misin?")
        onay = record()
        onay = onay.lower()
        if "evet" in onay:
            speak("Sistem yeniden başlatılıyor")
            os.system("shutdown /r /t 2")
            exit()
        if "hayır" in onay:
            speak("İşlem iptal edildi")

    if "google" in voice:
        speak("Googleda ne aramamı istersin?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İşte google sonuçları")

    if "github" in voice:
        speak("Githubda ne aramamı istersin?")
        search = record()
        url = "https://github.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("İşte github sonuçları.")

    if "uygulama aç" in voice:
        speak("Hangi uygulamayı açmamı istiyorsun?")
        runApp = record()
        runApp = runApp.lower()
        if "discord" in runApp:
            os.startfile(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\helpers\\Discord.lnk")
            speak("Discordu açtım.")
            exit()
        elif "vsc" in runApp:
            os.startfile(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\Yazilim\\Visual Studio Code.lnk")
            speak("Visual Studio Code'yi açtım.")
            exit()
        else:
            speak("İstediğin uygulama çalıştırma listemde yok.")

    if "mesaj yolla" in voice or "mesaj gönder" in voice:
        speak("Kime mesaj yollamak istiyorsunuz?")
        webbrowser.get().open("https://web.whatsapp.com/")
        user = record()
        user = user.lower()
        if "anne" in user:
            speak("Ne mesaj yollamak istiyorsunuz?")
            mesaj = record()
            if mesaj:
                speak(f"Annenize {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1234567890",mesaj)
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
        
        elif "baba" in user:
            speak("Ne mesaj yollamak istiyorsunuz?")
            mesaj = record()
            if mesaj:
                speak(f"Babanıza {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1234567890",mesaj)
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
        
        elif "arkadaş" in user:
            speak("Ne mesaj yollamak istiyorsunuz?")
            mesaj = record()
            if mesaj:
                speak(f"Arkadaşınıza {mesaj} mesajını yollamak istiyor musunuz?")
                onay = record()
                onay = onay.lower()
                if "evet" in onay:
                    k.sendwhatmsg("+90 1234567890",mesaj)
                    speak("Mesaj gönderildi.")
                if "hayır" in onay:
                    speak("İşlem iptal edildi.")
    if "müzik aç" in voice:
        music = os.listdir(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\music")
        music = random.choice(music)
        os.startfile(rf"C:\\Users\\PC\\OneDrive\\Masaüstü\\music\\{music}")
        speak("Senin için bir müzik açtım.")

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(r"C:\\Users\\PC\\OneDrive\\Masaüstü\\Asistan\\answer.mp3")
    os.remove(file)

def test(wake):
    wake = record()
    if wake != '':
        voice = wake.lower()
        response(voice)

while True:
    wake = record()
    if wake != '':
        wake = wake.lower()
        print(wake)
        response(wake)