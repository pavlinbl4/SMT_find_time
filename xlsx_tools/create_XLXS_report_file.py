from openpyxl import load_workbook
from openpyxl import Workbook
import os
from must_have.make_documents_subfolder import make_documents_subfolder
from openpyxl.styles import (
                        PatternFill, Border, Side,
                        Alignment, Font, GradientFill
                        )
from openpyxl import Workbook
from openpyxl.styles import PatternFill

from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import Rule


def create_report_file(report_folder, file_name, sheet_name, list_with_columns_names):
    report_file_name = f"{file_name}.xlsx"
    path_to_file = f'{report_folder}/{report_file_name}'

    if os.path.exists(path_to_file):
        wb = load_workbook(path_to_file)  # файл есть и открываю его
        ws = wb.create_sheet(sheet_name)  # добавляю новую таблицу
    else:
        wb = Workbook()  # если файда еще нет
        ws = wb.active  # если файа еще нет
        ws.title = sheet_name  # если файда еще нет

    ws.column_dimensions['A'].width = 50
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 50  # задаю ширину колонки


    ws['A1'] = list_with_columns_names[0]  # create columns names
    ws['B1'] = list_with_columns_names[1]
    ws['C1'] = list_with_columns_names[2]

    # bg_red = PatternFill(fill_type='solid', fgColor="FFC7CE")
    # dxf = DifferentialStyle(fill=bg_red)
    # rule = Rule(type="expression", dxf=dxf,  stopIfTrue=True)
    # rule.formula = ['$А1="doctor"']
    # ws.conditional_formatting.add("A1:C1", rule)

    wb.save(path_to_file)

    return path_to_file


def create_report(subfolder_name, file_name, sheet_name, list_with_columns_names): # return path to file
    return create_report_file(make_documents_subfolder(subfolder_name), file_name, sheet_name, list_with_columns_names)




if __name__ == '__main__':
    print(create_report("SMT_clinic", "appointments", 'clinic', ['doctor', 'appoinment_date', 'comments']))
