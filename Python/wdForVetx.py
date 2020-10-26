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
#driver.get("https://synapcom.myvtex.com/admin/license-manager/#/user-details")
driver.get("https://hermanmiller.myvtex.com/admin/license-manager/#/user-details")
driver.maximize_window()

time.sleep(4)

driver.find_element_by_xpath("//*[@id='render-admin.signin-legacy']/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div").click()
time.sleep(3)

driver.find_element_by_name("identifier").send_keys("")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
time.sleep(3)

driver.find_element_by_name("password").send_keys("")
time.sleep(3)

driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

time.sleep(13)

try:
	iframe = driver.find_element_by_xpath("//*[@id='app-content']/main/iframe")
	driver.switch_to.frame(iframe)

	driver.find_element_by_xpath("//*[@id='user-search-input']").send_keys("")
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='user-name']").send_keys("")
	time.sleep(2)
	driver.find_element_by_xpath("//*[@id='add-role']").send_keys("")
	time.sleep(2)
	driver.find_elements_by_xpath("//*[@id='perfis']/div[2]/div/div[3]/div[1]/div/ul/li")[0].click()
	time.sleep(4)
	
	driver.find_element_by_xpath("//*[@id='role-view-modal']/div[3]/button[1]").click()
	time.sleep(3)

	driver.find_element_by_xpath("//*[@id='perfis']/div[2]/div/button[1]").click()
	time.sleep(8)

	driver.find_element_by_xpath("//*[@id='usuarios']/div[1]/p/button").click()
	time.sleep(3)

	count = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
				31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,
				59,60,61,62,63,64, 65]

	vEmail = [""]
	
	vName = [""]
	
	vProfile = [""]

	for c in count:

		driver.find_element_by_xpath("//*[@id='user-search-input']").send_keys(vEmail[c])
		time.sleep(2)
		
		driver.find_element_by_xpath("//*[@id='user-name']").send_keys(vName[c])
		time.sleep(2)
		
		driver.find_element_by_xpath("//*[@id='add-role']").send_keys(vProfile[c])
		time.sleep(2)
		
		driver.find_elements_by_xpath("//*[@id='perfis']/div[2]/div/div[3]/div[1]/div/ul/li")[0].click()
		time.sleep(4)
	
		driver.find_element_by_xpath("//*[@id='role-view-modal']/div[3]/button[1]").click()
		time.sleep(3)

		driver.find_element_by_xpath("//*[@id='perfis']/div[2]/div/button[1]").click()
		time.sleep(8)

		driver.find_element_by_xpath("//*[@id='usuarios']/div[1]/p/button").click()
		time.sleep(2)

		print(c)

except NoSuchElementException as ex:
	print("Exception has been thrown. " + str(ex))
	driver.quit()
