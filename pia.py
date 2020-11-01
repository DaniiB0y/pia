from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import webbrowser as web
import speech_recognition as sr
import pyttsx3
import string

def buscar():
    print("Ouvindo!")
    audio = r.listen(source)
    a = r.recognize_google(audio, language='pt-BR')
    a = a.lower()
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://duckduckgo.com/")
    print(driver.title)
    search = driver.find_element_by_name("q")
    search.send_keys(f"{a}")
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    main = driver.find_elements_by_class_name("result__url__domain")
    pt2 = driver.find_elements_by_class_name("result__url__full")
    link1 = main[0]
    link2 = pt2[0]
    driver.get(f"{link1.text}{link2.text}")

engine = pyttsx3.init()
engine.say("Olá, eu sou o Piá diga oque precisa,  chamando ei Piá!")
engine.runAndWait()
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo!")
        audio = r.listen(source)
        frase = r.recognize_google(audio, language='pt-BR')
        frase2 = frase.lower()
        print(frase2)
        if frase2 == "ei piá":
            buscar()
        else:
            engine.say("Mas bah tche, me chame! diga ei piá")
            engine.runAndWait()
    # Speech recognition using Google Speech Recognition
