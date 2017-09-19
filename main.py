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


class HitFun:
    def __init__(self, url):
        self.url = url

    def r_useragent(self):
        u_agents = {
            1 : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            2 : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            3 : "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586",
            4 : "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            5 : "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            6 : "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            7 : "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
            8 : "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
            9 : "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
            10 : "Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36"
        }
        ran = randint(1, 10)
        return u_agents.get(ran, 2)

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
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'installLink')))

            except TimeoutException:
                print "Loading took too much time!"

            install = driver.find_element_by_class_name("installLink")

            install.click()
            try:
                wait = WebDriverWait(driver, 9)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

            except TimeoutException:
                print "Loading took too much time!"
            sleep(1)

            driver.close()

        except Exception, e:
            print "Something is not right! Error: ", e
            print "Closing the instance of browser!"
            driver.close()

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

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'installLink')))

            except TimeoutException:
                print "Loading took too much time!"

            install = driver.find_element_by_class_name("installLink")

            install.click()
            try:
                wait = WebDriverWait(driver, 9)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

            except TimeoutException:
                print "Loading took too much time!"
            sleep(1)
            driver.close()

        except Exception, e:
            print "Something not right, Error: ", e
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
                print "Lets check if Mobile Data successfully turned OFF!, pinging Google..."

        except:
            print "Something went wrong, trying again.."
            continue
        finally:
            if check_internet():
                print "Internet still working, lets try again!"
                return True
            else:
                print "Mobile Data turned OFF!\n"
                break


def turn_on_data():
    while True:
        try:
            if not check_internet():
                print "Now Turning Mobile Data ON, please wait.."

                data_on()

                sleep(8)

                print "Checking connectivity, pinging google.."

        except:
            print "Internet not working, lets try again!"
            continue

        if not check_internet():
            print "Internet not working, lets try again!"
            return True
        else:
            print "Connection established!"
            break


def get_ip():
    i = 5
    while not check_internet():
        print "Waiting for Mobile Data!"
        sleep(0.5)
    else:
        while i:
            try:
                my_ip = requests.get('http://ip.42.pl/raw').text
                return my_ip + "\n"
            except Exception, e:
                print "Unable to get IP, trying again.. Error: ", e
                i -= 1
                pass


print "Welcome to Hax 4Fun clicker!\n==========================================="
print "\nPlease make sure that your Phone is connected and USB Debugging and USB Tethering is enabled."


first_url = str(raw_input("Enter your first 4Fun url: "))

second_url = str(raw_input("Enter second 4Fun url: "))

my_4fun1 = HitFun(url=first_url)

my_4fun2 = HitFun(url=second_url)

while True:
    try:
        n_hits = int(raw_input("Enter the number of Hits to give: "))

    except ValueError:
        print "Not a valid response,Please Try again!"
        continue

    else:
        break


def select_browser():

    print "Which browser you want to use? Press num key:"
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

hit_counter = 1
hits_done = 0


while n_hits:
    t1 = time.time()
    print "Checking Internet connection, pinging Google!"

    if check_internet():
        turn_off_data()
    else:
        print "Mobile Data already OFF"

    turn_on_data()

    print "Your IP Address is: ", get_ip()

    if browser_to_use == 1:
        if hit_counter % 2 == 0:
            print "Everything is OK, opening Link 2"
            my_4fun1.open_firefox()
        else:
            print "Everything is OK, opening Link 1"
            my_4fun2.open_firefox()

    else:
        if hit_counter % 2 == 0:
            print "Everything is OK, opening Link 2"
            my_4fun1.open_chrome()
        else:
            print "Everything is OK, opening Link 1"
            my_4fun2.open_chrome()

    hits_done += 1
    print "Hit was successful\n"
    print "Total Successful hits done: %d" % hits_done
    
    n_hits -= 1
    hit_counter += 1
    
    t2 = time.time()
    print "\nThis Hit took: " + str(t2 - t1) + "seconds\n"
    print "==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ===="

    
    
