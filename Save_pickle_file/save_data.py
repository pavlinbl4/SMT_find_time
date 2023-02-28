import pickle
from must_have.make_subfolder import m_subfolder


def save_data_pickle(file_data, file_name):
    file_name = f'{m_subfolder("Pickle_files")}/{file_name}'
    saved_file = open(file_name, 'wb')
    pickle.dump(file_data, saved_file)


def read_pickle_data(file_name):
    saved_file = open(file_name, 'rb')
    saved_data = pickle.load(saved_file)
    return saved_data


if __name__ == '__main__':
    file_data = 'crocodile22'
    file_name = 'TTest_file_name'

    save_data_pickle(file_data, file_name)
    # way_to_file = f'/Volumes/big4photo/_PYTHON/Drops_words/Pickle_files_HB/{file_name}'
    # print(read_pickle_data(way_to_file))
