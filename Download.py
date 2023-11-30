import time

from SeleniumLibrary import SeleniumLibrary
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

lib = SeleniumLibrary()

download_directory = r"C:\Users\AbdulMalik\OneDrive - Winfo Solutions\Desktop\RPA Framework"

chrome_options = ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
chrome_options.add_argument(f"--user-data-dir={chrome_profile_directory}")


lib.open_browser(url='https://testfile.org/audio/ircam/', browser='chrome', options=chrome_options)
lib.maximize_browser_window()

lib.wait_until_element_is_visible('//span[text()="SAMPLE - 1"]', timeout=120)
lib.click_element('//span[text()="SAMPLE - 1"]')

time.sleep(20)

lib.close_browser()
