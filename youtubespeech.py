from selenium import webdriver
import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Ask to Youtube for search :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You request  : {}".format(text))
    except:
        print("Sorry could not recognize what you said")
        
driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

search_box = driver.find_element_by_id('search')
search_box.send_keys(text)

search = driver.find_element_by_id('search-icon-legacy')
search.click()