from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import csv
import io

driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")

driver.get('http://210.212.217.214/')
driver.maximize_window()


# id_list = ['R170176','R170181']
# pwd_list = ['NO68Q','DI69Z']

outputFile = io.open('Results.csv','w',newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Id','Name','SGPA'])

id_list = []
pwd_list = []
with open('id.txt','r') as f:
    l = f.readlines()
    # print(l)
    for i in l:
        id_list.append(i[0:7].rstrip('\n'))
        pwd_list.append(i[8:].rstrip('\n'))


for i in range(len(id_list)):
    usr = driver.find_element(By.NAME, "username")
    usr.send_keys(id_list[i])
    pwd = driver.find_element(By.NAME,"password")
    pwd.send_keys(pwd_list[i])

    btn = driver.find_element(By.NAME,"login")
    btn.click()
    # time.sleep(1)

    find_puc = driver.find_element(By.LINK_TEXT,"AY19-20 Results")
    find_puc.click()
    find_SEM = driver.find_element(By.LINK_TEXT,"SEM-I")
    find_SEM.click()
    semResults = driver.find_element(By.LINK_TEXT,"SEM-1Results")
    semResults.click()

    getID = driver.find_element(By.ID,"pd")
    l = getID.text.split('\n')
    data = []
    for i in l:
        if i.startswith('ID'):
            i = i.lstrip('ID : ')
            data.append(i)
        if i.startswith('Name'):
            i = i.lstrip('Name : ')
            data.append(i)
    # print(data)
    txt = driver.find_element(By.TAG_NAME,'tbody')
    # print(txt.text)
    data.append(txt.text[-4:])
    outputWriter.writerow(data)
    print(data)
    logout = driver.find_element(By.LINK_TEXT,"Logout")
    logout.click()
    # time.sleep(1)

driver.close()
