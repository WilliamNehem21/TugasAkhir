#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:40:51 2023

@author: williamnehemia
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os
import pandas as pd

home_url = 'https://www.sciencedirect.com/'
driver = webdriver.Chrome()
driver.get(home_url)
class_tags =  driver.find_elements(By.CLASS_NAME, "anchor anchor-default anchor-has-inherit-color")
print(len(class_tags))
list_url = class_tags.get_attribute('innerHTML')
# contentType=JL&accessType=openAccess&
# class="anchor js-publication-title anchor-default"
# link-anchor u-clr-black
