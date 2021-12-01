"""
WA module for scrapping and processing text from https://leg.wa.gov 

# Status

Current Coverage:
    [X] Committee Hearings (Audio Links) (2015 - 2020)

Planned Coverage:
    [ ] Committee Hearings (Video Links) (2000 - 2014)
    [ ] Floor Speeches (Video Links)

# WA Work Flow

CLASS WAScrape

    - wa_scrape_meeting_links by desired committee and legislative session. 
    Function searches TVW archives for links to each individual committee meeting for that leg session
    
    - wa_scrape_audio by wa_meeting_links output
    Function visits each link individually and gather weblinks for each meeting hearing audio by mp3 link on page
    
    -wa_scrape_download_audio by wa_scrape_audio output
    Function gives the user option to download all mp3 locally
    Pulls input by wa_scrape_audio for the weblinks by desired committee and leg session
    Rename the file names by committee name and date (YYYYMMDD) (e.g. wa_education_20200305.mp3)

CLASS WAProcess

    - wa_speech_to_text
    Function gives the user option to convert audio file to a text transcript through DeepSpeech
    Uses mp3 links directly to process the transcripts
    Downloads the transcript in json form, single json for each committee/legislative session
    
    - wa_text_clean
    Function conducts tests and run light cleaning to ensure transcript is ready for text analysis

"""

import os
from pathlib import Path
import sys
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC



def wa_meeting_links():

  """
  """
  
# DRIVER SETUP
service = Service("/Users/katherinechang/Google Drive/My Drive/2021/Fall 2021/CSE583/project/chromedriver_64")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# OPEN TO TVW ARCHIVES 
driver.get("https://www.tvw.org/archives/")

# ENTER SPECIFIC COMMITTEE NAME AND PRESS ENTER 

"""
input_search = driver.find_element(By.ID, "invintus-archives-search")
input_search.send_keys("House Education Committee")
input_search.send_keys(Keys.RETURN)
"""

# SELECT CATEGORY LEGISLATIVE

#driver.find_element(By.CLASS_NAME, "selectric-invintus-archives-filter-category").click()
#driver.find_element(By.CLASS_NAME, "selectric-hide-select").click()

dropdown_category=driver.find_element(By.CLASS_NAME, "invintus-archives-filter-category")

dropdown_category_select=Select(dropdown_category)

dropdown_category_select.select_by_index(2)

dropdown_category_select.select_by_visible_("Well Read")


selectric_option=driver.find_element(By.CLASS_NAME, "selectric")
print(selectric_option)

selectric_option.get_attribute('innerHTML')

selectric_option.get_attribute('innerHTML') 

# write script
script =  '<p class="label">Legislative</p><b class="button">▾</b>'
  
# generate a alert via javascript
selectric_option.execute_script(script)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("URL")
time.sleep(5)

Para_Element = driver.find_element_by_id("myP")
print(selectric_option.text)
# driver.execute_script("var ele=arguments[0]; ele.innerHTML = 'Successfully Changed the Content';", Para_Element)

driver.execute_script(script)
element = driver.find_element_by_tag_name("a")
driver.execute_script("arguments[0].setAttribute('href', 'https://www.google.com/')", element)
driver.execute_script("var ele=arguments[0]; ele.innerHTML = 'Google';", element)

Para_Element = driver.find_element_by_id("myP")
print(Para_Element.text)


####

options = [x for x in selectric_option.find_elements_by_tag_name("option")]

for element in options:
    print(element.get_attribute("value"))
    
dropdown_category.select_by_visible_text("Well Read")
    
options
    
.click()

print(dropdown_category_select)

#####


options = driver.find_elements(By.TAG_NAME, "option")

for each_option in dropdown_category:
    #print(each_option)
    print(each_option.get_attribute("value"))
    

for each_option in options:
    if (each_option.get_attribute("value")=="Agencies and Boards"):
        y=each_option
        break


# SELECT START DATE BY LEGISLATIVE SESSION
select_date_start = driver.find_element(By.CLASS_NAME, "invintus-archives-filter-start-date")
select_date_start.click()


for option in selectMonth.find_elements_by_tag_name('option'):
    if option.text == 'Mar':
        option.click() 
        break


for option in selectYear.find_elements_by_tag_name('option'):
    if option.text == '2017':
        option.click() 
        break 

days = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
days[4].click()


# SELECT END DATE BY LEGISLATIVE SESSION
select_date_end = driver.find_element(By.CLASS_NAME, "invintus-archives-filter-end-date")
select_date_end.click()

# INPUT COMMITTEE MEETING





# SAVE LINKS FOR MULTIPLE PAGES

url = driver.page_source

# FOR EACH PAGE SEARCH FOR A HREF TAG TO CREATE A LIST OF WEBLINKS

match = re.search(r'href=[\'"]?([^\'" >]+)', lines)



for i in lines:
    hit = meeting_regex.findall(l)


REGEX_PATTERN = r".*(\?eventID\=).*"
lines = url.split()
meeting_regex = re.compile(REGEX_PATTERN)
all_files = []

for l in lines:
    hit = meeting_regex.findall(l)
    if hit:
        print(hit)
        #all_files.extend(hit)
        
for filename in all_files:
    print(filename)



<a href="/watch/?eventID=2021111051">



# GO THROUGH EACH PAGE AND GATHER THE LINKS TO EACH MEETING






driver.close()


def wa_scrape_audio():

  """
    Webscrape function for Washington State Legislature Website for 2016-2020 sessions 
    
    Parameters
    ----------
    webscrape_links : LIST
        List of direct link(s) to WA committee video pages.
        Can also use list generated by wa_committee_links() 
    dir_chrome_webdriver : STRING
        Local directory that has Chrome Webdriver.
    dir_save : STRING
        Local directory to save audio files

    Returns
    -------
    All audio files found on the webscrape_links, saved on local dir_save.
    
    """

service = Service("/Users/katherinechang/Google Drive/My Drive/2021/Fall 2021/CSE583/project/chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.tvw.org/watch/?eventID=2021021259") 

arrow01 = driver.find_element(By.ID, 'content')
arrow01.click()

#arrow02 = driver.find_element(By.CLASS_NAME, 'interior_container')
#arrow02.click()
#arrow02 = driver.find_element(By.CLASS_NAME, 'invintus-player')
#arrow02.click()
#arrow02 = driver.find_element(By.CLASS_NAME, 'inv-underlay--actions')
#arrow02.click()

url = driver.page_source
REGEX_PATTERN = r'https.*audio.*\.mp3'
lines = url.split()
meeting_regex = re.compile(REGEX_PATTERN)
mp3_files = []

for l in lines:
    hit = meeting_regex.findall(l)
    if hit:
        mp3_files.extend(hit)
        
for filename in mp3_files:
    print(filename)
    
driver.close()



"""
https://invintus-client-media.s3.amazonaws.com/9375922947/bb61b863f2ace56a560d401f1deebfc17ec0201c_audio.mp3
https://invintus-client-media.s3.amazonaws.com/9375922947/071722fb938c8e0a87505936941971725631c303_audio.mp3

NOTES:
    Audio download button available until 2016. 2015 and previous years will require video links (mp4)
"""