from openpyxl import *

wb=load_workbook('/home/dev/test.xlsx')

for sheet in wb.sheetnames:
    ws=wb[sheet]
    for row in ws.rows:
        for cell in row:
            print(cell.value)
