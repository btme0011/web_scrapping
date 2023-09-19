# Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222  -> run this command to open chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 0

def sendMessage(companyName):
    dilogBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'artdeco-modal-outlet')]"))
    )

    # Wait for the "Add a note" button inside the dialog box to become clickable
    buttonAddANote = WebDriverWait(dilogBox, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//span[contains(., 'Add a note')]"))
    )

    # Click on the "Add a note" button
    buttonAddANote.click()

    # Wait for the textarea element with the name attribute containing "message" to become present
    text_area_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[contains(@name, 'message')]"))
    )

    # Clear any existing text in the textarea (optional)
    text_area_element.clear()

    # Write text into the textarea
    text_to_write = """Hello, I am Akhil Anand, currently a software developer at Amazon. I've found {company} to be a great company that sparked my interest. I believe that connecting with you would enrich my professional network. Thank you for considering my connection request""".format(company=companyName)
    text_area_element.send_keys(text_to_write)

    time.sleep(3);
    buttonSendNow = WebDriverWait(dilogBox, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[contains(., 'Send')]"))
    )
    buttonSendNow.click();


    # code of pyautogui
    # print("entered sendMessage")
    # time.sleep(5)
    # for i in range(2):
    #     print("Pressing tab")
    #     pyautogui.hotkey('tab')
    #     time.sleep(1)

    # print("Pressing enter")
    # pyautogui.hotkey('enter')
    # time.sleep(5)

    # print("Making Message Text")
    # body_text = """Hello, I am Akhil Anand, currently a software developer at Amazon. I've found {company} to be a great company that sparked my interest. I believe that connecting with you would enrich my professional network. Thank you for considering my connection request""".format(company=companyName)
    # print("Writing Text")
    # pyautogui.write(body_text)

    # time.sleep(15)
    # for i in range(2):
    #     print("Pressing Tab")
    #     pyautogui.hotkey('tab')
    #     time.sleep(1)

    print("Increasing count by 1")
    global count
    count = count + 1;


companyName = "CitizenGo"
positionOfCompany = 1
delay = 2
iteration = 50

link = 'https://www.linkedin.com/'

# Setup Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Setup Webdriver with the service and options
webdriver_service = Service(executable_path="/path/to/chromedriver")
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# rest of your code with added WebDriverWait
print("Opening Linkedin")
driver.get(link)

print("Finding The SearchBox")
search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-global-typeahead__input")))  # Class name of LinkedIn's search box

# ...previous code...

# Use WebDriverWait to wait until the search box is interactable, then send keys
search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-global-typeahead__input")))
print("Writing company Name to Search Box")
search_box.send_keys(companyName)
search_box.send_keys(Keys.RETURN) 

# Wait until the Companies button is interactable, then click it
print("Clicking on the Companies button")
Companies = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'artdeco-pill') and contains(@class, 'artdeco-pill--slate') and contains(@class, 'artdeco-pill--choice') and contains(@class, 'artdeco-pill--2') and contains(@class, 'search-reusables__filter-pill-button') and contains(.,'Companies')]")))

try:
    Companies.click()
except:
    raise Exception("Clicking on the Companies Failed")

# Wait until the li in the first ul at the specified index is interactable, then click it
print("Click on the Position of company")
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='search-results-container']/div")))
divs = driver.find_elements(By.XPATH, "//div[@class='search-results-container']/div")
divThatContainTheList = divs[1]

WebDriverWait(divThatContainTheList, 10).until(EC.presence_of_element_located((By.XPATH, ".//ul[contains(@class,'reusable-search__entity-result-list') and contains(@class, 'list-style-none')]")))
first_ul = divThatContainTheList.find_element(By.XPATH, ".//ul[contains(@class,'reusable-search__entity-result-list') and contains(@class, 'list-style-none')]")
print(first_ul.get_attribute('class'))

li_in_first_ul = first_ul.find_element(By.XPATH, f"./li[{positionOfCompany}]")

WebDriverWait(li_in_first_ul, 10).until(EC.presence_of_element_located((By.XPATH, ".//div[contains(@class,'entity-result')]")))
finalResult = li_in_first_ul.find_element(By.XPATH, ".//div[contains(@class,'entity-result')]")

try:
    print(finalResult.get_attribute('class'))
    final_link = WebDriverWait(finalResult, 10).until(EC.presence_of_element_located((By.XPATH, ".//a[@href]")))
    print(final_link.get_attribute('href'))
    driver.get(final_link.get_attribute('href'))
except:
    raise Exception("Clicking on the required company failed")



# select people option
print("Click on the People Option")
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='org-page-navigation__items ']")))
ulOptionsPeople = driver.find_element(By.XPATH, "//ul[@class='org-page-navigation__items ']")

peopleButton = WebDriverWait(ulOptionsPeople, 15).until(EC.presence_of_element_located((By.XPATH, "./li[contains(.,'People')]")))
try:
    peopleButton.click()
except:
    raise Exception("Clicking on the people button of the company failed")


# open all the people and write a message to them and connect
for i in range(iteration):
    time.sleep(5)
    print("Scrolling window")
    driver.execute_script("window.scrollBy(0, 1000)")

print("Collection all the list of people")
peopleUl = driver.find_element(By.XPATH, "//ul[contains(@class, 'display-flex') and contains(@class, 'list-style-none') and contains(@class, 'flex-wrap')]")
list_items = WebDriverWait(peopleUl, 5).until(EC.presence_of_all_elements_located((By.XPATH, "./li")))


original_window = driver.current_window_handle
urlList = []
print("Adding all the people url to urlList")
for item in list_items:
    try:
        itemAnchor = item.find_element(By.XPATH, ".//a[@href]")
    except:
        continue
    url = itemAnchor.get_attribute('href')
    urlList.append(url)

print("Iterating over the url list")
for urlLink in urlList:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))
    print("click on the link")
    driver.get(urlLink)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

    #connect
    #picking up the Second connect on the every page might change it later
    try :
        print("try to find the connect button")
        section_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'artdeco-card') and contains(@class, 'ember-view') and contains(@class, 'pv-top-card')]")))
        buttonConnect = WebDriverWait(section_element, 1).until(EC.presence_of_element_located((By.XPATH, ".//span[contains(., 'Connect')]")))
        buttonConnect.click()
        WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//body")))
        print("Try to send message")
        sendMessage(companyName);
    except Exception as e :
        print("Failed to find the connect button:", e)
        try :
            print("Try to click on More and find the connect button")
            section_element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'artdeco-card') and contains(@class, 'ember-view') and contains(@class, 'pv-top-card')]")))
            buttonMore = WebDriverWait(section_element, 1).until(EC.presence_of_element_located((By.XPATH, ".//span[contains(.,'More')]")))
            buttonMore.click()
            # if connection is already there then continue
            try :
                print("Already Following")
                buttonRemoveConnection = WebDriverWait(section_element, 1).until(EC.element_to_be_clickable((By.XPATH, ".//span[contains(., 'Remove Connection')]")))
            except :
                buttonConnect = WebDriverWait(section_element, 1).until(EC.element_to_be_clickable((By.XPATH, ".//span[contains(., 'Connect')]")))
                buttonConnect.click()
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//body")))
                print("Try to send message")
                sendMessage(companyName);
        except Exception as e :
            print("Failed to find the connect button even after clicking on the More button:", e)
            continue
        continue


print(count)
print(len(urlList))
