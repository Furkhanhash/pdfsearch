import PyPDF2
import re
import glob
import os

# open the pdf file

# define keyterms
String = "config"
# extract text and do the search
for filename in glob.glob(os.path.join(os.getcwd(), '*.pdf')):
    object = PyPDF2.PdfFileReader(filename)
    NumPages = object.getNumPages()
    for i in range(0, NumPages):
        # get number of pages       
        PageObj = object.getPage(i)
        #print("this is page " + str(i)) 
        Text = PageObj.extractText() 
        # print(Text)
        ResSearch = re.search(String, Text)
        if String in Text:
            print(filename)
            break
    #print(Text)
    #print(ResSearch)