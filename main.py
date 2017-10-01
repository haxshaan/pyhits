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
        i, f = 1, 92
        u_agents = {
            1 : "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
            2 : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
            3 : "Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36 Edge/13.10586",
            4 : "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
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
            22 : "Mozilla/5.0 (Linux; Android 7.1; Pixel Build/NDE63X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36",
            23 : "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; 2345Explorer 5.0.0.14136)",
            24 : "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6",
            25 : "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.3 (KHTML, like Gecko)",
            26 : "Chrome/6.0.472.63 Safari/534.3",
            27 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            28 : "Opera/9.00 (Windows NT 5.1; U; en)",
            29 : "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522+ (KHTML, like Gecko) Safari/419.3",
            30 : "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3",
            31 : "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, Like Gecko) Version/6.0.0.141 Mobile Safari/534.1+",
            32 : "Python-urllib/2.1",
            33 : "Yahoo! Slurp/Site Explorer",
            34 : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1 QIHU 360SE",
            35 : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 QIHU 360EE",
            36 : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 QIHU 360SE",
            37 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; 360SE)",
            38 : "Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7552.EU",
            39 : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Kuaiso/1.42.501.445 Safari/537.36",
            40 : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; JyxoToolbar1.0; http://www.Abolimba.de; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.1.4322)",
            41 : "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; http://www.Abolimba.de)",
            42 : "Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420  (KHTML, like Gecko)",
            43 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            44 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Acoo Browser; InfoPath.2; .NET CLR 2.0.50727; Alexa Toolbar)",
            45 : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Acoo Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            46 : "Mozilla/5.0 (Windows NT 6.1; rv:8.0) Gecko/20111108 Firefox/8.0 Alienforce/8.0",
            47 : "amaya/9.52 libwww/5.4.0",
            48 : "amaya/11.1 libwww/5.4.0",
            49 : "Amiga-AWeb/3.5.07 beta",
            50 : "AmigaVoyager/3.4.4 (MorphOS/PPC native)",
            51 : "AmigaVoyager/2.95 (compatible; MC680x0; AmigaOS)",
            52 : "AmigaVoyager/3.2 (AmigaOS/MC680x0)",
            53 : "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.47 Safari/535.11 MRCHROME",
            54 : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.1.963.51 Safari/535.11 MRCHROME SOC",
            55 : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1501.78 Safari/537.36 MRCHROME SOC",
            56 : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.191 Amigo/54.0.2840.191 MRCHROME SOC Safari/537.36",
            57 : "Mozilla/3.04 (compatible; ANTFresco/2.13; RISC OS 4.02)",
            58 : "Mozilla/3.04 (compatible; NCBrowser/2.35; ANTFresco/2.17; RISC OS-NC 5.13 Laz1UK1309)",
            59 : "HbbTV/1.1.1 (;Hisense;MT5651;;;) ANTGalio/3.3.0.26.04",
            60 : "Mozilla/4.0 (compatible; MSIE 6.0; AOL 6.0; Windows NT 5.1)",
            61 : "Mozilla/4.0 (compatible; MSIE 7.0; AOL 7.0; Windows NT 5.1; FunWebProducts)",
            62 : "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.0; Windows NT 5.1; .NET CLR 1.1.4322; Zango 10.1.181.0)",
            63 : "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            64 : "Mozilla/4.0 (compatible; MSIE 6.0; AOL 8.0; Windows NT 5.1; SV1)",
            65 : "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.17; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
            66 : "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.1; AOLBuild 4334.5000; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; InfoPath.1)",
            67 : "Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.6; AOLBuild 4340.12; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
            68 : "Mozilla/5.0 (AOL 9.7; AOLBuild 4343.55; Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240",
            69 : "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 AOL/9.8 AOLBuild/4346.18.US Safari/537.36",
            70 : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2841.00 Safari/537.36 AOLShield/54.0.2848.0",
            71 : "xChaos_Arachne/5.1.89;GPL,386+",
            72 : "Mozilla/5.0 (X11; U; Linux; C -) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.5",
            73 : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            74 : "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            75 : "Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
            76 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Avant Browser)",
            77 : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)",
            78 : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; JyxoToolbar1.0; Embedded Web Browser from: http://bsalsa.com/; Avant Browser; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET CLR 1.1.4322)",
            79 : "Avant Browser (http://www.avantbrowser.com)",
            80 : "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120515 Firefox/12.0 AvantBrowser/Tri-Core",
            81 : "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20120325 Firefox/11.0 AvantBrowser/Tri-Core",
            82 : "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20120325 Firefox/11.0 AvantBrowser/Tri-Core",
            83 : "Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; Avant Browser; rv:11.0) like Gecko",
            84 : "Mozilla/5.0 (Windows NT 6.3; WOW64; Avant TriCore) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
            85 : "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:27.0; Avant TriCore) Gecko/20100101 Firefox/27.0",
            86 : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 ASW/1.51.2220.53",
            87 : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36 ASW/1.46.1990.139",
            88 : "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) WhiteHat Aviator/33.0.1750.117 Chrome/33.0.1750.117 Safari/537.36",
            89 : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) WhiteHat Aviator/33.0.1750.117 Chrome/33.0.1750.117 Safari/537.36",
            90 : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 AviraScout/16.11.2883.2017",
            91 : "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh_CN) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0 baidubrowser/1.x Safari/534.7",
            92 : "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; baidubrowser 1.x)"
        }
        ran = randint(i, f)
        return u_agents.get(ran, 3)

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
                wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'INSTALL')))

                install = driver.find_element_by_class_name("installLink")

                driver.execute_script("arguments[0].click();", install)

            except TimeoutException:
                print "Loading took too much time!"
                driver.quit()

            try:
                wait = WebDriverWait(driver, 14)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'details-info')))

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

            sleep(8)

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
                my_ip = requests.get('https://api.ipify.org/?format=json').json()['ip']
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
            print "\n____CHECKING YOUR IP NOW____\n"
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

    if hits_done > 1:
        print "Last IP Address: ", last_ip[-2]
    print "New IP Address: ", last_ip[-1]

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
