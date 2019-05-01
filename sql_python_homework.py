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
# cursor.execute("SELECT * FROM Movie_table;")
#
# column = cursor.description

# row = cursor.fetchall()
# index = 0
# for item in row:
#     #print(item)
#     print(column[0][0],":",item.movie_title, column[1][0],":",item.movie_genre, column[2][0],":",item.movie_rating, "   ",column[3][0],":",item.movie_producer)
#     index = index + 1

