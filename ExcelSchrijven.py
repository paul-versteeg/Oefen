# Alle functies van OpenPyxl importeren
# OpenPyxl module kan je installeren met linux command: >> pip install openpyxl
# Daarna in PyCharm installeren door file->settings->project -> project interpreter. Op "+" klikken rechtsboven, naar openpyxl zoeken en installeren

from openpyxl import *

# excelsheet benoemen
wb=Workbook()
sheet=wb.active
filepath="/home/dev/test.xlsx"

# een grove weinig elegante manier om wat in het excelfile te zetten
row=1
column=2

sheet.cell(row,column).value='kolom1'
row=row+1
sheet.cell(row,column).value=84
row=row+1
sheet.cell(row,column).value=39
row=row+1
sheet.cell(row,column).value=5

column=column+1
row=1
sheet.cell(row,column).value='kolom2'
row=row+1
sheet.cell(row,column).value=230
row=row+1
sheet.cell(row,column).value=82
row=row+1
sheet.cell(row,column).value=9983

column=column+1
row=1
sheet.cell(row,column).value='kolom3'
row=row+1
sheet.cell(row,column).value=864
row=row+1
sheet.cell(row,column).value=1
row=row+1
sheet.cell(row,column).value=33

# file opslaan
wb.save(filepath)

