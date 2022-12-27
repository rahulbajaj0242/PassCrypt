import os
import bcrypt
from cryptography.fernet import Fernet
from dotenv.main import load_dotenv


def hash_password(pas):
  




def create_master_password():
  mas_pass = input('First, Choose a master password which will be used for authentication and password recovery\nMaster Password: ')
  
  # create pass.env file
  with open('pass.env') as reader:
    pass

  hash_mas_pass = hash_password(mas_pass)
  


def check_env_file():
  file_exists = os.path.exists('pass.env')

  if not file_exists:
    print('Looks like you\'re a new user!')
    create_master_password()
