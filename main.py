from database import createTable, addPassword, showAllRecords, showPasswordForWebsite, showAllPasswordForEmail

from passwords import authenticate, encrypt_password, decrypt_password

def startup():
  print('Welcome to your own personal Password Manager!')
  
  return authenticate()


def print_details(list):
  print('\n' + ('-'*20))

  for record in list:
    print(f"Username: {record[1]}")
    decrypted = decrypt_password(record[2])
    print(f"Password: {decrypted}")
    print(f"Email: {record[3]}")
    print(f"Website: {record[4]}")

  print('-'*20)

def menu():
  print('\n1. Add new password')
  print('2. See password for a website')
  print('3. See all passwords attached to an email')
  print('4. See all passwords')
  print('0. Exit')

  i = input('\nSelect option from main menu (1/2/3/4/0): ')

  if i == '0': exit()

  return i

  

def main():
  
  # create password table if it doesn't exist
  createTable()
  
  # authenticate the user
  auth = startup()

  while True:
    m = 0

    if auth:
      m = menu()
    else:
      print("Wrong Password! Exiting...")
      exit()
    
    if m == '1':
      print('Please add following details: ')
      email = input('Email address: ')
      website = input('Website Name: ')
      username = input('Username: ')
      password = input('Password: ')

      encrypt_pass = encrypt_password(password)

      addPassword(username, encrypt_pass, email, website)

      print('\nPassword successfully added!')

    if m == '2':
      website = input('Enter website name: ')
      records = showPasswordForWebsite(website)
      print_details(records)

    if m == '3':
      email = input('Enter email address: ')
      records = showAllPasswordForEmail(email)
      print_details(records)
      

    if m == '4':
      records = showAllRecords()
      print_details(records)



if __name__ == '__main__':
  main()