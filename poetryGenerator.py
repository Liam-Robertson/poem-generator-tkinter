import xml.etree.ElementTree as ET
import os
import docx
from docx.enum.text import WD_BREAK
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING

def createFileList():
	#Creating a list with all the filenames inside it [1-1-1.xml, 5-2-9.xml, 7-5-14.xml...]
	filename_lst = []

	for filename in os.listdir('../syllabary_poems'):
		if filename.endswith('.xml'):
			filename_lst.append(filename)
	return filename_lst

def findMaxValues(filename_lst):
	#Finding max values of X, Y and Z for "X-Y-Z.xml files. This is used later in the main algorithm"
	titleX_lst = []
	titleY_lst = []
	titleZ_lst = []

	for file in filename_lst:
		titleX_lst.append(int(file[:-4].split("-")[0]))
		titleY_lst.append(int(file[:-4].split("-")[1]))
		titleZ_lst.append(int(file[:-4].split("-")[2]))

	max_x = max(titleX_lst)
	max_y = max(titleY_lst)
	max_z = max(titleZ_lst)
	max_values = [max_x, max_y, max_z]

	return max_values

def getUserInput(filename_lst):
	#Handling user input errors. code = code_original is used in the main algorithm
	limit = int(input('How many poems do you want? '))
	while limit > len(filename_lst):
		print("Invalid input. Input a number equal to or less than " + str(len(filename_lst)))
		limit = int(input('How many poems do you want? '))

	code_original = input('What poem do you want to start with? ')
	code = code_original

	order_var = input('Do you want it outputted in reverse order (type "yes" or "no")')

"""
This algorithm creates a list of the files that are going to be printed out. 
It does this by taking the X coordinate in an X-Y-Z.xml file (e.g. in 1-2-3.xml x=1) then adding 1 to the X coordinate and checking to see if that file exists. 
If the file doesn't exist then it adds 1 again and checks if that files exists until it finds a file that does exist. Then it adds that file name to the final 
list. This process is then repeated for the X, Y and Z coordinates. Once a filename is added to the final list then that filename is removed from the original list (so there are no doubles in the final list). 
"""

def createOutputFileList(filename_lst, startingPoem, numOfPoems, max_values):
	final_lst = []
	counter3 = 0
	counter4 = 0

	final_lst.append(str(startingPoem) + ".xml")
	filename_lst.remove(startingPoem + '.xml')
	while len(final_lst) < numOfPoems: 
		for i, j in zip(range(3), max_values):
			counter3 = 0 
			if len(final_lst) < numOfPoems:
				countVar = len(final_lst)
				while len(final_lst) == countVar: 
					counter4 += 1
					code = code.split("-")
					code = [int(x) for x in code]
					code[i] += 1
					counter3 += 1
					if code[i] > j: 
						code[i] = 1
					code = [str(x) for x in code]
					code = '-'.join(code)
					if counter3 > j: 
						break
					if counter4 > 10000: 
						final_lst.append(filename_lst[0])
						filename_lst.remove(filename_lst[0])
					if code + ".xml" in filename_lst:
						counter4 = 0
						final_lst.append(code + '.xml')
						filename_lst.remove(code + '.xml')
	return final_lst

def reverseList(order_var, final_lst):
	#Reverse list order if user requests it
	if order_var == "yes":
		final_lst = final_lst[::-1]		
	return final_lst			

def readingXML(final_lst):
	#Creating a dictionary in the form (filename: [title, text])
	name_lst = []
	content_lst = []

	for filename in final_lst:
		temp_lst = []
		tree = ET.parse(filename)
		root = tree.getroot()
		temp_lst.append(root[0].text)
		temp_lst.append(root[2].text)
		content_lst.append(temp_lst)
		name_lst.append(filename[:-4])

	text_dict = dict(zip(name_lst, content_lst))
	return text_dict

def creatingTextDocumentOutput(text_dict):
	#Outputting to a word document
	counter2 = 0

	doc = docx.Document()
	for i in text_dict.keys():
		counter2 += 1 
		style = doc.styles['Normal']
		font = style.font
		font.name = 'Helvetica'
		font.size = Pt(14)
		par = doc.add_paragraph()
		par.paragraph_format.line_spacing = 1
		run1 = par.add_run(i)
		run1.add_break(WD_BREAK.LINE)
		run1.add_break(WD_BREAK.LINE)
		if text_dict[i][0] != None:
			if text_dict[i][0].isspace() == False:
				run2 = par.add_run(text_dict[i][0])
				run2.bold = True
				run2.add_break(WD_BREAK.LINE)
				run2.add_break(WD_BREAK.LINE)
		run3 = par.add_run(text_dict[i][1])
		if counter2 < len(text_dict):
			run3.add_break(WD_BREAK.PAGE)
	doc.save('Syllabary Test.docx')

	print(text_dict.keys())
	print("length is " + str(len(final_lst)))
	print("length of set is " + str(len(set(text_dict.keys()))))
