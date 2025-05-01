from selenium import webdriver
from bs4 import BeautifulSoup
import src.utils.Time as Time
import time
import re

URL = 'https://957benfm.com/stream/wbenfm/'

""" 
params:
    url (string) - webpages url to connect to

summary:
    connects to url and gets all of the text on the page. If any errors occurs quit program and output error

returns:
    (string) - the text from the url 

"""
def get_page_text(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        time.sleep(3)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup.get_text()
    
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Closing program!")
        raise SystemExit()

    finally:
        driver.quit()

"""
summary:
    gets text and parses to just have the songs played that given day. 

returns: 
    listOfSongs (list) - all songs played that day 
"""        
def get_songs_from_BenFM():

    text = get_page_text(URL)

    #uses current day to get all songs from that day
    date = Time.date
    date1 = Time.month

    # parsing data specifically for BenFM
    parts_after_first_date = text.split(date)
    section_after_first_date = parts_after_first_date[1]
    parts_before_second_date = section_after_first_date.split(date1)
    text_between_dates = parts_before_second_date[0].strip()
    final_values = text_between_dates.split(":")

    #creating list
    pattern = re.compile(r'\d+$') #pattern for digits at end (1 or more)
    listOfSongs = []
    for i in final_values:
        val = i[6:] #removes date
        val = val.lstrip(" -")
        val = val.replace('\u2014', 'by') # - via code (glitchy with using '-')
        val = re.sub(pattern, '', val)
        listOfSongs.append(val)
        
    #edit list to remove first last (formatting)
    listOfSongs.pop(0)
    listOfSongs.pop()

    return listOfSongs

if __name__ == "__main__":
    songs = get_songs_from_BenFM()
