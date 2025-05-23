#You can schedule this on a task scheduler without using loop and sleep time

import time
from plyer import notification

if __name__ == "__main__":
    while True:                     #How many times you want to run this 
        notification.notify(
            title="Please Drink Water!!",
            message="The human body is approximately 70% water.",
            timeout=5               #Notification floating time
        )
        time.sleep(60*60)           #Notification sleeping time
