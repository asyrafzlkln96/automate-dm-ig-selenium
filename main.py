from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time
import os
import logging,logging.handlers

from dotenv import load_dotenv

# Load env variables from .env file
load_dotenv()

# Script should login to instagram - DONE
# Navigate to DM section - DONE
# Send predefined messsage to list of users
# Handle login challenges or captchas

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
	"status.log",
	maxBytes= 1024 * 1024,
	backupCount = 1,
	encoding="utf8",
	)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


chrome = webdriver.Chrome()
chrome.get('https://instagram.com')

def login():
	# username=chrome.find_element(by=By.XPATH, value='//</html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input>')
	# username=chrome.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
	try:
		username=chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
		username.send_keys(os.getenv("INSTAGRAM_USERNAME"))
		time.sleep(4)
		pwd=chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
		# pwd = chrome.find_element(by=By.XPATH, value='//</html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input>')
		# pwd = chrome.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
		pwd.send_keys(os.getenv("INSTAGRAM_PASSWORD"))
		pwd.submit()
		time.sleep(7)
		logger.info('Successfully logged into Instagram Account!')
	except Exception as e:
		print('error:',str(e))
		logger.error(f'Error logging in: {str(e)}! Please check credential in .env file')



def bypass_save_info():
	try:
		# Bypass authentication
		login_code = chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input")
		login_code.send_keys(os.getenv("INSTAGRAM_CODE"))
		login_code.submit()
		time.sleep(4)
		# Bypass save info
		not_now = chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div").click()
		time.sleep(3)
		# Bypass save notification
		notification=chrome.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
		time.sleep(3)
		logger.info('Successfully bypassed all info and authentications!')
	except Exception as e:
		print(f'Error in bypass function: {str(e)}')


def message():
	try:
		message = "This is automated message .."
		recipient_name = 'asyrafzulmusic'
		msg_click = chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div/div[1]/div/div[2]/div/span")
		msg_click.click()
		time.sleep(6)	
		chaticon = chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div").click()
		time.sleep(5)
		typename = chrome.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input")
		typename.send_keys(recipient_name)
		time.sleep(5)

		click_name = chrome.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/label/div/input").click()
		next_btn = chrome.find_element_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div").click()
		time.sleep(3)
		mbox = chrome.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
		mbox.send_keys(message)
		send=chrome.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]")
		send.click()
		logger.info(f'Recipient/Recipients: {recipient_name}')
		logger.info(f'This is the message sent: {message}')

	except Exception as e:
		print(f'Error in message function: {str(e)}')
		logger.error(f'This is the message sent: {message}')


login()
bypass_save_info()
message()

# if '__name__' == '__main__':
# 	login()
# 	# bypass_save_info()