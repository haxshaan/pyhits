from selenium import webdriver
from os import system
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import socket
import requests
from random import randint
import time

__author__ = "Shantam Mathuria (Hax0)"
__copyright__ = "Open source"
__credits__ = ["Shantam Mathuria"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Shantam Mathuria"
__email__ = "shantam.m22@gmail.com"
__status__ = "Production"


class HitFun:
    def __init__(self, url):
        self.url = url

    def r_useragent(self):
        u_agents = {
            1 : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            2 : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            3 : "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 Edge/13.10586",
            4 : "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            5 : "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            6 : "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            7 : "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
            8 : "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
            9 : "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/56.0.2924.87 Safari/537.36",
            10 : "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Safari/537.36",
            11 : "Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/535.19",
            12 : "Mozilla/5.0 (Linux; Android 4.0.4; SGH-I777 Build/Task650 & Ktoonsez AOKP) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/535.19",
            13 : "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-J727A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
            14 : "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-J727AZ Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
            15 : "Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-J327A Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
            16 : "Mozilla/5.0 (Linux; Android 7.1.1; HTC U11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
            17 : "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile",
            18 : "Mozilla/5.0 (Linux; Android 8.0.0; Pixel Build/OPR6.170623.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36",
            19 : "Mozilla/5.0 (Linux; Android 7.1; Pixel Build/NDE63V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36",
            20 : "Mozilla/5.0 (Linux; Android 7.1.2; Pixel Build/NHG47O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
            21 : "Mozilla/5.0 (Linux; Android 7.1.2; Pixel Build/NJH47F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.107 Mobile Safari/537.36",
            22 : "Mozilla/5.0 (Linux; Android 7.1; Pixel Build/NDE63X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36"
        }
        ran = randint(1, 22)
        return u_agents.get(ran, 20)

    def f_profile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.set_preference("general.useragent.override", self.r_useragent())
        profile.set_preference('permissions.default.image', 1)
        return profile

    def open_firefox(self):

        driver = webdriver.Firefox(executable_path=r'firefox_driver\geckodriver.exe', firefox_profile=self.f_profile())

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 15)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'installLink')))

            except TimeoutException:
                print "Loading took too much time!"

            install = driver.find_element_by_class_name("installLink")

            install.click()
            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

            except TimeoutException:
                print "Loading took too much time!"
            sleep(1)

            driver.quit()

        except Exception, e:
            print "Something is not right! Error: ", e
            print "Closing the instance of browser!"
            driver.quit()

    def c_profile(self):

        c_option = webdriver.ChromeOptions()
        c_option.add_argument('--incognito')

        user_agent = self.r_useragent()
        c_option.add_argument("--user-agent="+user_agent)

        prefs = {"profile.managed_default_content_settings.images":2}
        c_option.add_experimental_option("prefs", prefs)

        return c_option

    def open_chrome(self):

        driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe', chrome_options=self.c_profile())
        driver.set_window_size(720, 1280)

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 15)
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'INSTALL')))

            except TimeoutException:
                print "Loading took too much time!"

            install = driver.find_element_by_class_name("installLink")

            driver.execute_script("arguments[0].click();", install)

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

            except TimeoutException:
                print "Loading took too much time!"
            sleep(1)
            driver.quit()

        except Exception, e:
            print "Something not right, Error: ", e
            driver.quit()


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
            print "Turning OFF Mobile Data, please wait.."
            data_off()

        except:
            print "Something went wrong, trying again.."
            continue
        else:
            print "Mobile Data turned OFF!\n"
            break


def turn_on_data():
    while True:
        try:
            print "Now Turning Mobile Data ON, please wait.."

            data_on()

            sleep(8)

        except:
            print "Internet not working, lets try again!"
            continue
        else:
            print "Mobile Data turned ON!\n"
            break


def get_ip():
    i = 5
    j = 20
    while j and not check_internet():
        print "Waiting for Mobile Data!"
        sleep(1)
        j -= 1
    else:
        while i:
            try:
                my_ip = requests.get('http://ip.42.pl/raw').text
                return my_ip + "\n"
            except Exception, e:
                print "Unable to get IP, trying again.. Error: ", e
                i -= 1
                continue

print "Welcome to Hax Pyhits!\n==========================================="
print "\nPlease make sure that your Phone is connected and USB Debugging & USB Tethering is enabled."
print "\nTo stop the program at any point, press CTRL + C\n"

first_url = str(raw_input("Enter your first 4Fun url: "))

second_url = str(raw_input("Enter second 4Fun url: "))

my_urls = {
        1: first_url,
        2: second_url
    }


def add_wait():
    random_seconds = randint(5, 15)
    return random_seconds


def random_urls():
    ran_num = randint(1, len(my_urls))
    return my_urls.get(ran_num)

# Not needed anymore since I added random url support
#my_4fun1 = HitFun(url=first_url)

#my_4fun2 = HitFun(url=second_url)

while True:
    try:
        n_hits = int(raw_input("Enter the number of Hits to give: "))

    except ValueError:
        print "Not a valid response,Please Try again!"
        continue

    else:
        break


def select_browser():

    print "Select your browser. Press num key:"
    while True:
        try:
            browser_name = int(raw_input("'1' Firefox\n'2' Chrome\nEnter you choice: "))

        except ValueError:
            print "UhhOhh! Please enter only integer, Try again!"
            continue
        else:
            break
    if browser_name == 1:
        print "You selected Firefox browser!\n"
    else:
        print "You selected Chrome browser!\n"
    return browser_name


browser_to_use = select_browser()

hits_done = 0

last_ip = []


def change_ip():
    while True:
        try:
            turn_off_data()

            sleep(1)

            turn_on_data()

        except:
            print "Can't interact with Phone, check usb connection!"
            continue
        else:
            break

while n_hits:

    t1 = time.time()

    current_url = random_urls()

    my_4fun = HitFun(url=current_url)

    if hits_done:

        while True:
            print "\nCHECKING YOUR IP NOW!!\n"
            new_ip = get_ip()

            if new_ip == last_ip[-1]:
                print "Not changed, changing your IP, please wait.....\n"
                change_ip()
                continue
            else:
                print "IP changed successfully!!\n"
                break
    else:
        change_ip()

    last_ip.append(get_ip())

    print "Your IP Address is: ", last_ip[-1]

    if browser_to_use == 1:
        print "Everything is OK, opening random url"
        my_4fun.open_firefox()

    else:
        print "Everything is OK, opening random url"
        my_4fun.open_chrome()

    hits_done += 1
    print "Hit was successful\n"
    print "Total Successful hits done: %d" % hits_done

    n_hits -= 1

    t2 = time.time()

    print "\nThis Hit took: " + str(t2 - t1) + "seconds\n"

    waiting = add_wait()

    print "Adding a random wait of: %s seconds!" % str(waiting)

    print "==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ===="

    sleep(waiting)

print "Thanks for using Hax Pyhits!"
