import PyPDF2

pdfFileObj = open('benephilly.pdf', 'rb')  # creating a pdf file object

pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # Create a PDF reader Object

print(pdfReader.numPages) # Number of Pages

pageObj = pdfReader.getPage(0)  # creating a page object 

print(pageObj.extractText()) # extracting text from page 

pdfFileObj.close()