import mysql.connector
import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image
import pytesseract
import re
from mysql.connector import pooling

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

loginStatus = True

def verifyLoginStatus():
    return loginStatus

def verifyLogin(email: str, password: str):

    # Attempt connection to Oracle db.
    try: 
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DlGkS!2#4%",
        database="solohack"
        )
        print("Connected to database")
    except:
        print("Was not able to connect to database")
    print("debug1")
    cur = connection.cursor()
    print("debug2")
    # Check if the user even exists
    select_stmt = "select * from users where email = %(email)s"
    cur.execute(select_stmt, { 'email': email })
    print("debug3")
    number = cur.fetchall() 
    if (len(number) != 1):
        print("User with email does not exist")
        return None
    select_stmt = "select * from users where email = %s and password = %s"
    cur.execute(select_stmt, (email, password))
    user = cur.fetchall()
    cur.close()
    connection.close()
    if (len(user) != 1):
        print("Password does not match, try again")
        return None
    print("Successfully verified user")
    return user
def login(email, password):

    user = verifyLogin(email, password)

    if user is None:
        st.write("Your email and/or password are incorrect")

    else:

        user_email = user[0][0]

        st.experimental_set_query_params(user="user", email=user_email)

        st.write("You are logged in")

        loginStatus = True

def addUser(email: str, password: str) -> str:

    #hashedEmail = hashCode(email).hexdigest()
    #hashedPassword = hashCode(password).hexdigest()

    # Attempt connection to Oracle database.
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DlGkS!2#4%",
        database="solohack"
        )
        print("Connected to database")

    except:
        print("Was not able to connect to the database.")
    cur = connection.cursor()
    try:
        select_stmt = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cur.execute(select_stmt, (email, password))
        connection.commit()
        output = "Added user into database"
    except:
        output = "Unsuccessful"  
    cur.close()  
    connection.close()
    return output

def addExpression(email: str, password: str) -> str:

    #hashedEmail = hashCode(email).hexdigest()
    #hashedPassword = hashCode(password).hexdigest()

    # Attempt connection to Oracle database.
    try:
        connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="DlGkS!2#4%",
        database="solohack"
        )
        print("Connected to database")

    except:
        print("Was not able to connect to the database.")
    cur = connection.cursor()
    try:
        select_stmt = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cur.execute(select_stmt, (email, password))
        connection.commit()
        output = "Added user into database"
    except:
        output = "Unsuccessful"  
    cur.close()  
    connection.close()
    return output