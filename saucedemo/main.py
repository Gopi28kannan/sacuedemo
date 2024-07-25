from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from Data import datas
from Locators import locator
import pytest
import pandas as pd
import csv


class Test_Webpage:

    csv_file = 'product'
    field_names = ['Product Name', 'Description', 'Price']
    csv_name = 'Result/'+csv_file+'.csv'
    with open(csv_name, 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = field_names) 
        writer.writeheader()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_open_webpage(self):
        self.driver.get(datas.data().url)
        self.driver.maximize_window()
        time.sleep(3)

    def test_login_webpage(self):
        self.driver.find_element(By.XPATH, locator.locate().username).send_keys(datas.data().user_name)
        self.driver.find_element(By.XPATH, locator.locate().Password).send_keys(datas.data().password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, locator.locate().login).click()
        time.sleep(2)

    def product(self):
        Product_name = self.driver.find_element(By.XPATH, locator.locate().item_name).text
        Description = self.driver.find_element(By.XPATH, locator.locate().description).text
        Price = self.driver.find_element(By.XPATH, locator.locate().price).text
        table=[]
        table_dict = {'Product Name': Product_name, 'Description': Description, 'Price': Price}
        table.append(table_dict)
        try:
            with open(self.csv_name, 'a') as adds:
                writer = csv.DictWriter(adds, fieldnames = self.field_names)
                writer.writerows(table)
            print('Data added in excel file')
        except:
            print("Data None")
        time.sleep(1)
        table.clear()
        self.driver.back()
        time.sleep(3)

    def test_products(self):
        items = self.driver.find_elements(By.XPATH, locator.locate().items)
        for item in items:
            item.click()
            time.sleep(2)
            self.product()


web = Test_Webpage()
web.test_open_webpage()
web.test_login_webpage()
web.test_products()

