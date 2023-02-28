from openpyxl import load_workbook
import os
from must_have.make_documents_subfolder import make_documents_subfolder
from openpyxl.styles import (
    PatternFill, Border, Side,
    Alignment, Font
)
from openpyxl import Workbook


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

    ws.row_dimensions[1].height = 30

    ws['A1'] = list_with_columns_names[0]  # create columns names
    ws['B1'] = list_with_columns_names[1]
    ws['C1'] = list_with_columns_names[2]
    ws['A1'].font = Font(size=18, bold=True)
    ws['B1'].font = Font(size=18, bold=True)
    ws['C1'].font = Font(size=18, bold=True)
    ws['A1'].alignment = Alignment(horizontal='center')
    ws['B1'].alignment = Alignment(horizontal='center')
    ws['C1'].alignment = Alignment(horizontal='center')
    ws['A1'].fill = PatternFill('solid', fgColor="DDDDDD")
    ws['B1'].fill = PatternFill('solid', fgColor="DDDDDD")
    ws['C1'].fill = PatternFill('solid', fgColor="DDDDDD")

    thins = Side(border_style="double", color="1d51e7")

    ws['A1'].border = Border(top=thins, bottom=thins, left=thins, right=thins)
    ws['B1'].border = Border(top=thins, bottom=thins, left=thins, right=thins)
    ws['C1'].border = Border(top=thins, bottom=thins, left=thins, right=thins)

    wb.save(path_to_file)

    return path_to_file


def create_report(subfolder_name, file_name, sheet_name, list_with_columns_names):  # return path to file
    return create_report_file(make_documents_subfolder(subfolder_name), file_name, sheet_name, list_with_columns_names)


if __name__ == '__main__':
    print(create_report("SMT_clinic", "appointments", 'clinic', ['doctor', 'appoinment_date', 'comments']))
