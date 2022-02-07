import os

''' 
- Step 1: looking in the Glossary/Input direcotry to get the names of the file we split them the python save it as an
 array and we take the first element of the array(name without extension sep='.')
- Step 2: Create an file of the file name array to add easly in the html file later ToC(Table of Contents)
- Step 3: Saving the lines between h3 and h4 including h4 in variable. Same thing with td in some files
- Step 4: create file html new structure with the save line from te step 3
 '''

# this directory is where the input files are stored
directory = r'/Users/kemendimeri/PycharmProjects/Glossary/Input'
for filename_path in os.listdir(directory):
	if filename_path.endswith('.html'):
		filename = filename_path.split(sep='.',)
		with open('/Users/kemendimeri/PycharmProjects/Glossary/glossary_list.txt', 'a+') as file_writer:
			file_writer.write(filename[0] + '\n')
		print(filename[0])
	else: continue
	# step 2
	file = open(r'/Users/kemendimeri/PycharmProjects/Glossary/Input/' + filename_path)
	line_count = 0
	text_lines = file.read()
	text = ''
	# step 3
	h3 = text_lines.find('<h3')
	h4 = text_lines.find('<h4')
	result = text_lines[h3:h4]
	# step 4
	filename = filename_path.split(sep='.', )
	templateheader = f'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Strict//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>{filename[0]}</title>
<meta name="_keywords" content="5G|{filename[0]}">
<meta name="_display_title" content="{filename[0]}|{filename[0]}|{filename[0]}">

<link rel="stylesheet" href="styles/html_docs_standard.css" type="text/css">
</head>
<body>
'''
	templatefooter = f'''<table class="copyright"><tr>
<td class="copyright">&copy;&nbsp;<a href="http://www.inacon.com">INACON GmbH</a>
1999 - 2020. All rights reserved. Reproduction and/or unauthorized use of<br>this material is prohibited and will be prosecuted to the full extent of German and international laws.</td>
</tr></table>
</body>
</html>
	'''
	with open('/Users/kemendimeri/PycharmProjects/Glossary/Output/'+str(filename[0])+'.html', 'a') as writing:
		writing.write(templateheader + result + templatefooter)
	file.close()