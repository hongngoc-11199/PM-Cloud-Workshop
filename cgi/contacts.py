#!/usr/bin/env python3

print("Content-Type: text/html\n")

print("<html><body>")
print("<h1>Contact List</h1>")
print("<ul>")

with open("/usr/lib/cgi-bin/contacts.txt") as f:
    for line in f:
        name, phone = line.strip().split(":")
        print(f"<li>{name} - {phone}</li>")

print("</ul>")
print("</body></html>")
