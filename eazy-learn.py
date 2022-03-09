""" Eazy to make, eazy to learn """
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

USERNAME = "s2187089"
PASSWORD = "hellothere"
DRIVER_PATH = "./drivers/chromedriver.exe"
MYED_LOGIN_URL = "https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F"
REACT_PATH = "./react/script.js" ### TBC

def main():
  # Login
  try:
    username, password = getLoginDetails()
  except:
    print("Login failed.")
    return

  # Open Selenium
  driver = webdriver.Chrome(DRIVER_PATH)
  driver.get(MYED_LOGIN_URL)

  # Login in Selenium
  login(driver, username, password)
  
  # Process page
  courseLinks = getCourseLinks(driver)
  visibleCourses = chooseVisibleCourses(courseLinks)
  injectReact(driver, visibleCourses, REACT_PATH)
  

def getLoginDetails(file="credentials.txt"):
  """ Asks for login details """

  # Gets username and password
  try:
    file = open("credentials.txt", "r+")
    file.close()
  except:
    file = open("credentials.txt", "w+")
    file.close()

  with open("credentials.txt", "r+") as file:
    contents = file.read().splitlines()

    if (len(contents) > 1):
      username, password = contents[0], contents[1]
    else:
      # Prompts for username and password if none are saved
      print("Well Hello There!  We are glad you have chosen EazyLearn!")
      username = input("Enter myed username:\t")
      password = input("Enter myed password:\t")
      
      # Write new credentials to file
      file.seek(0)
      file.write(username+"\n"+password)
      file.truncate()

  return username, password

def login(driver, username, password):
  """ Automates the login process through myed """
  # Fill username
  usernameInput = driver.find_element(By.ID, "login")
  usernameInput.send_keys(username + "\n")

  # Fill password
  passwordInput = driver.find_element(By.ID, "password")
  passwordInput.send_keys(password + "\n")

def getCourseLinks(driver):
  """ Returns a dictionary {courseName: url} """
  sleep(2)

  # generate the dictionary
  linkElementsContainer = driver.find_elements(By.CLASS_NAME, 'list-group')
  linkElementsLI = linkElementsContainer[0].find_elements(By.CLASS_NAME, 'list-group-item')
  courseInfo = [(LI.find_element(By.TAG_NAME, 'a').get_attribute('innerHTML'), LI.find_element(By.TAG_NAME, 'a').get_attribute('href')) for LI in linkElementsLI]
  courseDict = {}
  
  for course in courseInfo:
    name,link = course
    courseDict[name] = link

  return courseDict


def chooseVisibleCourses(courseLinks):
  """ Prompt to choose visible courses """
  # Display courses
  index = 0
  for courseName in courseLinks.keys():
    print("%d) %s" % (index, courseName))
    index += 1
  
  # Choose courses
  inputStr = input("Choose courses:")
  allChoices = dict(zip(range(index), courseLinks.keys()))
  choicesNames = [allChoices[int(num)] for num in inputStr.split()]
  choicesDict = {name: courseLinks[name] for name in choicesNames}
  return choicesDict

def injectReact(driver, visibleCourses, reactPath):
  """ Replaces html code with React """
  driver.execute_script("document.body.innerHTML = '<p>%s</p>';" % "I am going to the toilet.")
  # driver.execute_script("alert('I am going to the toilet.');")
  sleep(10)
  pass


# Starts the program
if __name__ == '__main__':
  main()