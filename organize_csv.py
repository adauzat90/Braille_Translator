import csv
def name_length(elem):
	if len(elem)>0:
		return len(elem[0])
	else:
		return 999999

elements = []

with open('in_word_cont.csv') as rows:
		readCSV = csv.reader(rows, delimiter = ',')
		for row in readCSV:
			elements.append(row)
#print (elements)
elements = [e for e in elements if e]
elements.sort(key=name_length, reverse = True)

with open('in_word_cont.csv', mode = 'w', newline = '') as file:
	row_writer = csv.writer(file, delimiter = ',')
	for element in elements:
		row_writer.writerow(element)