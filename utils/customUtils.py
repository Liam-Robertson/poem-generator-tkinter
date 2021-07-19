import datetime
from termcolor import colored
import sys
import os

def sysStatus(message, lineSpacing=1):
	# Creates terminals messages with timestamp, color coded keywords and specified line spacing 
	rawtime = datetime.datetime.now()
	timeStamp = rawtime.strftime('%Y-%m-%d %H:%M:%S')
	warningCodes = ['Warning: ', 'Success:', 'Error: ']
	warningColors = ['yellow', 'green', 'red']
	for index in range(3):
		if warningCodes[index] in message:
			coloredWarning = colored(warningCodes[index], warningColors[index])
			message = message.replace(warningCodes[index], coloredWarning)
	printStatement = f'{timeStamp}    {message}'
	counterList = [abs(lineSpacing) // 2] * 2
	if abs(lineSpacing) % 2 == 1:
		if lineSpacing < 0: 
			counterList[1] += 1
		elif lineSpacing > 0: 
			counterList[0] += 1
	printStatement = '{}{}{}'.format(counterList[1] * '\n', printStatement, counterList[0] * '\n')
	print(printStatement)

def debugVar(variable, message=''):
	# Creates clear variable displays for debugging
	coloredID  = colored("####################################################################", 'magenta')
	sysStatus(coloredID, -1)
	sysStatus(f'{variable=}', 0)
	if message != '':
		sysStatus(message, 0)
	sysStatus(coloredID, 1)

def debugStr(message, identifier=1):
	# Creates clear messages for debugging 
	coloredID  = colored("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", 'magenta')
	sysStatus(coloredID, -1)
	sysStatus('Debug statement {}: {}'.format(identifier, message), 0)
	sysStatus(coloredID, 1)

def preRunCleanUp():
	# Clears out the terminal so you can easily view when the latest run was initiated
	if sys.platform.startswith('linux'):
		os.system('clear')
	elif sys.platform.startswith('win'):
		os.system('cls')
	sysStatus('Run Started...\n')

def convertPath(inputPath):
	# Convert paths to work on any operating system
	if sys.platform.startswith('win'):
		temp = inputPath.replace('/', '\\')
		if temp[:2] != '\\\\':
			if temp[:2] != '.\\' and temp[0] != '\\':
				temp = '\\\\' + temp[2:]
			elif temp[0] == '\\':
				temp = '\\\\' + temp[1:]
		result = temp

	elif sys.platform.startswith('win') != True:
		result = inputPath.replace('.\\', '/').replace('\\', '/').replace('//', '/')
	if os.path.exists(result) == False and result[:2] != '.\\' and len(result.split('/')) != 2:
		sysStatus(f"Error: Can't access folder {result} from {sys.platform}")
	return result