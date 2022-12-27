import os
import bcrypt
import dotenv
from cryptography.fernet import Fernet
from dotenv.main import load_dotenv



def hash_password(pas):
  bytes = pas.encode('utf-8')
  salt = bcrypt.gensalt()

  hash = bcrypt.hashpw(bytes, salt)

  return hash



def check_master_password():
  user_pass = input("First, authenticate yourself\nEnter master password: ")

  user_bytes = user_pass.encode('utf-8')

  master_password_bytes = os.environ['MASTER'].encode('utf-8')

  result = bcrypt.checkpw(user_bytes, master_password_bytes)

  return result


def create_master_password():
  mas_pass = input('First, Choose a master password which will be used for authentication and password recovery\nMaster Password: ')
  
  # Hash the password first before saving it in the env file
  hash_mas_pass = hash_password(mas_pass).decode()

  # add hashed password to environment variables and then add it into pass.env file
  os.environ['MASTER'] = hash_mas_pass
  dotenv.set_key('pass.env', 'MASTER', os.environ['MASTER'])


def authenticate():
  found_dotenv = os.path.exists('pass.env')

  if not found_dotenv:
    print('Looks like you\'re a new user!')
    
    # create pass.env file
    with open('pass.env', 'a') as file:
      pass
    
    # create new master password
    create_master_password()
    return True

  else:
    load_dotenv('pass.env')
    auth = check_master_password()

    return auth