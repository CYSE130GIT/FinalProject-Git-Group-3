import smtplib
from email.message import EmailMessage 
import psutil
import logging
import time

#logging config
logging.basicConfig(
    filename= "system_performance.log",
    level=logging.INFO,
    format= "%(asctime)s - CPU: %(message)s"
)

#email alert function
def send_alert(subject, body):
        msg = EmailMessage()
        msg.set_content(body)
        msg['Subject']= subject
        msg['From']= 'youremail@gmail.com'
        msg['To']= 'recipient_email@gmail.com'
#Sends the message using an email login, I have tried to get the smtp login to work with both gmail and yahoo to luck, but the code should be correct.
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login('your_email@gmail.com', 'your_password')
            smtp.send_message(msg)

#logging function
def log_system_performance():
    while True: 
        #cpu usage pulled
        cpu_usage=psutil.cpu_percent(interval=1)

        #memory usage pulled
        memory=psutil.virtual_memory()
        memory_usage=memory.percent 

        #disk usage pulled
        disk=psutil.disk_usage('/')
        disk_usage=disk.percent

        #logging data
        logging.info(
            f"CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%"
        )
        
        #alert generation Prints test string to terminal and attempts to send email
        if cpu_usage >60:
            send_alert('High CPU Usage Alert', f'CPU Usage is {cpu_usage}%')
            print('High Cpu Usage')

        if memory_usage >60:
            send_alert('High Memory Usage Alert', f'Memory Usage is {memory_usage}%')
            print('High Memory Usage')

        if disk_usage >60:
            send_alert('High Disk Usage Alert', f'Disk Usage is {disk_usage}%')
            print('High Disk Usage')

        #defining logging interval 
        time.sleep(30) 

if __name__=="__main__":
    log_system_performance()

