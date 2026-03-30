import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",   
    port=3306
)
cursor = conn.cursor()

# 2. Database & Table Setup
cursor.execute("CREATE DATABASE IF NOT EXISTS sqlproject")
cursor.execute("USE sqlproject")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20),
        age INT,
        course VARCHAR(50)
    )
""")

def add_student():
    name = input("Enter Name: ")
    age = int(input('Enter age: '))
    course = input("Enter course: ")
    query = "INSERT INTO students(name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(query, values)
    conn.commit()
    print("Student Added Successfully!")

def view_student():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    print("\n--- Student List ---")
    for row in data:
        print(row)
    print("--------------------\n")

def update_student():
    student_id = int(input('Enter Student ID to Update: '))
    name = input("Enter New Name: ")
    query = "UPDATE students SET name = %s WHERE id = %s"
    values = (name, student_id)
    cursor.execute(query, values)
    conn.commit()
    print("Student updated successfully!")

def delete_student():
    id = int(input("Enter Student ID to Delete: "))
    query = "DELETE FROM students WHERE id = %s"  
    values = (id,)
    cursor.execute(query, values)
    conn.commit()
    print("Student Deleted")

while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()           
    elif choice == 2:
        view_student()
    elif choice == 3:           
        update_student()        
    elif choice == 4:
        delete_student()        
    elif choice == 5:
        print("Goodbye!")
        break                   
    else:
        print("Invalid choice. Please enter 1-5.")