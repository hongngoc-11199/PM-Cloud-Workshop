#!/usr/bin/env python3

import pymysql

print("Content-Type: text/html")
print()

print("<html>")
print("<body>")
print("<ul>")

try:
    conn = pymysql.connect(
        host="localhost",
        user="testuser",
        password="1234",
        database="contacts_db",
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT name, phone FROM contacts")

    rows = cursor.fetchall()

    if not rows:
        print("<li>No data found</li>")
    else:
        for name, phone in rows:
            print(f"<li>{name} - {phone}</li>")

    conn.close()

except Exception as e:
    print("<li>Error occurred:</li>")
    print(f"<li>{e}</li>")

print("</ul>")
print("</body>")
print("</html>")
