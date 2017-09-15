"""A Python script to get automatic hits"""

__author__      = "Shantam Mathuria"
__credits__ = ["Ujjaval", "Param"]
__email__ = "shantam.m22@gmail.com"

from selenium import webdriver
from os import system
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import socket
import requests


class HitFun:
    def __init__(self, url):
        self.url = url

    def f_profile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.set_preference("general.useragent.override",
                               "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36")
        return profile

    def open(self):

        driver = webdriver.Firefox(firefox_profile=self.f_profile())
        print "Everything is OK, opening link.."
        driver.get(self.url)

        try:
            wait = WebDriverWait(driver, 12)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'installLink')))

        except TimeoutException:
            print "Loading took too much time!"

        install = driver.find_element_by_class_name("installLink")

        install.click()
        try:
            wait = WebDriverWait(driver, 6)
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'id-app-title')))

        except TimeoutException:
            print "Loading took too much time!"
        sleep(1)
        driver.close()


def data_on():
    system("adb shell svc data enable")


def data_off():
    system("adb shell svc data disable")


def check_internet():
    REMOTE_SERVER = "www.google.com"
    try:

        # Lets check if DNS could be resolved

        host = socket.gethostbyname(REMOTE_SERVER)

        s = socket.create_connection((host, 80), 2)
        s.getsockname()
        s.close()
        sleep(2)

        return True

    except:
        pass
    return False


def turn_off_data():
    while True:
        try:
            if check_internet():
                print "Internet is working. Turning OFF Mobile Data, please wait.."
                data_off()
                sleep(2)
                print "Lets check if Mobile Data successfully turned OFF!, pinging Google..."

        except check_internet() == True:
            print "Internet still working, lets try again!"
            continue
        else:
            print "Mobile Data is turned OFF!\n---- ---- ---- ---- ----"
            break


def turn_on_data():
    while True:
        try:
            print "Now Turning Mobile Data ON, please wait.."

            data_on()

            sleep(7)

            print "Checking connectivity, pinging google.."
        except check_internet() == False:
            print "Internet not working, lets try again!"
            continue
        else:
            print "Internet connection established!"
            break


def get_ip():
    i = 5
    while i:
        try:
            my_ip = requests.get('http://ipecho.net/plain?').text
            return my_ip
        except:
            print "Unable to get IP, trying again.."
            i -= 1
            pass


print "Welcome to Hax 4Fun clicker!\n==========================================="
print "\nPlease make sure that your Phone is connected and USB Debugging and USB Tethering is enabled."

url = str(raw_input("Enter your 4Fun url: "))

my_4fun = HitFun(url)

while True:
    try:
        n_hits = int(raw_input("Enter the number of Hits to give: "))

    except ValueError:
        print "The entered value is not recognised, Try again!"
        continue

    else:
        break

hits_done = 0

while n_hits:
    print "Checking Internet connection, pinging Google!"

    turn_off_data()

    turn_on_data()

    print "Your IP Address is: ", get_ip()

    my_4fun.open()

    print "Hit was successful\n==== ==== ==== ==== ==== ==== ==== ===="
    hits_done += 1
    n_hits -= 1
    
print "Total Successful hits done: %d" %(hits_done)
