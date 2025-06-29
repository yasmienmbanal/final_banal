from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("http://localhost/ocss/admin_login.php")
driver.maximize_window()
time.sleep(3)

username = driver.find_element(By.NAME, "admin_username").send_keys("admin")
time.sleep(1)
password = driver.find_element(By.NAME, "admin_pass").send_keys("admin")
time.sleep(1)
button = driver.find_element(By.NAME, "admin_login").click()
time.sleep(2)

nav_bar = driver.find_element(By.XPATH, "/html/body/div[8]/span").click()
time.sleep(2)

faculty = driver.find_element(By.CSS_SELECTOR, "#mySidenav > ul > li:nth-child(1) > a").click()
time.sleep(2)
emp_num = driver.find_element(By.NAME, "emp_number").send_keys("17-06")
firstname = driver.find_element(By.NAME, "fname").send_keys("Yasmien Banal")
date_hired = driver.find_element(By.NAME, "date_hired")
driver.execute_script("arguments[0].type = 'date'; arguments[0].value = '2023-06-15';", date_hired)
status = driver.find_element(By.NAME, "status").send_keys("Temporary")
field = driver.find_element(By.NAME, "background_field").send_keys("Social Sciences")
address = driver.find_element(By.NAME, "address").send_keys("Agdangan, Quezon")
contact = driver.find_element(By.NAME, "contact_no").send_keys("09919198202")
email = driver.find_element(By.NAME, "email").send_keys("yasmienbanal@gmail.com")
password = driver.find_element(By.NAME, "pass").send_keys("reign111#")
time.sleep(1)
btn = driver.find_element(By.NAME, "register_faculty").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

nav_bar = driver.find_element(By.XPATH, "/html/body/div[8]/span").click()
time.sleep(2)

faculty = driver.find_element(By.CSS_SELECTOR, "#mySidenav > ul > li:nth-child(1) > a").click()
time.sleep(2)
emp_num = driver.find_element(By.NAME, "emp_number").send_keys("17-06")
firstname = driver.find_element(By.NAME, "fname").send_keys("Yasmien Banal")
date_hired = driver.find_element(By.NAME, "date_hired")
driver.execute_script("arguments[0].type = 'date'; arguments[0].value = '2023-06-15';", date_hired)
status = driver.find_element(By.NAME, "status").send_keys("Temporary")
field = driver.find_element(By.NAME, "background_field").send_keys("Social Sciences")
address = driver.find_element(By.NAME, "address").send_keys("Agdangan, Quezon")
contact = driver.find_element(By.NAME, "contact_no").send_keys("09919198202")
email = driver.find_element(By.NAME, "email").send_keys("yasmienbanal@gmail.com")
password = driver.find_element(By.NAME, "pass").send_keys("reign111#")
time.sleep(1)
btn = driver.find_element(By.NAME, "register_faculty").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

nav_bar = driver.find_element(By.XPATH, "/html/body/div[8]/span").click()
time.sleep(2)

subject = driver.find_element(By.CSS_SELECTOR, "#mySidenav > ul > li:nth-child(2) > a").click()
time.sleep(2)

driver.find_element(By.NAME, "subject_code").send_keys("INTE 362")
driver.find_element(By.NAME, "subject_description").send_keys("Quality Assurance")
driver.find_element(By.NAME, "unit").send_keys("3")
driver.find_element(By.NAME, "lecture").send_keys("2")
driver.find_element(By.NAME, "laboratory").send_keys("3")
time.sleep(1)
driver.find_element(By.NAME, "add").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

nav_bar = driver.find_element(By.XPATH, "/html/body/div[8]/span").click()
time.sleep(2)

room = driver.find_element(By.CSS_SELECTOR, "#mySidenav > ul > li:nth-child(3) > a").click()
time.sleep(2)

driver.find_element(By.NAME, "room").send_keys("107")
time.sleep(1)
driver.find_element(By.NAME, "add_room").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

nav_bar = driver.find_element(By.XPATH, "/html/body/div[8]/span").click()
time.sleep(2)

schedules = driver.find_element(By.CSS_SELECTOR, "#mySidenav > ul > li:nth-child(7) > a").click()
time.sleep(2)

subject_description = driver.find_element(By.ID, "subject_description").send_keys("Quality Assurance")
time.sleep(1)
day = driver.find_element(By.ID, "day_description").send_keys("T F")
time.sleep(1)
time_dropdown = driver.find_element(By.ID, "time_description").send_keys("4:30-6:00")
time.sleep(1)
room_dropdown = driver.find_element(By.ID, "room_description").send_keys("107")
time.sleep(1)
professor = driver.find_element(By.ID, "fname").send_keys("Yasmien Banal")
time.sleep(1)
driver.find_element(By.NAME, "add_schedule").click()
time.sleep(2)

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print("ALERT TEXT:", alert.text)
    alert.accept()
    print("Alert closed successfully.")
except:
    print("No alert appeared after duplicate entry.")

time.sleep(5)
driver.quit()