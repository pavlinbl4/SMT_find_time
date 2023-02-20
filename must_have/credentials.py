from dotenv import load_dotenv
import os


def get_credentials():
    load_dotenv()
    login = os.environ.get('login')
    password = os.environ.get('password')
    return login, password


if __name__ == '__main__':
    print(get_credentials())
