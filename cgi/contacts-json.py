#!/usr/bin/env python3

import pymysql
import json

print("Content-Type: application/json")
print()

response = {
    "ok": True,
    "count": 0,
    "data": []
}

try:
    conn = pymysql.connect(
        host="localhost",
        user="testuser",
        password="1234",
        database="contacts_db",
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, email FROM contacts")
    for name, phone, email in cursor.fetchall():
    response["data"].append({
        "name": name,
        "telephone": phone,
        "email": email
    })
    rows = cursor.fetchall()

    for name, phone in rows:
        response["data"].append({
            "name": name,
            "telephone": phone
        })

    response["count"] = len(response["data"])

    conn.close()

except Exception as e:
    response = {
        "ok": False,
        "error": str(e)
    }

print(json.dumps(response, ensure_ascii=False))
