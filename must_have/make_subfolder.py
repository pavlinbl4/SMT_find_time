import os
import pathlib


def m_subfolder(subfolder_name):
    if not os.path.exists(subfolder_name):
        os.makedirs(subfolder_name)
    return pathlib.Path(subfolder_name).absolute()


if __name__ == '__main__':
    print(m_subfolder('sub_dir'))
