import openpyxl

path = "20211024 Interrompibilita spreadsheet.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

values = []

# Get the active worksheet
for row in range(6,66):
    for column in range(1, 5)
       cell_value = worksheet 