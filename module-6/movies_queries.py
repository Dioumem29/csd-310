import mysql.connector
from getpass import getpass

# Connect to the movies database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=getpass("Enter MySQL password: "),
    database="movies"
)

print("Successfully connected to MySQL!")

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Query 1: Retrieve all studio records
cursor.execute("SELECT * FROM studio")

# Retrieve the query results
studios = cursor.fetchall()

print("\n-- DISPLAYING Studio RECORDS --")

# Display each studio
for studio in studios:
    print("Studio ID:", studio[0])
    print("Studio Name:", studio[1])
    print()
#create a new cursor to execute the next query
cursor = db.cursor()
# Query 2: Retrieve all genre records
cursor.execute("select * from genre")

# Retrieve the query results
genres = cursor.fetchall()

print("\n-- DISPLAYING Genre RECORDS --")

# Display each genre
for genre in genres:
    print("Genre ID:", genre[0])
    print("Genre Name:", genre[1])
    print()

#create a new cursor to execute the next query
cursor = db.cursor()
# Query 3: Retrieve all movie under 2hours
cursor.execute("select film_name, film_runtime from film where film_runtime < 120")

# Retrieve the query results
movies = cursor.fetchall()

print("\n-- DISPLAYING Short Film RECORDS --")

# Display each movie
for movie in movies:

    print("Movie Title:", movie[0])
    print("Runtime:", movie[1])
    print()

#create a new cursor to execute the next query
cursor = db.cursor()
#retieve all movie by director
cursor.execute("select film_name, film_director from film order by film_director")

# Retrieve the query results
directors = cursor.fetchall()

print("\n-- DISPLAYING Director RECORDS in Order --")

# Display each movie by director
for director in directors:
    print("Movie Title:", director[0])
    print("Director:", director[1])
    print()

# Close the cursor and database connection
cursor.close()
db.close()


