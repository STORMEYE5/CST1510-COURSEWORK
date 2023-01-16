import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='CST1510_DATABASE'
)

mycursor = mydb.cursor(buffered=True)

table_create = "CREATE TABLE employees (name VARCHAR(255), password VARCHAR(255))"

value_insert = "INSERT INTO employees (name, password) VALUES (%s, %s)"

employee = [
  ('Peter', 'peter1234'),
  ('Anna', 'anna1234'),
  ('Paul', 'paul1234')
]

mycursor.execute(table_create)

mycursor.executemany(value_insert, employee)

mycursor.execute("SELECT * FROM employees")
results = mycursor.fetchall()
print(results)

mydb.commit()
