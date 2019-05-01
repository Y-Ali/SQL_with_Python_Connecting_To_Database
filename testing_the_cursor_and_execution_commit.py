import pyodbc

# variables to create a connection
server = 'localhost,1433'
database = 'homework_db'
username = 'SA'
password = 'Passw0rd2018'

## making a connection
docker_homework_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'
                                  ';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

#creating a cursor that can execute SQL functions on connected db
cursor = docker_homework_db.cursor()

# INSERT INTO Function :
def save_datails(movie_title, movie_genre, movie_rating, movie_producer):
    try:
        query = (f"INSERT INTO Movie_table (movie_title, movie_genre, movie_rating, movie_producer) VALUES ('{movie_title}', '{movie_genre}', '{movie_rating}', '{movie_producer}')")
        #print(query)
        cursor.execute(query)
        docker_homework_db.commit()
        print("Successfully inserted values into the table")

    except Exception as ermsg:
        print("PANIC")
        print(ermsg)
        raise

save_datails("Iron Man", "Action", 5.0, "John")


