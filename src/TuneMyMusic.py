from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv

URL = 'https://www.tunemymusic.com/transfer/text-file-to-amazon-music'

""" 
Params:
    xPath (string) - XPATH element to be selected and clicked
    driver (WebDriver): The Selenium WebDriver object used to control the Chrome browser.
    wait (WebDriverWait): The WebDriverWait object used to wait for elements to become clickable or visible before interacting with them.

summary:
    finds button, scrolls to it (just in case not in view), clicks it, and then waits a little for loading 
"""
def clickButton(xPath, wait, driver):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, xPath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", button) #scroll into view
    driver.execute_script("arguments[0].click();", button)
    time.sleep(1)

"""
Params:
    driver (WebDriver): The Selenium WebDriver object used to control the Chrome browser.
    wait (WebDriverWait): The WebDriverWait object used to wait for elements to become clickable or visible before interacting with them.

summary:
    signs into tune my music based off my credentials
"""
def sign_into_converter(driver, wait):

    # click login button
    clickButton("//a[text()='Login' and contains(@class, 'Fotter_FotterLink')]", wait, driver)

    #locate sign in fields
    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'Email')))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, 'Password')))

    # username and password from .env
    load_dotenv()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    #enter information 
    username_field.send_keys(username)
    password_field.send_keys(password)

    #pressing login button 
    clickButton("//button[text()='Login' and contains(@class, 'Login_MainBtn')]", wait, driver)

""" 
params:
    newSongsBool (bool) - determinate if any new songs were discovered
    AddedSongs_file (str) - location of newly added songs
    PLAYLIST_NAME (str) - name of playlist to be updated (MUST BE CREATED FIRST WITH ONE SONG)
    
summary:
    ENTRY POINT - ensures new songs were discovered
    connects to url via ignognito, hence no cookies are saved, and goes through the process of uploading the AddedSongs.txt file
    via signing into website and selecting correct playlist (PLAYLIST_NAME)
"""
def connecting_to_amazon_playlist(newSongsBool, AddedSongs_file, PLAYLIST_NAME):

    #checking if there are no songs to add
    if not newSongsBool:
        print("All songs played today are already added to the playlist")
        raise SystemExit()
    
    # add option for incognito so website never has cached info or anything
    options = Options()
    options.add_argument("--incognito")

    #opens website to read
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    #Allowing cookies (in the way of other elements)
    clickButton("//button[contains(@class, 'HeaderMenu_CookieAlertOK')]", wait, driver)

    # sign in 
    sign_into_converter(driver, wait)
    
    #choosing start button
    clickButton('//button[text()="Let\'s start"]', wait, driver)

    #choosing txt file convert type
    clickButton('//img[@alt="Upload file"]', wait, driver)

    # select file to upload
    file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    file_input.send_keys(AddedSongs_file)
    time.sleep(5) #make sure file has been parsed

    #choosing Destination
    clickButton('//button[contains(text(), "Choose Destination")]', wait, driver)

    # choose amazon music to convert to
    # ** need to already have amazon linked to tune my music webpage**
    clickButton("//img[@src='/images/platformsLogo/white/Amazon.svg']", wait, driver)

    #selecting EDIT to change playlist
    clickButton("//img[@alt='Edit Target Playlist'][@src='/images/pencil.svg']", wait, driver)

    #clicking drop down menu
    select_element = wait.until(EC.element_to_be_clickable((
        By.XPATH, "//select[contains(@class, 'targetPlaylistConfig_moveToSelect__')]"
    )))
    select = Select(select_element)
    select.select_by_value("MoveToExistingPlaylist")

    #selecting the playlist
    clickButton(f"//span[text()='{PLAYLIST_NAME}']", wait, driver)

    #click save button
    clickButton('//button[contains(text(), "Save")]', wait, driver)

    #click transfer
    clickButton('//button[contains(text(), "Start Transfer")]', wait, driver)

    #closing site once its done transfering by waiting til the continue button appears (5 min limit)
    WebDriverWait(driver, 300).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(), "Transfer completed")]'))
    )
    driver.quit()

