# automate-dm-ig-selenium
Automate Direct Messages(DMs) to Instagram using Selenium

## Requirements:
- selenium==4.2.0
- python-dotenv==1.0.0

## Prerequisites:
- You have to have Instagram account, preferred to have two accounts to test this script
- You have to download ChromeDriver.exe from (https://chromedriver.chromium.org/downloads), then put into the same directory as the main.py
- For this test, I used ChromeDriver version 121.0.6167.85 from (https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip)
- .env file that contains this key: "INSTAGRAM_USERNAME": your_account_username, "INSTAGRAM_PASSWORD": your_password, "INSTAGRAM_CODE": login_code_if_have, "LOGIN_CODE_FLAG": "True"
- LOGIN_CODE_FLAG is "True" by default, if don't have login code, then set to "False"

## Functionality:
- This script is developed to automate Messages to Instagram using Selenium.
- Logging functions to log info and error messages from the automation script.

## To run the script (after done the Prerequisites):
- Activate virtual environment or conda environment
- Run pip install -r requirements.txt
- Set .env file correctly with your credentials and configurations
- Type python main.py in terminal
  ![image](https://github.com/asyrafzlkln96/automate-dm-ig-selenium/assets/53460015/f4459049-e60d-4a69-99a0-0f0f046cea20)


## Current limitation:
- The current implementation only runs on Selenium version 4.2.0. The script does not work on version 4.17.2(tested), and not tested with other versions of Selenium that are mentioned
- Thus , if you have newer Selenium, or other version of Selenium, do run this to reinstall to 4.2.0 (Run pip install selenium==4.2.0 --force-reinstall)
- The current script works if you have Google Chrome, assuming most PC already preinstalled with Chrome. Firefox will not work (need GeckoDriver.exe)
- If you need to exclude the login code, you may disable the login code by setting LOGIN_CODE_FLAG to "False" in .env file
- Current approach uses Absolute XPath, which even small changes from Instagram may break the code. If Instagram updates the HTML structure, the code may not work.
 (A better implementation would be more readable XPath or other locator strategies
E.g: //span[text()='Direct']
//div[contains(@class, 'user-container')][1]//span[text()='Direct'] )
