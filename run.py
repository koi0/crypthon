import platform
import os
import time
import hashlib

def initiate():
	if platform.system() == str("Linux"):
		print("User running LINUX")
		os.system("clear")
		firstDialouge()

	elif platform.system() == str("Windows"):
		print("ERROR: This script is not yet compatible with Windows based systems :(.")
		exit()
	else:
		print("ERROR: Unable to recognize platform...")
		exit()

def firstDialouge():
	time.sleep(0.1)
	print("******************************")
	time.sleep(0.1)
	print("* Welcome to crypthon!       *")
	time.sleep(0.1)
	print("******************************")
	time.sleep(0.1)
	print("* What would you like to do? *")
	time.sleep(0.1)
	print("******************************")
	time.sleep(0.1)
	print("* 1. Encrypt a message.      *")
	time.sleep(0.1)
	print("* 2. Encrypt a file.         *")
	time.sleep(0.1)
	print("* 3. Exit crypthon.          *")
	time.sleep(0.1)
	print("******************************")
	time.sleep(0.1)
	in1 = input("> ")

	try:
		int(in1)
	except ValueError:
		print("ERROR: user entered illegal character.")
		exit()

	if int(in1) == int(1):
		print("")
		encryptMessage()
	elif int(in1) == int(2):
		print("")
		encryptFile()
	elif int(in1) == int(3):
		print("Exiting...")
		exit()
	else:
		print("you didn't type anythin :(")
		exit()

def encryptMessage():
	print("Encrypt message")

def encryptFile():
	print("Encrypt message")


initiate()