# automate-dm-ig-selenium
Automate Direct Messages(DMs) to Instagram using Selenium

## Requirements:
- selenium<=4.2.0
- python-dotenv==1.0.0

## Prerequisites:
- You have to have Instagram account, preferred to have two accounts to test this script
- .env file that contains this key: "INSTAGRAM_USERNAME": your_account_username, "INSTAGRAM_PASSWORD": your_password, "INSTAGRAM_CODE": login_code_if_have, "LOGIN_CODE_FLAG": "True"
- LOGIN_CODE_FLAG is "True" by default, if don't have login code, then set to "False"

## Functionality:
- This script is developed to automate Messages to Instagram using Selenium.
- Logging functions to log info and error messages from the automation script.

## To run the script:
python main.py

## Current limitation:
- The current implementation only runs on Selenium version 4.2.0 and below. Newer versions of Selenium will not work
- Thus , if you have newer Selenium, preferred to downgrade to 4.2.0 and below.
- Thus, if you need to exclude the login code, you may disable the login code by setting LOGIN_CODE_FLAG to "False"

