import socket
import threading
import csv
import mysql.connector
import pickle


HOST = "127.0.0.1"
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

FORMAT = "utf-8"

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='CST1510_DATABASE'
)

mycursor = mydb.cursor(buffered=True)


def chat():
    s.listen()
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=message_broadcast, args=(conn, addr))
        thread.start()


def message_broadcast(conn, addr):
    print(f"CONNECTED: {addr}")
    connected = True

    while connected:
        motor_list = ["2L-T", "2JZ", "3L", "5L", "3S", "3M"]
        data_variable = conn.recv(1024)
        data = pickle.loads(data_variable)
        file_write(motor_list, data)

        for i in range(len(motor_list)):
            mycursor.execute("""SELECT quantity FROM stock WHERE product_name = '%s' """ % (motor_list[i]))
            result = mycursor.fetchone()
            quantity = result[0]

            new_quantity = quantity - int(data[i])

            mycursor.execute("""UPDATE stock SET quantity = '%s' WHERE product_name = '%s' """ % (new_quantity, motor_list[i]))

            mydb.commit()

        print(data)
        del data
        del quantity
        del new_quantity

        connected = False

    conn.close()

def file_write(motor_list, data):
    with open("cst1510_data", 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        for v in range(len(motor_list)):
            if data[v] == 0:
                continue
            else:
                csvwriter.writerow((motor_list[v], data[v]))


chat()
