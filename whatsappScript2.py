# Whatsapp Script to send sheduled messages
# Send Birthday Wishes
# By KAMLESH PANDEY

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(
    "chromedriver")

driver.get("https://web.whatsapp.com/")


def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()
        
def msg():
    name = input('\nEnter Group/User Name: ')
    message = f'Happy Birthday to you {name}'
    try:
        Count = int(input("Enter the message count: "))
        timing_in_min = int(input("Enter the time in min after which you want to send the wishes: "))
        timing = (timing_in_min)*60

        # Find whom to message
        user = driver.find_element_by_xpath(
            '//span[@title = "{}"]'.format(name))
        user.click()
    except:
        msg()

    sleep(timing)

    # Text Box
    text_box = driver.find_element_by_class_name('_3uMse')

    # Send Button
    for i in range(Count):
        text_box.send_keys(message)
        driver.find_element_by_class_name("_1U1xa").click()
        # print(i)

    reps()
    
msg()

# Programmed by Kamlesh Pandey