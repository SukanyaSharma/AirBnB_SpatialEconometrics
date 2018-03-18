import csv
import urllib
import unicodedata

##http://scraping.pro/using-selenium-webdriver-for-website-scraping/
import selenium
from selenium import webdriver
##import selenium.webdriver.chrome.webdriver

##http://stackoverflow.com/questions/18624888/selenium-python-closing-alert-window-in-chrome
import selenium.webdriver.common.alert
##from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException

import time
##import random


ids = []
blkgrp =[]
addresses = []

with open("./Dataset_MAIN/School_District_Quality/CT_Centroid_outcome_missing.csv") as inputfile:
    next(inputfile)
    inputread = csv.reader(inputfile, delimiter=',')
    for row in inputread:
        ids.append(row[0])
        blkgrp.append(row[0])
        addresses.append(row[1])

driver = webdriver.Chrome(executable_path = "chromedriver")
##myfile=open('M:/Millennial_CA/21_RC_LCCM/03_data_process/07_Python/Bak_greatschools/greatschools_elem_run4.csv', 'wt')
myfile=open('./Dataset_MAIN/School_District_Quality/School_outcome4.csv', 'wt')
##myfile=open('M:/Millennial_CA/21_RC_LCCM/03_data_process/07_Python/Bak_greatschools/greatschools_high.csv', 'wt')
outputfile = csv.writer(myfile, delimiter=',', lineterminator='\n')
outputfile.writerow(["id", "stcnttr", "name", "addr", "level", "dist", "score"])

