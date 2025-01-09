#!/usr/bin/env python
# coding: utf-8

# In[1]:


api_key = 'd05ade6f74865817bb0abc0ec55eff38'  # 2Captcha API

DATE_ = '07082024'

COUNTY = 'MIAMI-DADE'

''' begin county options

Alachua
Baker
Bay
Bradford
Brevard
Broward
Calhoun
Charlotte
Citrus
Clay
Collier
Columbia
DeSoto
Dixie
Duval
Escambia
Flagler
Franklin
Gadsden
Gilchrist
Glades
Gulf
Hamilton
Hardee
Hendry
Hernando
Highlands
Hillsborough
Holmes
Indian River
Jackson
Jefferson
Lafayette
Lake
Lee
Leon
Levy
Liberty
Madison
Manatee
Marion
Martin
Miami-Dade
Monroe
Nassau
Okaloosa
Okeechobee
Orange
Osceola
Palm Beach
Pasco
Pinellas
Polk
Putnam
Santa Rosa
Sarasota
Seminole
St. Johns
St. Lucie
Sumter
Suwannee
Taylor
Union
Volusia
Wakulla
Walton
Washington


end counties '''

names_to_added = 100

# from seleniumwire import webdriver  # Import from seleniumwire
from bs4 import BeautifulSoup
import time
import sys
import os
from twocaptcha import TwoCaptcha
from selenium import webdriver
# from PIL import Image
from io import BytesIO
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests
import base64
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://chrome.google.com/webstore/detail/bihmplhobchoageeokmgbdihknkjbknd')


# In[ ]:



driver.switch_to.window(driver.window_handles[0])
driver.get('https://services.flhsmv.gov/crashreportpurchasing/')
driver.implicitly_wait(10)
#css_ele = driver.find_element(By.CSS_SELECTOR)
#css_eles = driver.find_elements(By.CSS_SELECTOR)

driver.find_element(By.CSS_SELECTOR, 'div input[type="submit"]').click()
driver.find_element(By.CSS_SELECTOR, 'input[id="LegalRepresentative"]').click()
driver.find_element(By.CSS_SELECTOR, 'option[value="MD"]').click()
driver.find_element(By.CSS_SELECTOR, 'input[data-val-required="DL/ID Card Number: Please complete the field."]').send_keys('2343242')
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

i = 0

rmpr = []
# Switch to the newly opened tab (index 1 in window_handles)
driver.switch_to.window(driver.window_handles[0])

# Switch to the newly opened tab (index 1 in window_handles)
driver.switch_to.window(driver.window_handles[0])


ALL_Last_names = ['Smith', 'Williams', 'Johnson', 'Rodriguez', 'Brown', 'Jones', 'Gonzalez', 'Davis', 'Miller', 'Perez',
                  'Hernandez', 'Martinez', 'Thomas', 'Lopez', 'Wilson', 'Anderson', 'Jackson', 'Diaz', 'Taylor',
                  'Martin', 'Moore', 'White', 'Thompson', 'Fernandez', 'Harris', 'Sanchez', 'Rivera', 'Clark', 'Hall',
                  'Robinson', 'Lewis', 'Walker', 'Lee', 'Allen', 'Roberts', 'Young', 'Green', 'King', 'Scott', 'Torres',
                  'Adams', 'Baker', 'Campbell', 'Wright', 'Alvarez', 'Gomez', 'Hill', 'Cruz', 'Nelson', 'Carter',
                  'Mitchell', 'Edwards', 'Morales', 'Ramirez', 'Collins', 'Evans', 'Stewart', 'Phillips', 'Kelly',
                  'Turner', 'Morris', 'Bell', 'Parker', 'Ramos', 'Rogers', 'Murphy', 'Morgan', 'Bennett', 'Ortiz',
                  'Reyes', 'Cooper', 'Cook', 'Watson', 'Ruiz', 'Ward', 'Howard', 'Brooks', 'Powell', 'Wood', 'Simmons',
                  'Ross', 'Suarez', 'Richardson', 'Butler', 'Cox', 'Jenkins', 'Sullivan', 'Cohen', 'Gray', 'Gordon',
                  'Peterson', 'Joseph', 'Griffin', 'Reed', 'Graham', 'Jimenez', 'Gutierrez', 'Murray', 'Hughes',
                  'Hamilton', 'Russell', 'Jordan', 'Myers', 'Santiago', 'Castillo', 'Henderson', 'Barnes', 'Price',
                  'Fisher', 'Nguyen', 'Delgado', 'Sanders', 'Foster', 'Castro', 'Patel', 'Henry', 'McDonald',
                  'Reynolds', 'Vazquez', 'Alexander', 'Ellis', 'Perry', 'Medina', 'Coleman', 'Wallace', 'Patterson',
                  'Long', 'Flores', 'Gibson', 'Stevens', 'Dixon', 'Grant', 'Kennedy', 'West', 'Daniels', 'Marshall',
                  'Ford', 'Mills', 'Cole', 'Stephens', 'Shaw', 'Vega', 'Vargas', 'Owens', 'Crawford', 'Herrera',
                  'Andrews', 'Silva', 'Mendez', 'Acosta', 'Stone', 'Cabrera', 'Hart', 'Greene', 'Valdes', 'Hunter',
                  'Romero', 'Rose', 'Wells', 'Burns', 'Freeman', 'Holmes', 'Simpson', 'Snyder', 'Ferguson', 'Palmer',
                  'Richards', 'Soto', 'Black', 'Pierre', 'Nunez', 'Porter', 'Leon', 'Colon', 'Santos', 'Fox', 'Knight',
                  'Hicks', 'Ryan', 'Carroll', 'Pena', 'Figueroa', 'Burke', 'Hunt', 'Lane', 'Bradley', 'Tucker', 'Rojas',
                  'Gardner', 'Moreno', 'Wagner', 'Webb', 'Jacobs', 'Arnold', 'Reid', 'Hudson', 'Dunn', 'Nichols',
                  'Hoffman']

