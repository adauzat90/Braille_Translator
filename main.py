import csv
from collections import OrderedDict

def recieve_input():
	input_str = ""
	with open("test.txt", "r") as input_doc:
		for line in input_doc:
			input_str += line

	return input_str

def replace_single_word_cont(input):
	single_word_cont = {}
	with open('Single_word_cont.csv') as letters:
		readCSV = csv.reader(letters, delimiter = ',')
		for row in readCSV:
			if len(row) == 2:
				symbol = row[0]
				single_word_cont[symbol] = row[1]

	for key in single_word_cont:
		input = input.replace(key,single_word_cont[key])

	return input

def replace_in_word_cont(input):
	in_word_cont = OrderedDict()
	with open('in_word_cont.csv') as letters:
		readCSV = csv.reader(letters, delimiter = ',')
		for row in readCSV:
			if len(row) == 2:
				symbol = row[0]
				in_word_cont[symbol] = row[1]

	word_list = input.split()

	output = ""

	for word in word_list:
		if word != "ow":
			for key in in_word_cont:
				if key != "ea" or word[-2:] != "ea":
					word = word.replace(key,in_word_cont[key]+"/")
					#print("key: "+key + "  "+word)
		output += word + " "
	return output

def replace_capitalization(input):
	sentences = input.split('.')
	#print (sentences)
	output = ""
	for sentence in sentences:
		if sentence != "":
			if sentence.isupper():
				sentence = sentence.lower()
				#print(sentence)

				output += ("6/6/"+sentence+"./6 ")
				#print (output)
			else:
				output += (sentence +". ")
				#print(output)

	#print (output)
	words = output.split()
	#print(words)
	output = ""
	for word in words:
		if word.isupper() and len(word)>1:
			word = word.lower()
			output += "6/6/"+word+" "
		elif word[0].isupper():
			word = word.lower()
			output += "6/"+word+" "

		else:
			output += word+" "
	#print(output)
	return output

def replace_commas(input):
	input = input.replace(",","/2")
	return input

def output_to_file(text,translation):
	#print ("Printing:" + text)
	with open("output.txt","w") as file:
		lines = text.split("\n")
		tranlated_words = translation.split()
		word_num = 0
		print("total: " + str(len(tranlated_words)))
		for line in lines:
			if line.strip():
				if len(line.split())>5:
					split_line = line.split()
					total_len = len(split_line)
					current_len = 0
					while total_len>current_len:
						if total_len>=current_len+5:
							file.write(" ".join(split_line[current_len:current_len+5])+"\n")
							file.write(" ".join(tranlated_words[word_num:word_num+5])+"\n")
							current_len+=5
							word_num+=5
							print(word_num)
						else:
							file.write(" ".join(split_line[current_len:total_len])+"\n")
							file.write(" ".join(tranlated_words[word_num:word_num+(total_len-current_len)])+"\n")
							word_num+=total_len-current_len
							current_len+=total_len
							break
					file.write("\n")
				else:
					file.write(line + "\n")
					print(line)
					size_of_line = len(line.split())
					file.write(" ".join(tranlated_words[word_num:size_of_line+word_num]) + "\n")
					word_num+=size_of_line
					file.write("\n")
					#print(word_num)


if __name__ == "__main__":

	braile_dict = {}

	with open('braile_letters.csv') as letters:
		readCSV = csv.reader(letters, delimiter = ',')
		for row in readCSV:
			if len(row) == 2:
				symbol = row[0]
				braile_dict[symbol] = row[1]

	orig_input_str = recieve_input()
	input_str = orig_input_str
	input_str = input_str.replace('\n','').replace('\r','')
	input_str = replace_capitalization(input_str)
	#print("After Capitalization: " + input_str)
	input_str = replace_commas(input_str)
	#print("After commas: " + input_str)
	#input_str = replace_single_word_cont(input_str)
	#print("After single word: "+input_str)
	input_str = replace_in_word_cont(input_str)
	#print("After replacement in: " + input_str)
	for key in braile_dict:
		input_str = input_str.replace(key,braile_dict[key]+"/")

	input_str = input_str.replace("//","/")

	tokens = input_str.split()
	#print(tokens)

	output_str = ""
	for token in tokens:
		token = "(" + token
		if token[-1] == "/":
			token = token[:-1]
		token = token+") "
		output_str += token

	output_str = output_str.rstrip()
	if output_str[-1] != ")":
		output_str += ")"

	#print (output_str)
	output_to_file(orig_input_str,output_str)


