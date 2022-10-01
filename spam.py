#!/usr/bin/python3
# Coded by - WebDux (vakh0) -

import pyautogui, time
from termcolor import colored

try:
	print(colored("___[SPAMMER]___", "yellow"))

	word = input(colored('Enter Spam Text: ', 'green'))
	def howmany():
		try:
			global each
			each = int(input(colored('Enter how many you want: ', 'green')))
		except:
			print(colored("[ERROR] You must enter numbers!", "red"))
			howmany()
	howmany()
	i = 0
	def timeToSleep():
		try:
			global tsleep
			tsleep = int(input(colored("Enter time to sleep in seconds: ", "green")))
		except:
			print(colored("[ERROR] Please enter in seconds!", "red"))
			timeToSleep()
	timeToSleep()
	time.sleep(tsleep)

	print("\n[$] Sending ", each, word, "\n\n")
	while i < each:
		print(colored("[+] Sending ", "red") + word)
		pyautogui.typewrite(word)
		pyautogui.press('enter')
		i += 1

except KeyboardInterrupt:
    print(colored("\nSpammer Stopped...", "yellow"))