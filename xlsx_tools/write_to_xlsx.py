import openpyxl


from xlsx_tools.create_XLXS_report_file import create_report


def write_to_xlsx(doctor_family_name, appointment_dict, path_to_file, count):
    wb = openpyxl.load_workbook(path_to_file, read_only=False)
    sheet = wb.active
    i = 1
    for k in appointment_dict:
        sheet.cell(row=3 + count, column=1).value = doctor_family_name
        # sheet.cell(row=2, column=1 + i).value = k  # дата приема должна быть только в одной строке
        sheet.cell(row=3 + count, column=1 + i).value = ", ".join(
            appointment_dict[k])  # запись времени приема должна соответсвовать дате  колонки
        i += 1
    wb.save(path_to_file)


if __name__ == '__main__':
    column_to_write = [7, 11]  # список общих дней приема ( те ключей словаря) у врачей
    columns_names = ['doctor'] + column_to_write
    print(columns_names)
    create_report("SMT_clinic", "appointments", 'clinic', columns_names)
    appoint_dict = {7: ['11:40', '12:40', '13:00', '13:20', '13:40', '14:00', '14:20'],
                    9: ['09:20', '09:40', '10:00', '10:20', '10:40', '11:00', '11:20', '11:40', '12:00', '12:20',
                        '12:40', '13:00', '13:20', '13:40', '14:00', '14:20'],
                    11: ['10:00', '10:20', '11:20', '11:40', '12:20', '12:40', '13:00', '13:20', '13:40', '14:00',
                         '14:20', '14:40', '15:00', '15:20', '15:40']}

    write_to_xlsx("Айболит", appoint_dict, '/Users/evgeniy/Documents/SMT_clinic/appointments.xlsx', count=0,
                  )
