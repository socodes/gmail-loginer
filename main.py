from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

#provide url
url = 'https://www.gmail.com'
#provide username
gmail_username = input("Enter your username: ")
#provide password
gmail_password = input("Enter your password: ")

#create a driver
driver = webdriver.Chrome(ChromeDriverManager().install())
#open url with driver
driver.get(url)
#wait to see the reaction
driver.implicitly_wait(30)
#find username element and provide username to it
driver.find_element("id",'identifierId').send_keys(gmail_username)
#click next button
driver.find_element("id",'identifierNext').click()
#wait to see reaction
driver.implicitly_wait(30)
#find password element and provide password to it
driver.find_element("name",'password').send_keys(gmail_password)
#click next button
driver.find_element("id",'passwordNext').click()