for i in range(109, 868):  
    scores = []
    scores.append(ids[i])
    scores.append(blkgrp[i])
    #scores.append(addresses[i])
    driver.get("https://www.greatschools.org/")
    try:
        elem=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div[2]/div/div[2]/div[2]/form/div/span/input[2]")
        elem.clear()
        elem.send_keys(addresses[i])
        elem.send_keys(Keys.RETURN)
        ##http://selenium-python.readthedocs.io/waits.html
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "js-numOfSchoolsFound"))
            )
            ##driver.set_page_load_timeout(3)
            ##http://stackoverflow.com/questions/32276654/setting-page-load-timeout-in-selenium-python-binding
            ##time.sleep(random.uniform(3.0, 9.0))
            ##http://stackoverflow.com/questions/15985339/how-do-i-get-current-url-in-selenium-webdriver-2-python
            ##URL = driver.current_url
            ##print (URL)
        except TimeoutException as e:
            print(e)
            a = ['TimeoutException', 0, 0, 0, 0]
            scores.extend(a)
            print(scores)
            outputfile.writerow(scores)
            myfile.flush()
            del scores[2:7]
            driver.close()
            time.sleep(5)
            driver = webdriver.Chrome(executable_path="chromedriver")
            driver.get("https://www.greatschools.org/")
            #elem=driver.find_element_by_xpath("//body/div[6]/div/div/div[2]/div/div/div/form/div/span/input[2]")
            #elem.clear()
            #elem.send_keys(addresses[i])
            #elem.send_keys(Keys.RETURN)
        finally:
            ##try:
            ##    time.sleep(2)
            ##    a = driver.find_element_by_id("js-assigned-school-elementary").text.split('\n')
            ##    #a = driver.find_element_by_id("js-assigned-school-middle").text.split('\n')
            ##    #a = driver.find_element_by_id("js-assigned-school-high").text.split('\n')
            ##    a2 = [a[2], a[3], a[7], a[8], a[9]]
            ##    scores.extend(a2)
            ##    print(scores)
            ##    outputfile.writerow(scores)
            ##    myfile.flush()
            ##    del scores[2:7]
            ##except IndexError as e:
            try:
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div[1]").click() # Refine Search
                #driver.find_element_by_xpath("//body/div[6]/div[2]/div[3]/div/div/div/div[2]/div[2]/div/form/div/div/div[3]/div[2]/label").click() # elementary
                #driver.find_element_by_xpath("//body/div[6]/div[2]/div[3]/div/div/div/div[2]/div[2]/div/form/div/div/div[3]/div[3]/label").click() # middle
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/form/div/div[1]/div[3]/div[4]/label").click() # high
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/form/div/div[3]/div[3]/div[1]/label").click() # public district
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/button").click() # Submit
                time.sleep(2)
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/button").click() # open the dropdown menu
                driver.find_element_by_xpath("/html/body/div[6]/div[2]/div[3]/div/div/div[2]/div[1]/div/div/ul/li[1]/a/span[1]").click() # click Sort by distance
                items = driver.find_elements_by_xpath("//div[@class='pvm gs-bootstrap js-schoolSearchResult js-schoolSearchResultCompareErrorMessage']")
                time.sleep(2)
                for i in range(0, len(items)):
                    row = []
                    row.extend(items[i].text.split('\n'))
                    scores.extend([row[0], row[1], row[5], row[6], row[7]])
                    print(scores)
                    outputfile.writerow(scores)
                    myfile.flush()
                    del scores[2:7]
            # if pop-up appears (survey), clicking is not possible -> produces an IndexError.
            except IndexError as e:
                print (e)
                a = ['IndexError', 0, 0, 0, 0]
                scores.extend(a)
                print(scores)
                outputfile.writerow(scores)
                myfile.flush()
                del scores[2:7]
            except NoSuchElementException as e:
                print(e)
                a = ['NoSuchElementException', 0, 0, 0, 0]
                scores.extend(a)
                print(scores)
                outputfile.writerow(scores)
                myfile.flush()
                del scores[2:7]
            except WebDriverException as e:
                print (e)
                a = ['WebDriverException', 0, 0, 0, 0]
                scores.extend(a)
                print(scores)
                outputfile.writerow(scores)
                myfile.flush()
                del scores[2:7]
    except NoSuchElementException as e:
        print(e)
        a = ['NoSuchElementException', 0, 0, 0, 0]
        scores.extend(a)
        print(scores)
        outputfile.writerow(scores)
        myfile.flush()
        del scores[2:7]
    except StaleElementReferenceException as e:
        print(e)
        a = ['StaleElementReferenceException', 0, 0, 0, 0]
        scores.extend(a)
        print(scores)
        outputfile.writerow(scores)
        myfile.flush()
        del scores[2:7]
        driver.close()
        time.sleep(90)
        driver = webdriver.Chrome(executable_path="chromedriver")
        driver.get("https://www.greatschools.org/")
    except UnexpectedAlertPresentException as e:
        print(e)
        ##http://stackoverflow.com/questions/28397370/python-selenium-unexpectedalertpresentexception
        ##http://stackoverflow.com/questions/19003003/check-if-any-alert-exists-using-selenium-with-python
        ##driver.find_elements_by_link_text("OK").click()
        a = ['UnexpectedAlertPresentException', 0, 0, 0, 0]
        scores.extend(a)
        print(scores)
        outputfile.writerow(scores)
        myfile.flush()
        del scores[2:7]
        alert = driver.switch_to_alert()
        alert.accept()
    except StaleElementReferenceException as e:
        print(e)
        a = ['StaleElementReferenceException', 0, 0, 0, 0]
        scores.extend(a)
        print(scores)
        outputfile.writerow(scores)
        myfile.flush()
        del scores[2:7]
        driver.close()
        time.sleep(90)
        driver = webdriver.Chrome(executable_path="chromedriver")
        driver.get("https://www.greatschools.org/")
    except NoSuchElementException as e:
        print(e)
        a = ['NoSuchElementException', 0, 0, 0, 0]
        scores.extend(a)
        print(scores)
        outputfile.writerow(scores)
        myfile.flush()
        del scores[2:7]
##getscore(addr_actual, "js-assigned-school-middle", "//body/div[6]/div[2]/div[3]/div/div/div/div[2]/div[2]/div/form/div/div/div[3]/div[3]/label")
##getscore(addr_actual, "js-assigned-school-high", "//body/div[6]/div[2]/div[3]/div/div/div/div[2]/div[2]/div/form/div/div/div[3]/div[4]/label")

myfile.close()
driver.close()
