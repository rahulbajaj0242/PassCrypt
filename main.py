import psycopg2


try:

  conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres' port='5432'")


  cur = conn.cursor()

# Execute a command: this creates a new table
  cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
  cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Query the database and obtain data as Python objects
  cur.execute("SELECT * FROM test;")
  cur.fetchone()
  (1, 100, "abc'def")

# Make the changes to the database persistent
  conn.commit()

# Close communication with the database
  cur.close()
  conn.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)