Last_names = ALL_Last_names[:names_to_added + 1]




while i < len(Last_names):
    last_n = Last_names[i]
    while True:

        try:
            driver.get('https://services.flhsmv.gov/crashreportpurchasing/crashreport/search')

            driver.find_element(By.CSS_SELECTOR, 'div[value="lastNameAndCrashDate"]').click()
            driver.find_element(By.CSS_SELECTOR, 'input[id="IsCrashDateTreatedAsRange"]').click()
            driver.find_element(By.CSS_SELECTOR, 'input[id="CrashDate"]').send_keys(DATE_)
            driver.find_element(By.CSS_SELECTOR, 'input[id="LastName"]').send_keys(last_n)
            driver.find_element(By.CSS_SELECTOR, 'input[id="CountyName"]').send_keys(COUNTY)
            # driver.find_element(By.CSS_SELECTOR,'input[id="CountyCode"]').click()
            # input("Press Enter To Pass....")

            # sleep(0.2)
            # Find an input field or element where you want to send the down arrow key
            input_element = driver.find_element(By.CSS_SELECTOR, 'input[id="CountyName"]')
            sleep(0.3)
            # Send the down arrow key
            input_element.send_keys(Keys.ARROW_DOWN)
            sleep(0.3)
            for mmm in range(5):
                input_element.send_keys(Keys.ENTER)
                # sleep(0.2)
            # Send the Tab key
            # sleep(0.5)
            input_element.send_keys(Keys.TAB)
            sleep(0.3)
            driver.implicitly_wait(1)
            print('------Waiting for the Captcha To be Filled------')
            while True:

                # Switch to the newly opened tab (index 1 in window_handles)
                driver.switch_to.window(driver.window_handles[0])

                # Find the element you want to capture (replace with your own locator)

                element = driver.find_element(By.CSS_SELECTOR, 'div[id="searchQueryCaptcha_CaptchaImageDiv"]')

                # Get the position and size of the element
                # location = element.location
                # size = element.size

                # Capture a screenshot of the entire page
                # screenshot = driver.get_screenshot_as_png()

                # Use PIL to crop the screenshot to the element
                # image = Image.open(BytesIO(screenshot))
                # cropped_image = image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))

                # Save the cropped image to a file
                # cropped_image.save("image11.png")

                # Get the element screenshot as a base64-encoded string
                element_screenshot = element.screenshot_as_base64

                # Convert base64 to image file (optional)
                with open("image11.png", "wb") as f:
                    f.write(base64.b64decode(element_screenshot))

                # Close the webdriver

                # Switch to the newly opened tab (index 1 in window_handles)
                driver.switch_to.window(driver.window_handles[0])


                # image_url=driver.find_element(By.CSS_SELECTOR,'img[id="searchQueryCaptcha_CaptchaImage"]').get_attribute('src')

                def solve(f):
                    with open(f, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode('ascii')
                        url = 'https://api.apitruecaptcha.org/one/gettext'

                        data = {
                            'userid': 'scholarpon@gmail.com',
                            'apikey': 'd9AAJFWfGT9iLMTHljk5',
                            'data': encoded_string
                        }
                        response = requests.post(url=url, json=data, timeout=30)
                        data = response.json()
                        return data


                S_code = solve('image11.png')['result']
                # S_code=result['code']
                
                driver.find_element(By.CSS_SELECTOR,'input[id="CaptchaCode"]').send_keys(S_code)
                sleep(0.2)
                WWW = 0
                driver.find_element(By.CSS_SELECTOR,'input[id="continueButton"]').click()

                print('#######')
                try:
                    driver.find_element(By.CSS_SELECTOR,'img[id="searchQueryCaptcha_CaptchaImage"]')
                    working = 1
                except:
                    working = 0
                if working == 0 or working == 1:
                    break

        except:
            WWW = 0
        try:
            driver.find_element(By.CSS_SELECTOR,'img[id="searchQueryCaptcha_CaptchaImage"]')
            WWW = 0
        except:
            WWW = 1
        if WWW == 1:
            break

    sleep(2)

    soup = BeautifulSoup(driver.page_source)
    for rnp in range(1):
        ROWS = soup.select('div[class="row border rounded"]')
        for row in ROWS:
            temp = {}
            try:
                tabs = row.select('div[class^="row"]')
                for tab in tabs:
                    KEY = tab.select_one('div[class^="col-"]').text.strip()
                    VALUE = tab.select_one('div[class^="col "]').text.strip()
                    if KEY != '':
                        temp[KEY] = VALUE




            except:
                pass
            rmpr.append(temp)
            print(temp)
    print('------------------------------   ', i)
    i = i + 1

# In[46]:


# Assuming you have a list of JSON data
json_data_list = rmpr

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(json_data_list)

# Specify the CSV file path
csv_file_path = 'output.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f'CSV file "{csv_file_path}" created successfully.')

# In[ ]: