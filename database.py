import psycopg2 


def connection():
  try:
    conn = psycopg2.connect("dbname='test' user='test' host='localhost' password='test' port='5432'")
  except Exception as e:
    print(e)

  return conn

def createTable():
  conn = connection()
  cur = conn.cursor()

  cur.execute('CREATE TABLE IF NOT EXISTS passwords(id serial PRIMARY KEY, username varchar(255) NOT NULL, password varchar(255) NOT NULL, email varchar(255), website varchar(255) NOT NULL);')

  conn.commit()
  cur.close()
  conn.close()

def addPassword(username, password, email, website,):
  conn = connection()
  cur = conn.cursor()

  cur.execute('INSERT INTO passwords(username, password, email,  website) VALUES(%s, %s, %s, %s);', (username, password, email, website))

  conn.commit()
  cur.close()
  conn.close()

def showPasswordForWebsite(website):
  conn = connection()
  cur = conn.cursor()

  cur.execute('SELECT password FROM passwords WHERE WEBSITE LIKE %s', (website,))
  records = cur.fetchall()

  cur.close()
  conn.close()

  return records

def showAllPasswordForEmail(email):
  conn = connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM passwords WHERE email LIKE %s', (email,))
  records = cur.fetchall()

  cur.close()
  conn.close()

  return records

  
def showAllRecords():
  conn = connection()
  cur = conn.cursor()

  cur.execute('SELECT * FROM passwords;')
  records = cur.fetchall()

  cur.close()
  conn.close()

  return records