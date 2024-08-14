from fastapi import FastAPI
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

userenv = os.getenv('PMA_USER')
passwordenv = os.getenv('PMA_PASSWORD')
hostenv = os.getenv('PMA_HOST')
portenv = os.getenv('PMA_PORT')
databaseenv = os.getenv('MYSQL_DATABASE')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/employees")
async def get_employees():
    connection = mysql.connector.connect(
        user=userenv,
        password=passwordenv,
        host=hostenv,
        port=portenv,
        database=databaseenv
    )
    print('DB connected')
    cursor = connection.cursor(dictionary=True)
    cursor.execute('Select * FROM employees')
    employees = cursor.fetchall()
    datas = []
    for employee in employees:
        print(employee)
        data = {
            "first_name": employee["first_name"],
            "last_name": employee["last_name"],
            "email": employee["email"],
            "department": employee["department"]
        }
        datas.append(data)
    connection.close()
    print('DB closed')
    return { 'employees' : datas }