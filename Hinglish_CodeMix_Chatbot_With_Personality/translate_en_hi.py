import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googletrans import Translator

def filereader(filename):
    file_object = open(filename,"r")
    file_content = file_object.read()
    file_output = open("output.txt","w", encoding='utf-8')
    file_output_transliterated = open("output_transliterated.txt","w",encoding='utf-8')
    #lol = file_content.replace("\n\n","\n")
    # Removes the texts in brackets because they are just representing situation
    lol = re.sub(' \[.*\]',"",file_content)
    lol = re.sub('Michel','Michael',lol)
    lol = re.sub('Michael:','Michael@',lol)
    lol = re.sub('\n.*:','\nVarun:',lol)
    lol = re.sub('Michael@','Michael:',lol)
    length = 0
    '''translator = Translator()
    for scripts in lol.split("\n\n"):
        for dialogue in scripts.split('\n'):
            length = length + len(dialogue)
            if (length >= 3900):
                length = 0
                translator = Translator()
            translation = translator.translate(dialogue, src='en', dest='hi')
            file_output.write(translation.text)
            file_output.write('\n')
        file_output.write('\n')'''
    driver = webdriver.Chrome(executable_path="C:\\Users\\vlalw\\Documents\\chromedriver\\chromedriver_chatbot\\chromedriver.exe")
    driver.get("https://www.google.ca/search?dcr=0&sxsrf=ACYBGNSwCHesxbh4Zrot7gN7881aZfxtPw%3A1572890265123&ei=mWbAXayZB83n5gK7mrLoCA&q=english+to+hindi+translator&oq=english+to+hindi+translator&gs_l=psy-ab.3..0i71l8.0.0..594809...0.4..0.0.0.......0......gws-wiz.Yg3_zU0IXzw&ved=0ahUKEwjsyZfskNHlAhXNs1kKHTuNDI0Q4dUDCAs&uact=5")
    try:
        for scripts in lol.split("\n\n"):
            if (len(scripts) >= 3900):
                for dialogue in scripts.split('\n'):
                    english_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='tw-ta tw-text-large goog-textarea']")))
                    english_input = driver.find_element_by_xpath("//textarea[@class='tw-ta tw-text-large goog-textarea']")
                    english_input.clear()
                    english_input.send_keys(dialogue)
                    time.sleep(0.5)
                    hindi_output = driver.find_element_by_xpath("//pre[@class='tw-data-text tw-text-large tw-ta']/span")
                    file_output.write(hindi_output.text)
                    file_output.write('\n')
                    hiden_output = driver.find_element_by_xpath("//pre[@class='tw-data-text tw-text-small tw-ta']/span")
                    file_output_transliterated.write(hiden_output.text)
                    file_output_transliterated.write('\n')
            else:
                english_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='tw-ta tw-text-large goog-textarea']")))
                english_input = driver.find_element_by_xpath("//textarea[@class='tw-ta tw-text-large goog-textarea']")
                english_input.clear()
                english_input.send_keys(scripts)
                time.sleep(1)
                hindi_output = driver.find_element_by_xpath("//pre[@class='tw-data-text tw-text-large tw-ta']/span")
                file_output.write(hindi_output.text)
                file_output.write('\n')
                hiden_output = driver.find_element_by_xpath("//pre[@class='tw-data-text tw-text-small tw-ta']/span")
                file_output_transliterated.write(hiden_output.text)
                file_output_transliterated.write('\n')
            file_output.write('\n')
            file_output_transliterated.write('\n')
    finally:
        driver.close()
    #file_output.close()
    file_object.close()
    print("here")
    '''Pam: Well. I don't know.
    Michael: If you think she's cute now, you should have seen her a couple of years ago. [growls]
    Aman: What?'''
    #################################
    # Practicing Translator
    #translator = Translator()
    #translation = translator.translate("My name is Varun", src='en', dest='hi')
    #file_output.write(translation.text)

    #################################
    # Practicing Selenium
    #driver = webdriver.Chrome(executable_path="C:\\Users\\vlalw\\Documents\\chromedriver\\chromedriver_chatbot\\chromedriver.exe")
    #driver.get("https://www.google.ca/search?dcr=0&sxsrf=ACYBGNSwCHesxbh4Zrot7gN7881aZfxtPw%3A1572890265123&ei=mWbAXayZB83n5gK7mrLoCA&q=english+to+hindi+translator&oq=english+to+hindi+translator&gs_l=psy-ab.3..0i71l8.0.0..594809...0.4..0.0.0.......0......gws-wiz.Yg3_zU0IXzw&ved=0ahUKEwjsyZfskNHlAhXNs1kKHTuNDI0Q4dUDCAs&uact=5")
    #try:
    #    english_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@class='tw-ta tw-text-large goog-textarea']")))
    #    english_input = driver.find_element_by_xpath("//textarea[@class='tw-ta tw-text-large goog-textarea']")
    #    english_input.clear()
    #    english_input.send_keys("My name is Varun")
    #    time.sleep(0.5)
    #    print("here")
    #    hindi_output = driver.find_element_by_xpath("//pre[@class='tw-data-text tw-text-large tw-ta']/span")
    #    print("here")
    #    #print(hindi_output.text)
    #    file_output.write(hindi_output.text)
    #finally:
    #    driver.close()
    txt = "Michael: The rain in [looks at camera] Spain\nJim: The winter"
    lol = re.sub('Michael:','Michael@',txt)
    lol = re.sub('\n.*:','\nVarun:',lol)
    lol = re.sub('Michael@','Michael:',lol)
    print(lol)
    #x = re.search("^The.*Spain$", txt)
    x = re.search('\[.*\]', txt)

    if (x):
        print("YES! We have a match!")
    else:
        print("No match")

filereader("michael_office_en.txt")
