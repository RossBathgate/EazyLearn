""" Eazy to make, eazy to learn """
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

USERNAME = "s2187089"
PASSWORD = "hellothere"
DRIVER_PATH = "./drivers/chromedriver.exe"
MYED_LOGIN_URL = "https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F"
REACT_PATH = "./ui.js"
CREDENTIALS_PATH = "credentials.txt"
VISIBLE_COURSES_PATH = "course_links.txt"
REACT_WINDOW_OBJECT = "visibleCourses"
REACT_HTML_STRUCTURE = """
<html>
  <head>
    <title>EazyLearn</title>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""

def main():
  # Login
  try:
    username, password = getLoginDetails(CREDENTIALS_PATH)
  except:
    print("Login failed.")
    return

  # Open Selenium
  driver = webdriver.Chrome(DRIVER_PATH)
  driver.get(MYED_LOGIN_URL)

  # Login in Selenium
  login(driver, username, password)
  
  # Get visible courses
  visibleCourses = readVisibleCourses(VISIBLE_COURSES_PATH)
  if not visibleCourses:
    courseLinks = getCourseLinks(driver)
    visibleCourses = chooseVisibleCourses(courseLinks)
    saveVisibleCourses(visibleCourses, VISIBLE_COURSES_PATH)

  # Start React
  injectReact(driver, visibleCourses, REACT_PATH)
  

def createFileIfNotExists(filepath):
  try:
    file = open(filepath, "r+")
    file.close()
  except:
    file = open(filepath, "w+")
    file.close()


def getLoginDetails(loginFilepath):
  """ Asks for login details """
  createFileIfNotExists(loginFilepath)

  with open(loginFilepath, "r+") as file:
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
  sleep(10)

  # Extract courses from page
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


def readVisibleCourses(filepath):
  """ Reads visible courses from a file """
  createFileIfNotExists(filepath)
  visibleCourses = None

  with open(filepath, "r") as coursesFile:
    lines = coursesFile.read().splitlines()
    if (len(lines) > 1):
      # Course choices from file
      visibleCourses = {}
      for line in lines:
        courseName, courseLink = line.split(",")
        visibleCourses[courseName] = courseLink

  return visibleCourses


def saveVisibleCourses(visibleCourses, filepath):
  """ Stores the visible courses to a file """
  with open(filepath, "w") as coursesFile:
    outputLines = "\n".join(["%s,%s" % courseDetails for courseDetails in visibleCourses.items()])
    coursesFile.seek(0)
    coursesFile.write(outputLines)


def injectReact(driver, visibleCourses, reactPath):
  """ Replaces html code with React """
  # [{title: link: }]
  # Convert visible courses to json
  formattedCourses = [{"title": courseName, "link": courseLink} for (courseName, courseLink) in visibleCourses.items()]
  visibleCoursesJson = json.dumps(formattedCourses)

  # Inject react code
  driver.execute_script("document.body.innerHTML = `%s`; window.%s = %s"
                        % (REACT_HTML_STRUCTURE, REACT_WINDOW_OBJECT, visibleCoursesJson))

  with open(reactPath, "r") as reactFile:
    reactScript = reactFile.read() 
    driver.execute_script(reactScript)

  sleep(10)


# Starts the program
if __name__ == '__main__':
  main()