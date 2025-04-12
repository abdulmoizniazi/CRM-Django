import mysql.connector
# print(f"Connector version: {mysql.connector.__version__}")
print(f"Available attributes: {dir(mysql.connector)}")

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin'
)

cursorObject = dataBase.cursor()

cursorObject.execute("SHOW DATABASES")
databases = [db[0] for db in cursorObject.fetchall()]

if "elderco" not in databases:
    cursorObject.execute("CREATE DATABASE elderco")
    print("Database 'elderco' created.")
else:
    print("Database 'elderco' already exists.")
