from selenium import webdriver
from os import system
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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

used_agent = []


class HitFun:
    def __init__(self, url):
        self.url = url

    def r_useragent(self):
        i, f = 1, 282

        u_agents = {
            1 : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            2 : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            3 : "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 Edge/13.10586",
            4 : "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            5 : "Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            6 : "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36"
        }
        while True:
            ran = randint(i, f)

            if used_agent.count(ran) > 2:
                continue

            else:
                used_agent.append(ran)
                return u_agents.get(ran, 250)

    def phantom_arg(self):
        phan = dict(DesiredCapabilities.PHANTOMJS)

        phan['phantomjs.page.settings.userAgent'] = self.r_useragent()
        phan['phantomjs.page.settings.loadImages'] = False
        return phan

    def open_phantom(self):

        driver = webdriver.PhantomJS(executable_path=r"phantomjs\bin\phantomjs.exe", desired_capabilities=self.phantom_arg())
        driver.set_window_size(720, 1280)

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnArea"]/a')))
                print driver.current_url()
                install = driver.find_element_by_class_name("installLink")

                driver.execute_script("arguments[0].click();", install)

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

                print "Hit was successful\n"

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

        except Exception, e:
            print "Something not right, Error: ", e
            driver.quit()

        finally:
            driver.quit()

    def f_profile(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        profile.set_preference("general.useragent.override", self.r_useragent())
        profile.set_preference('permissions.default.image', 1)
        return profile

    def open_firefox(self):

        driver = webdriver.Firefox(executable_path=r'firefox_driver\geckodriver.exe', firefox_profile=self.f_profile())
        driver.set_window_size(720, 1280)

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 15)
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'INSTALL')))

                install = driver.find_element_by_class_name("installLink")

                driver.execute_script("arguments[0].click();", install)

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

                print "Hit was successful\n"

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

        except Exception, e:
            print "Something not right, Error: ", e
            driver.quit()

        finally:
            driver.quit()

    def c_profile(self):

        c_option = webdriver.ChromeOptions()
        c_option.add_argument('--incognito')

        user_agent = self.r_useragent()
        c_option.add_argument("--user-agent="+user_agent)

        prefs = {"profile.managed_default_content_settings.images": 2}
        c_option.add_experimental_option("prefs", prefs)

        return c_option

    def open_chrome(self):

        driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe', chrome_options=self.c_profile())
        driver.set_window_size(720, 1280)

        try:

            driver.get(self.url)

            try:
                wait = WebDriverWait(driver, 15)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnArea"]/a')))

                install = driver.find_element_by_class_name("installLink")

                driver.execute_script("arguments[0].click();", install)

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

                print "Hit was successful\n"

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

        except Exception, e:
            print "Something not right, Error: ", e
            driver.quit()

        finally:
            driver.quit()


def data_on():
    system("adb shell svc data enable")


def data_off():
    system("adb shell svc data disable")


def check_internet():

    remote_server = "www.google.com"

    try:

        # Lets check if DNS could be resolved

        host = socket.gethostbyname(remote_server)

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

            sleep(1)

        except:
            print "Internet not working, lets try again!"
            continue
        else:
            print "Mobile Data turned ON!\n"
            break


def get_ip():
    i = 5
    j = 10
    while j and not check_internet():
        print "Waiting for Mobile Data!"
        sleep(1)
        j -= 1
    else:
        while i:
            try:
                if i % 2 == 0:
                    my_ip = requests.get('https://api.ipify.org/?format=json').json()['ip']
                    return my_ip + "\n"
                else:
                    my_ip = requests.get('https://wtfismyip.com/text').text
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


def add_wait(start, end):
    random_seconds = randint(start, end)
    return random_seconds


def random_urls():
    ran_num = randint(1, len(my_urls))
    return my_urls.get(ran_num)

"""
Not needed anymore since I added random url support
my_4fun1 = HitFun(url=first_url)

my_4fun2 = HitFun(url=second_url)
"""

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
        while True:

            try:
                browser_name = int(raw_input("'1' Firefox\n'2' Chrome\n'3' Headless Browser\nEnter you choice: "))

            except ValueError:
                print "UhhOhh! Please enter only integer, Try again!"
                continue
            else:
                break
        if browser_name == 1:
            print "You selected Firefox browser!\n"
            break
        elif browser_name == 2:
            print "You selected Chrome browser!\n"
            break
        elif browser_name == 3:
            print "You selected Headless Browser!\n"
            break
        else:
            print "That is not a valid response, try again!"
            continue
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

            sleep(3)

        except:
            print "Can't interact with Phone, check usb connection!"
            continue
        else:
            break

while n_hits:

    t1 = time.time()

    current_url = random_urls()

    my_4fun = HitFun(url=current_url)

    if hits_done > 0:

        while True:
            print "\n____CHECKING YOUR IP NOW____\n"
            new_ip = get_ip()

            if new_ip == last_ip[-1]:
                print "Not changed, changing your IP, please wait.....\n"
                change_ip()
                sleep(5)
                continue
            else:
                print "IP changed successfully!!\n"
                last_ip.append(new_ip)
                print "Last IP Address: ", last_ip[-2]
                break
    else:
        change_ip()
        sleep(9)
        new_ip = get_ip()
        last_ip.append(new_ip)

    print "New IP Address: ", last_ip[-1]

    if browser_to_use == 1:
        print "Everything is OK, opening random url"
        my_4fun.open_firefox()

    elif browser_to_use == 2:
        print "Everything is OK, opening random url"
        my_4fun.open_chrome()
    else:
        print "Everything is OK, opening random url"
        my_4fun.open_phantom()

    hits_done += 1

    print "Total Successful hits done: %d" % hits_done

    n_hits -= 1

    t2 = time.time()

    print "\nThis Hit took: %.2f seconds" % (t2 - t1)

    waiting = add_wait(8, 17)

    print("Changing IP for next session!\n")

    change_ip()

    print "Adding a random wait of: %s seconds!" % str(waiting)

    print "==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ===="

    sleep(waiting)

print "Thanks for using Hax Pyhits!"
