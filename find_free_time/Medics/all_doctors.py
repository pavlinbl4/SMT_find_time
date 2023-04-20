from find_free_time.Medics.regex_filter import regex_string_to_dict


def read_specializations_file(txt_file):
    with open(txt_file, 'r') as data_file:
        all_data = data_file.readlines()
    for line in all_data:
        spec_dict = regex_string_to_dict(line.strip()) #  dict lool like {'26977': 'Флебология'}







if __name__ == '__main__':
    print(read_specializations_file("/Volumes/big4photo/_PYTHON/SMT_find_time/find_free_time/specialization.txt"))