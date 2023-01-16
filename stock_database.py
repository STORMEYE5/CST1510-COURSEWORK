import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='CST1510_DATABASE'
)

mycursor = mydb.cursor(buffered=True)

table_create = "CREATE TABLE stock (product_name VARCHAR(255), quantity INTEGER, price INTEGER)"
table_delete = "DROP TABLE stock"

value_insert = "INSERT INTO stock (product_name, quantity, price) VALUES (%s, %s, %s)"

# "2L-T", "2JZ", "3L", "5L", "3S", "3M"
stock = [
  ("2L-T", 1000, 250),
  ("2JZ", 1000, 1000),
  ("3L", 1000, 450),
  ("5L", 1000, 780),
  ("3S", 1000, 620),
  ("3M", 1000, 650)
]

# mycursor.execute(table_create)
# #
# mycursor.executemany(value_insert, stock)

mycursor.execute("SELECT quantity FROM stock where product_name = 'clothes'")
j = "bed_sheets"
i=1000
mycursor.execute("""SELECT quantity FROM stock""")
results = mycursor.fetchall()
output = results[0]
print(results)
#
# if results[0] > i:
#   print("greater")

mydb.commit()
