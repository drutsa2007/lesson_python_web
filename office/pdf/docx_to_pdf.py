import sys
import os
import comtypes.client

wdFormatPDF = 17

# если брать названия из аргументов строки
# in_file = os.path.abspath(sys.argv[1])
# out_file = os.path.abspath(sys.argv[2])

in_file = os.path.abspath("filename1.docx")
out_file = os.path.abspath("filename1.pdf")

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()