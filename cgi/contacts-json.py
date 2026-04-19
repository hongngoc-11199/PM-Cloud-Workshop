#!/usr/bin/python3

import pymysql
import json

print("Content-Type: application/json")
print()

conn = pymysql.connect(
    host="localhost",
    user="testuser",
    password="1234",
    database="contacts_db"
)

cursor = conn.cursor()
cursor.execute("SELECT name, phone, email FROM contacts")

data = []
for name, phone, email in cursor.fetchall():
    data.append({
        "name": name,
        "telephone": phone,
        "email": email
    })

print(json.dumps({
    "ok": True,
    "data": data
}))
