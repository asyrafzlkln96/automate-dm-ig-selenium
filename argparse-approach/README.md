## Argparse approach
Added argument parser approach for ease of uses

# Usage (run script using this command):
python main.py --ig_username "username" --ig_password "password" --code_flag --ig_code 123456

# Example if using cronjob:
- This will run the script on Monday, set the cronjob in server by cron -e
  
0 0 * * 1 /path/to/python /path/to/your/main.py --ig_username 'username' --ig_password 'password' --code_flag --ig_code 123456



