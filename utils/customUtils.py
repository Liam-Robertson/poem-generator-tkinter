import datetime
from termcolor import colored
import sys
import os

def sysStatus(message, lineSpacing=1):
	# Creates terminals messages with timestamp and color coded keywords 
	rawtime = datetime.datetime.now()
	timeStamp = rawtime.strftime('%Y-%m-%d %H:%M:%S')
	warningCodes = ['Warning: ', 'Success:', 'Error: ']
	warningColors = ['yellow', 'green', 'red']
	for index in range(3):
		if warningCodes[index] in message:
			coloredWarning = colored(warningCodes[index], warningColors[index])
			message = message.replace(warningCodes[index], coloredWarning)
	printStatement = f'{timeStamp}    {message}'
	counterList = [0, 0]
	if lineSpacing != 0:
		if abs(lineSpacing) % 2 == 1:
			if lineSpacing < 0:
				counterList[1] += 1
				lineSpacing = abs(lineSpacing)
			else:
				counterList[0] += 1
		lineSpacing = abs(lineSpacing)
		counterList[0] += lineSpacing // 2
		counterList[1] += lineSpacing // 2
		printStatement = '{}{}{}'.format('\n' * counterList[1], printStatement, counterList[0] * '\n')
	print(printStatement)

def debugVar(variable, message=''):
	# Creates clear variable displays for debugging
	coloredID  = colored("####################################################################", 'magenta')
	sysStatus(coloredID, -1)
	sysStatus(f'{variable=}', 0)
	if message != '':
		sysStatus(message, 0)
	sysStatus(coloredID, 1)
	

def debugId(message, identifier=1):
	# Creates clear identifiers for debugging 
	coloredID  = colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'magenta')
	sysStatus(coloredID, -1)
	sysStatus('Debug statement {}: {}'.format(identifier, message), 0)
	sysStatus(coloredID, 1)

def preRunCleanUp():
	#Clears out the terminal so you can easily view when the latest run was initiated
	if sys.platform.startswith('linux'):
		os.system('clear')
	elif sys.platform.startswith('win'):
		os.system('cls')

	sysStatus('Run Started...\n')


def _convertPath():
	return