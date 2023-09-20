import sys
import os
import comtypes.client

wdFormatPDF = 17

# если брать названия из аргументов строки
# in_file = os.path.abspath(sys.argv[1])
# out_file = os.path.abspath(sys.argv[2])

in_file = os.path.abspath("filename2.xlsx")
out_file = os.path.abspath("filename2.pdf")

excel = comtypes.client.CreateObject('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False
# print(dir(excel))
doc = excel.Workbooks.Open(in_file)
doc.WorkSheets("New_sheet2").Select()
doc.ActiveSheet.ExportAsFixedFormat(0, out_file)
# doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
excel.Quit()