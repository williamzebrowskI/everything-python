from PyPDF2 import PdfReader
import re
import PyPDF2
import pytest
import nltk

reader = PdfReader('benephilly.pdf', 'rb') # Create a PDF reader Object
number_of_pages = len(reader.pages) #number of pages
page = reader.pages[0]   # creating a page object 
text = page.extract_text()  # extracting text from page 
print(text)

#def test_create_txt():
 #   texts = "We are here to help! Call llkj BenePhilly at 1-800-236-2 194 if you have any questions." 
#    convert_file = open('pdfconvert.txt', 'wt')  #creates file
#    print(text, file=convert_file) # prints text from pdf to new file

#    convert_file = open('pdfconvert.txt', 'r')
#    #assert texts in convert_file.read()
#    convert_file.close()


#def test_mod_text():
#    mod = open('pdfconvert.txt', 'r')
#    print(mod[0:10])

#test_create_txt()
