from selenium import webdriver

driver = webdriver.Chrome("chromedriver")

driver.get("https://web.whatsapp.com")

def msg():
    name = input('\nEnter Group/User Name: ')
    message = input("Enter your message to group/user")
    Count = int(input("Enter the message count:"))

    # Find Whom to message 
    user = driver.find_element_by_xpath(
        '//span[@title = "{}"]'.format(name))
    
    user.click()

    text_box = driver.find_element_by_class_name('_3uMse')

    #Send Button
    for i in range(Count):
        text_box.send_keys(message)
        driver.find_element_by_class_name("_1U1xa").click()

msg()


def reps():
    print("Do you want to send more msg to anyone")
    askUser = input("Press y for Yes and n for No : ")
    if (askUser == 'Y' or askUser == 'y'):
        msg()
        reps()
    elif (askUser == 'N' or askUser == 'n'):
        print("Thank you see you soon")
    else:
        print("Please Enter Valid option :\n")
        reps()

reps()
