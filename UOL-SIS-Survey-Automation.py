from selenium import webdriver
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import  Keys
import time
import os, sys

# Testing chrome driver with path
# Old Code for Chrome
"""
 driver = webdriver.Chrome('C:/driver/chromedriver.exe')
"""


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.minimize_window()
# Program main code here
print("Wait for 5 Second Please: UOL Server is Busy")
time.sleep(5)
clears = lambda: os.system('cls')
clears()
print("UOL SIS Survey", "Automation", "By Hamza Haroon")
print("Downlaod from Github:", "http://bit.ly/UOL-SIS-Automation", "By Mr.HaaMoo")
print("Source code Available on Github")
print("---------------START PROGRAM---------------")
print("---------------Select Your Favorite Option---------------")
print("Program Sleep for 2 Sec...")
time.sleep(2)

METHOD = input("WANT TO USE LOGIN METHOD? (Y/N): ")
if METHOD == 'y' or METHOD == 'YES' or METHOD == 'Y' or METHOD == 'yes':
    sisurl = 'http://sis.uol.edu.pk/sis/MainForms/login.aspx'
    driver.get(sisurl)
    USERNAME = input('Enter User-Name: ')
    PASSWORD = input("Enter Password: ")
    NEUTRAl = input("Comment for Survey: ")
    if NEUTRAl == "":
        print("Comment is Must:")
        time.sleep(2)
        driver.quit()
        sys.exit()

    User_input = driver.find_element_by_xpath('//*[@id="txtUserName"]')
    User_input.send_keys(USERNAME)

    Passcode_input = driver.find_element_by_xpath('//*[@id="txtPassword"]')
    Passcode_input.send_keys(PASSWORD)

    login_button = driver.find_element_by_xpath('//*[@id="Button1"]')
    login_button.click()
    print("Program Sleep for 5 Sec...")
    driver.maximize_window()
    driver.minimize_window()
    time.sleep(5)
    curl = driver.current_url
    if curl == "http://sis.uol.edu.pk/sis/MainForms/MainForm.aspx":
        driver.quit()
        sys.exit()

else:
    print("---------------PUT URL (Example:http://survey.uol.edu.pk/survey/account/userprofile.aspx?key=xxxx)---------------")
    url = input("Enter URL Here: ")
    NEUTRAl = input("Comment for Survey: ")
    if NEUTRAl == "":
        print("Comment is Must:")
        time.sleep(2)
        driver.quit()
        sys.exit()
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)


def stepscomplete():
    # Start Completing Steps
    time.sleep(2)
    steps1_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StartNavigationTemplateContainerID_StartNextButton"]').click()
    print("Step No.01 Completed")
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q245_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q246_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q247_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q248_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.02 Completed")
    time.sleep(2)
####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q249_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q250_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q251_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q252_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.03 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q253_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q254_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q255_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q256_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q257_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.04 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q311_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q312_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q313_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q314_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q315_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.05 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q258_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q259_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q260_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q261_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.06 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q262_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q263_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q264_rb3"]').click()
    Comments_Box = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q265_txtAnswer"]')
    Comments_Box.send_keys(NEUTRAl)
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.07 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q266_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q267_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q268_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q269_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.08 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q292_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q293_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q294_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.09 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q270_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q271_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.10 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q272_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q273_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.11 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q274_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q275_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q276_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q277_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q278_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q279_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q280_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q281_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q282_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q283_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q284_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q285_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q286_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_StepNavigationTemplateContainerID_StepNextButton"]').click()
    print("Step No.12 Completed")
    time.sleep(2)

####################
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q287_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q288_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q289_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q290_rb3"]').click()
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_Q291_rb3"]').click()
    step2_next = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_Wizard1_FinishNavigationTemplateContainerID_FinishButton"]').click()
    print("Step No.13 Completed")
    time.sleep(2)

    # Steps Completed

#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
#_________________________________________STEPS FUNCTION END HERE____________________________________________#


#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 1st Subject
print("---------------1st Subject---------------")
Subject1 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[2]/td[6]').text
print("Subject No.1 "+str(Subject1))
time.sleep(1)
while Subject1 != 'Completed':
    driver.find_element_by_xpath("//*[@id='mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_0']").click()
    # Function of Steps
    stepscomplete()
    time.sleep(2)
    Subject1 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[2]/td[6]').text
    print("Subject No.1 "+str(Subject1))
    time.sleep(2)
    # Subject 1 Completed
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#



#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 2nd Subject Start

print("---------------2nd Subject---------------")
Subject2 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[3]/td[6]').text
print("Subject No.2 "+str(Subject2))
time.sleep(1)

while Subject2 != 'Completed':
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_1"]').click()

    # Function of Steps
    stepscomplete()

    time.sleep(2)
    Subject2 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[3]/td[6]').text
    print("Subject No.2 " + str(Subject2))
    time.sleep(2)



# Subject 2 Completed
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#




#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 3rd Subject Start

print("---------------3rd Subject---------------")
Subject3 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[4]/td[6]').text
print("Subject No.3 " + str(Subject3))
time.sleep(1)

while Subject3 != 'Completed':
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_2"]').click()

    # Function of Steps
    stepscomplete()

    time.sleep(2)
    Subject3 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[4]/td[6]').text
    print("Subject No.3 " + str(Subject3))
    time.sleep(2)

# Subject 3 Completed
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#





#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 4th Subject Start

print("---------------4th Subject---------------")
Subject4 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[5]/td[6]').text
print("Subject No.4 " + str(Subject4))
time.sleep(1)

while Subject4 != 'Completed':
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_3"]').click()

    # Function of Steps
    stepscomplete()

    time.sleep(2)
    Subject4 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[5]/td[6]').text
    print("Subject No.4 " + str(Subject4))
    time.sleep(2)

# Subject 4 Completed
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#




#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 5th Subject Start

print("---------------5th Subject---------------")
Subject5 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[6]/td[6]').text
print("Subject No.5 " + str(Subject5))
time.sleep(1)

while Subject5 != 'Completed':
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_4"]').click()

    # Function of Steps
    stepscomplete()

    time.sleep(2)
    Subject5 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[6]/td[6]').text
    print("Subject No.5 " + str(Subject5))
    time.sleep(2)

# Subject 5 Completed
#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#



#________________________________________________________________________________________________________#
#________________________________________________________________________________________________________#
# 6th Subject Start

print("---------------2nd Subject---------------")
Subject6 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[7]/td[6]').text
print("Subject No.6 " + str(Subject6))
time.sleep(1)

while Subject6 != 'Completed':
    driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus_btnFillSurvey_5"]').click()

    # Function of Steps
    stepscomplete()

    time.sleep(2)
    Subject6 = driver.find_element_by_xpath('//*[@id="mainBodyContentPlaceHolder_ContentPlaceHolder1_grdStudentStatus"]/tbody/tr[7]/td[6]').text
    print("Subject No.6 " + str(Subject6))
    time.sleep(2)

# Subject 6 Completed
#________________________________________________________________________________________________________#
#______________________________Thanks to Hamza Haroon____Created with <3______________________________________#

print("Created with <3")
time.sleep(5)

sys.exit()
