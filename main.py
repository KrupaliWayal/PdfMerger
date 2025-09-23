import PyPDF2 #PyPDF2 can also remove existing pages, slice the pdf,retrieve certain pages, etc.

pdffiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdffiles:
    pfdFile = open(filename, "rb") #use to open pdf
    pdfReader = PyPDF2.PdfReader(pfdFile) #PdfFileReader is a class used to append
    merger.append(pdfReader) #merges
pfdFile.close() #closed the opened file
merger.write("merged.pdf") #save merged pdf as merged.pdf