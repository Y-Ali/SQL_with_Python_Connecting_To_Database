# import pyodbc
#
# # variables to create a connection
# server = 'localhost,1433'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
#
# ## making a connection
# northwind_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}'
#                                   ';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#
# #creating a cursor that can execute SQL functions on connected db
# cursor = northwind_db.cursor()
# #cursor.execute("SELECT ContactName FROM Customers WHERE Country = 'Germany';")
# #row = cursor.fetchall()
#
#
# column = cursor.description
#
# def get_country(country):
#     cursor.execute( "SELECT ContactName FROM Customers WHERE Country =" + "'" + country + "'" )
#     row = cursor.fetchall()
#     for item in row:
#         print(item[0])
#         #print(item)
#
# get_country("Austria")
#
