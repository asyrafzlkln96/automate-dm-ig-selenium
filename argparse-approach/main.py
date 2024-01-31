from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
import time
import os
import logging,logging.handlers
import argparse


## This script automates the login and sends DM to list of users to Instagram using selenium
## This version uses argument parser to parse variable 
## Usage: python main.py --ig_username "username" --ig_password "password" --code_flag --ig_code 123456

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


parser = argparse.ArgumentParser(description='Python selenium app to automate DM to Instagram')

parser.add_argument('--ig_username', type=str, help='Instagram Username')
parser.add_argument('--ig_password', type=str, help='Instagram Password')
parser.add_argument('--code_flag', action='store_true', help='Login Code Flag, default is True, set to False if dont have code')
parser.add_argument('--ig_code', type=int, help='Instagram Login Code')

args = parser.parse_args()

ig_username = args.ig_username
ig_password = args.ig_password
code_flag = args.code_flag
ig_code = int(args.ig_code)

chrome = webdriver.Chrome()
chrome.get('https://instagram.com')


def login(ig_username, ig_password):
	try:
		time.sleep(2)
		username = chrome.find_element(By.XPATH, "//input[@aria-label='Phone number, username, or email']")
		username.send_keys(ig_username)
		time.sleep(4)
		pwd = chrome.find_element(By.XPATH, "//input[@aria-label='Password']")
		pwd.send_keys(ig_password)
		pwd.submit()
		time.sleep(7)
		logger.info('Successfully logged into Instagram Account!')
	except Exception as e:
		print('error:',str(e))
		logger.error(f'Error logging in: {str(e)}! Please check credential in .env file')



def bypass_save_info(code_flag, ig_code):
	try:
		login_code_flag = code_flag
		time.sleep(2)
		# Bypass authentication
		if login_code_flag == 'True' or login_code_flag == True:
			login_code = chrome.find_element(By.XPATH, "//input[@aria-describedby='verificationCodeDescription']")
			login_code.send_keys(ig_code)
			login_code.submit()
			time.sleep(4)
		# Bypass save info
		not_now = chrome.find_element(By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(@class, 'xa49m3k') and contains(@class, 'xe8uvvx')]").click()
		time.sleep(3)
		# Bypass save notification
		notification=chrome.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
		time.sleep(3)
		logger.info('Successfully bypassed all info and authentications!')
	except Exception as e:
		print(f'Error in bypass function: {str(e)}')


def send_message(chrome,recipient_name,message):
	try:
		msg_click = chrome.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div/div[1]/div/div[2]/div/span")
		# msg_click = chrome.find_element(By.XPATH, "//span[contains(@class, 'x1lliihq') and contains(@class, 'x193iq5w') and contains(@class, 'x6ikm8r') and contains(@class, 'x10wlt62') and contains(@class, 'xlyipyv') and contains(@class, 'xuxw1ft')]")
		msg_click.click()
		time.sleep(6)	
		chaticon = chrome.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div").click()
		# chaticon = chrome.find_element(By.XPATH, "//div[contains(@class, 'x1lliihq') and contains(@class, 'x1n2onr6') and contains(@class, 'x5n08af')]").click()
		time.sleep(5)
		typename = chrome.find_element(By.XPATH, "//input[@placeholder='Search...'][@name='queryBox']")
		typename.send_keys(recipient_name)
		time.sleep(5)

		click_name = chrome.find_element(By.XPATH, "//input[@aria-label='Toggle selection'][@name='ContactSearchResultCheckbox']").click()
		next_btn = chrome.find_element(By.XPATH,"/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div").click()
		time.sleep(3)
		mbox = chrome.find_element(By.XPATH, "//div[@aria-describedby='Message']")
		mbox.send_keys(message)		
		send = chrome.find_element(By.XPATH, "//div[@role='button' and text()='Send']")
		send.click()
		logger.info(f'Recipient/Recipients: {recipient_name}')
		logger.info(f'This is the message sent: {message}')
		logger.info('Successfully sent message!')

	except Exception as e:
		print(f'Error in message function: {str(e)}')
		logger.error(f'Error in send message function: {message}')



login(ig_username, ig_password)
bypass_save_info(code_flag, ig_code)
recipients = ['asyrafzulmusic','9gag']
msg = "This is an automated message.."

for recipient_username in recipients:
	send_message(chrome,recipient_username,msg)

	



	
