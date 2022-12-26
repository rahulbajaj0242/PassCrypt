import psycopg2
import maskpass

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
  print('1. Add new password')
  print('2. See all passwords')
  print('0. Exit')

  i = input('Select option from main menu (1/2/0): ')

  if i == '3': exit()

  return i

  

def main():
  
  try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres' port='5432'")

    cur = conn.cursor()

    # create a table called passwords with fields id, username, password and website
    # cur.execute('CREATE TABLE passwords(id serial PRIMARY KEY, username varchar(255), password varchar(255), website varchar(255));')

    auth = startup()
    m = menu() if auth == '1' else print("Wrong Password! Exiting...")

    if m == '1':
      print('Please add following details: ')
      website = input('Website Name: ')
      username = input('Username: ')
      password = input('Password: ')

      cur.execute(f'INSERT INTO passwords(username, password, website) VALUES(%s, %s, %s);', (username, password, website))


    if m == '2':
      cur.execute('SELECT * FROM passwords;')
      data = cur.fetchall()
      print(data)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

  except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)



if __name__ == '__main__':
  main()