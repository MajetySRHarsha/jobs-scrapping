import sqlite3
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import psycopg2

connection_url="postgres://ccedeshe:3zrgNOufP52EUgDfwliIhQzb4SMBAJAE@snuffleupagus.db.elephantsql.com/ccedeshe"
connection = psycopg2.connect(connection_url)
cursor = connection.cursor()
def create_table():
    print("hello")
    create_table_query = """
    CREATE TABLE IF NOT EXISTS careers (
        job_title TEXT,
        location TEXT,
        job_description_link TEXT,
        job_type TEXT,
        company_name TEXT
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()
    return "Success"

def check_duplicates(cursor, role, place, link, job_type, company_name):
        select_query = """
            SELECT * FROM Careers
            WHERE job_title = %s AND location = %s AND job_description_link = %s
            AND job_type = %s AND company_name = %s;
        """
        cursor.execute(select_query, (role, place, link, job_type, company_name))
        result = cursor.fetchone()
        if result is not None:
            print("Duplicate entry found.")
            return True
        else:
            print("No duplicate entry found.")
            return False
        
def insert_to_table(role, place, link, job_type, company_name):
        if check_duplicates(cursor, role, place, link, job_type, company_name):
            print("Duplicate entry found. Skipping insertion.")
        else:
            insert_query = """
                INSERT INTO careers (job_title, location, job_description_link, job_type, company_name)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (role, place, link, job_type, company_name))
            connection.commit()

def fetch_jobs(company_name):
    if(company_name=='Airbnb'):
        select_query = """
                SELECT * FROM Careers
                WHERE company_name = 'Airbnb';
            """
    elif(company_name=='Benz'):
        select_query = """
                SELECT * FROM Careers
                WHERE company_name = 'Benz';
            """
    elif(company_name=='intern'):
         select_query = """
                SELECT * FROM Careers
                WHERE job_type = 'Intern';
            """
    elif(company_name=='FullTime'):
         select_query = """
                SELECT * FROM Careers
                WHERE job_type = 'Full-time';
            """     
    elif(company_name=='Contractor'):
         select_query = """
                SELECT * FROM Careers
                WHERE job_type = 'Contractor';
            """     
    
    else:
         select_query = """
                SELECT * FROM Careers;
            """
         
    cursor.execute(select_query)
    rows = cursor.fetchall()
    jobs = [
            {
                "job_title": row[0],
                "location": row[1],
                "job_description_link": row[2],
                "job_type": row[3],
                "company_name": row[4]
            }
            for row in rows
        ]
        
    return jobs
