import psycopg2
import maskpass
from database import createTable, addPassword, showAllRecords, showPasswordForWebsite, showAllPasswordForEmail

master_password = "secretpassword"

def startup():
  print('Welcome to your own personal Password Manager!')
  print('\n\nFirst, Please add the master password to authenticate yourself: ', end='')
  i = maskpass.askpass()

  if(i == master_password):
    return '1'
  else:
    return '0'


def menu():
  print('\n1. Add new password')
  print('2. See password for a website')
  print('3. See all passwords attached to an email')
  print('4. See all passwords')
  print('0. Exit')

  i = input('\nSelect option from main menu (1/2/3/4/0): ')

  if i == '0': exit()

  return i


# def encryptPassword(password):
#   pass

  

def main():
  
  createTable()
  
  auth = startup()

  while True:
    m = menu() if auth == '1' else print("Wrong Password! Exiting...")
    
    if m == '1':
      print('Please add following details: ')
      email = input('Email address: ')
      website = input('Website Name: ')
      username = input('Username: ')
      password = input('Password: ')

      # updatedPassword = encryptPassword(password)

      addPassword(username, password, email, website)

      print('\nPassword successfully added!')

    if m == '2':
      website = input('Enter website name: ')
      records = showPasswordForWebsite(website)
      print(records)

    if m == '3':
      email = input('Enter email address: ')
      records = showAllPasswordForEmail(email)
      print(records)

    if m == '4':
      data = showAllRecords()
      print(data)



if __name__ == '__main__':
  main()