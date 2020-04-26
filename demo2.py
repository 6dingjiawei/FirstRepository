# -*-coding:UTF-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://localhost/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
