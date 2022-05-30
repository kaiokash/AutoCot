from sys import prefix
from tkinter import messagebox
#import pyautogui    
import time 
#import pyperclip
import _tkinter
#import pandas
#import openpyxl
import selenium
import tkinter


# This code is to hide the main tkinter window
root = tkinter.Tk()
root.withdraw()

# Message Box
messagebox.showinfo("Title", "Message")

from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import smtplib  

#import email.message 

#deixar invisivel

options = webdriver.ChromeOptions()


options.add_argument("--headless")

nav = webdriver.Chrome(chrome_options=options)
#nav.maximize_window()
#Pesquisar o site a cotação '''

nav.get("https://www.hotmilhas.com.br/")

time.sleep(3)
#Setar e-mail  

#Nova Cotação 

#nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')
time.sleep(3)
#Achando campo e clicando na opção 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[3]')[0].click()

#Smiles  59K
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[4]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_1 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(40)')[0].click()

#Confirmando com Botão 
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

#pausa
time.sleep(3)


#Nova Cotação 
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()

nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')

time.sleep(3)

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[3]')[0].click()
#Smiles 100K
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[4]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_1 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(81)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()
time.sleep(3)


#Nova Cotação 
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')

time.sleep(3)

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[3]')[0].click()
#Smiles 200K

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[3]/div[4]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_1 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(181)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

time.sleep(3)

#Nova Cotação 
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')

time.sleep(3)

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[4]')[0].click()

#Azul 59K   

nav.find_elements_by_xpath('//*[@id="select_points_3"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_3 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(48)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()
time.sleep(3)

#Nova Cotação 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()



nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')

time.sleep(3)

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[4]')[0].click()

#Azul 100K   

nav.find_elements_by_xpath('//*[@id="select_points_3"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_3 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(89)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()


time.sleep(3)

#Nova Cotação 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()



nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')

time.sleep(3)

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[4]')[0].click()

#Azul 101K   

nav.find_elements_by_xpath('//*[@id="select_points_3"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_3 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(90)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

time.sleep(3)

#Nova Cotação 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


time.sleep(3)

nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')


nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[1]')[0].click()

#Latam 59K   

nav.find_elements_by_xpath('//*[@id="select_points_2"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_2 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(40)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

time.sleep(3)

#Nova Cotação 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


time.sleep(3)

nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')


nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[1]')[0].click()

#Latam 100K   

nav.find_elements_by_xpath('//*[@id="select_points_2"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_2 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(81)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

time.sleep(3)

#Nova Cotação 

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/div[1]/div/a[1]')[0].click()


time.sleep(3)

nav.find_element_by_xpath('//*[@id="quotation-form"]/div[1]/div[1]/input').send_keys('teste@outlook.com')


nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[1]')[0].click()
nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[1]/div[2]/div/div/div[2]/div/ul/li[1]')[0].click()

#Latam 150K   

nav.find_elements_by_xpath('//*[@id="select_points_2"]/div[1]')[0].click()
nav.find_elements_by_css_selector('#select_points_2 > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(131)')[0].click()

nav.find_elements_by_xpath('/html/body/div[6]/div/div/div/div/form/div[2]/div/div/button')[0].click()

nav.close()
