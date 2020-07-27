import xlrd

path= ("F:\\NEEL\\Python Classes\\TestData.xlsx")

wb= xlrd.open_workbook(path)

sheet=wb.sheet_by_index(0)

print(sheet.cell_value(1))