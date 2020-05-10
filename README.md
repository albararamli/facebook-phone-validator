# facebook-phone-validator
For a series of the phone, check each the phone number has a Facebook account associated with that phone number or not.

# command
python -W ignore r.py 218925122310 3

The first argument is the international phone number that includes country code but without (+ or 00).
The second argument is the number of how many phones number to check after the current one.

# Output
A list.csv file that contain the follownig columns:
Phone #, status, time consumed to check

# Dependences 
Note, Chrome browser should be available (the following command for mac-os)
pip install selenium
brew cask upgrade chromedriver
