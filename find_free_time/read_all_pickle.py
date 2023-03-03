import os

from Save_pickle_file.save_data import read_pickle_data
from xlsx_tools.create_XLXS_report_file import create_report
from xlsx_tools.write_to_xlsx import write_to_xlsx


def pickle_dict():
    return f'{os.getcwd()}/Pickle_files'


def read_files():
    return os.listdir(pickle_dict())


def common_keys(all_data):
    doctors = [x for x in all_data]
    selected_days = set(all_data[doctors[0]])
    for i in range(1, len(doctors)):
        selected_days = set.intersection(selected_days, set(all_data[doctors[i]]))
    return selected_days


def get_common_dates():  # main function !!!
    pickle_folder = pickle_dict()
    all_data = {}
    for name in read_files():
        all_data[name.split("_")[0]] = read_pickle_data(f'{pickle_folder}/{name}')
    return all_data


def table_heard_genetation(common_days):
    return ['doctor'] + sorted([x for x in common_days])


if __name__ == '__main__':
    all_data = get_common_dates()  # еще один словарь где ключи фамилии докторов, а значения словари с датами их приемов
    common_days = common_keys(all_data)  # days when all doctors are available
    columns_names = table_heard_genetation(common_days)  # names of columns in table
    path_to_file = create_report("SMT_clinic", "appointments", 'clinic', columns_names)  # create report file
    write_to_xlsx(all_data, common_days, path_to_file)  # записываю данные в файл
