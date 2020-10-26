import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import time

def _options():
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument('--disable-gpu') if os.name == 'nt' else None # Windows workaround
    options.add_argument("--verbose")
    return options

driver = webdriver.Chrome("C:\\python38\\Scripts\\webdriver\\chromedriver.exe")
driver.get("https://synapcom.myvtex.com/admin/license-manager/#/user-details")
#driver.get("https://synapcom.myvtex.com/admin/license-manager/#/user-list/1")
driver.maximize_window()

time.sleep(4)

driver.find_element_by_xpath("//*[@id='render-admin.signin-legacy']/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div").click()
time.sleep(3)

driver.find_element_by_name("identifier").send_keys("myEmail")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
time.sleep(3)

driver.find_element_by_name("password").send_keys("myPass")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

time.sleep(13)

try:
	iframe = driver.find_element_by_xpath("//*[@id='app-content']/main/iframe")
	driver.switch_to.frame(iframe)

	driver.find_element_by_xpath("//*[@id='user-search-input']").send_keys("contoso@gmail.com")
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='user-name']").send_keys("Contoso")
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='add-role']").send_keys("Owner")
	time.sleep(2)
	driver.find_elements_by_xpath("//*[@id='perfis']/div[2]/div/div[3]/div[1]/div/ul/li")[0].click()
	time.sleep(4)
	
	driver.find_element_by_xpath("//*[@id='role-view-modal']/div[3]/button[1]").click()
	time.sleep(3)

	driver.find_element_by_xpath("//*[@id='perfis']/div[2]/div/button[1]").click()
	
	driver.quit()

except NoSuchElementException as ex:
	print("Exception has been thrown. " + str(ex))
	driver.quit()
