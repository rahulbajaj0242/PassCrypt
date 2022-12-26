import psycopg2




def main():
  
  try:
    conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres' port='5432'")

    cur = conn.cursor()

    # cur.execute('CREATE TABLE password(id serial PRIMARY KEY, )')



    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

  except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)






if __name__ == '__main__':
  main()