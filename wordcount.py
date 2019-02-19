 # read a .txt file from a folder
# Count the number of times each word appears in the file
# Create a file called output.txt and write each word and its count in this file.



# Removing all punctuations and making sure, everything in lower case
def remove_punctuation():
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_line = ""
		for char in line:
        if char not in punctuations:
            new_line = new_line + char
						new_line = new_line.lower()
    return (new_line)




# counting the repeated words and storing them into a dictionary
def words_count():
    dict = {}
		words = remove_punctuation().split(' ')
		#print(words)
		for word in words:
		    if word not in dict:
				    dict[word] = 1
				else:
				    dict[word] +=1
		return dict



if __name__=="__main__":
    filename = input("paste your directory here from where you want to read:")
		f = open(filename, "r")
		line = f.read()
		# print(line)
		f1 = open("C:\Dev\output.txt", "w")
		f1.write("word---wordcount\n")
		for key,value in words_count().items():
		    f1.write("{}----{}\n".format(key,value))
		f.close()
		f1.close()














