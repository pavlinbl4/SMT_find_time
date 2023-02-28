from Save_pickle_file.save_data import read_pickle_data
import os



def common_keys():
    return set(dict1).intersection(set(dict2))


def make_dict():
    print(os.getcwd())


if __name__ == '__main__':
    # dict1 = read_pickle_data(
    #     '/Volumes/big4photo/_PYTHON/SMT_find_time/find_free_time/Pickle_files/Гаглоева_Зарина_Рафиковна')
    # dict2 = read_pickle_data(
    #     '/Volumes/big4photo/_PYTHON/SMT_find_time/find_free_time/Pickle_files/Марченко_Ольга_Андреевна')
    #
    # print(dict1.keys())
    # print(dict2.keys())
    # common_k = common_keys()
    # print(f"{common_k = }")
    #
    # dict1 = {x : dict1[x] for x in common_k}
    # dict2 = {x : dict2[x] for x in common_k}
    #
    # print(dict1.keys())
    # print(dict2.keys())
    print(make_dict())
