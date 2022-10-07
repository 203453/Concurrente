from mimetypes import init
from urllib import response
import requests
import time
import psycopg2

def service():
    print("Hola Service")
    get_service()
    

def get_service():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    if response.status_code == 200 :
        data = response.json()
        write_db(data)

    else:
        print('Error')

def connect_db():
    con = psycopg2.connect(database="concurrente", user="postgres", password="emi203453", host="localhost", port="5432")
    print("Database opened successfully")
    con.autocommit = True
    return con

def write_db(data):
    
    print(data)
    connection = connect_db()

    cursor = connection.cursor()

    for dataOut in data:
        title = dataOut['title']
        query = f""" INSERT INTO test (title) VALUES ('{title}') """
        cursor.execute(query)

if __name__ == "__main__":
    init_time = time.time()
    service()   
    end_time = time.time() - init_time
    print(end_time)