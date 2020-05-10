# Facebook-phone-validator
For a series of the phone, check each the phone number has a Facebook account associated with that phone number or not. The script runs in the background.

# Command
python -W ignore run.py 218925122310 3 1

The first argument [218925122310] is the international phone number that includes country code but without (+ or 00).
The second argument [3] is the number of how many phones number to check after the current one.
The third argument [1] is the increment number, if it equals 1, this means to check the number after the current one

# Shell Output
The shell output as following:

+218925122310 , [not found] , 7.0

+218925122312 , [found] , 9.2

+218925122314 , [found] , 8.4


first columns has the phone number, second column the stauts, and last coumns the time in second the consumend to check.

# Shell Output
A list.csv file that contains a list of the Phone numbers that were associated with a Facebook account

# Dependences 
Note, Chrome browser should be available (the following command for mac-os)

pip install selenium

brew cask upgrade chromedriver
