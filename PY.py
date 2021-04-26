from PyPDF2 import PdfFileWriter , PdfFileReader
pdfwriter=PdfFileWriter()
pdf=PdfFileReader("a.pdf") # Name of the pdf you want to protect with password.
for page_num in range(pdf.numPages):
    pdfwriter.addPage(pdf.getPage(page_num))
passw="Math1158" #The password you want to put
pdfwriter.encrypt(passw)
with open("Answer.pdf",'wb') as f: # Nwe password protected PDF. Here Answer is the name of the new pdf
    pdfwriter.write(f)
    f.close()