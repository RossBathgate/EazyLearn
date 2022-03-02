""" Eazy to make, eazy to learn """

from selenium import webdriver
from time import sleep

USERNAME = "s2187089"
PASSWORD = "hellothere"
DRIVER_PATH = "./drivers/chromedriver.exe"
MYED_LOGIN_URL = "https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F"
REACT_PATH = "./react/script.js" ### TBC

def main():
  # Open Selenium
  # driver = webdriver.Chrome(DRIVER_PATH)
  # driver.get(MYED_LOGIN_URL)

  # Login
  try:
    username, password = getLoginDetails()
    print(username, password)
    return


    login(driver, username, password)
  except:
    print("Login failed.")
    return
  
  # Process page
  courseLinks = getCourseLinks(driver)
  visibleCourses = chooseVisibleCourses(courseLinks)
  injectReact(driver, visibleCourses, REACT_PATH)
  

def getLoginDetails(file="credentials.txt"):
  """ Asks for login details """

  with open("credentials.txt", "r+") as file:
    contents = file.read().splitlines()

    if (len(contents) > 1):
      username, password = contents[0], contents[1]
    else:
      # Prompts for username and password if none have been saved
      print("Well Hello There!  We are glad you have chosen EazyLearn!")
      username = input("Enter myed username:\t")
      password = input("Enter myed password:\t")
      
      # Overwrite the file with new credentials
      file.seek(0)
      file.write(username+"\n"+password)
      file.truncate()

  return username, password


def login(driver, username, password):
  """ Automates the login process through myed """
  pass


def getCourseLinks(driver):
  """ Returns a dictionary {courseName: url} """
  pass


def chooseVisibleCourses(courseLinks):
  """ Prompt to choose visible courses """
  pass


def injectReact(driver, reactPath):
  """ Replaces html code with React """
  pass


# Starts the program
if __name__ == '__main__':
  main()