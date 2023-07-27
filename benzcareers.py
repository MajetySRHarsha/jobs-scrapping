import sqlite3
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify
import psycopg2
from database import create_table,insert_to_table


def scrape_benz():
    response = requests.get('https://jobs.lever.co/MBRDNA')
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs=soup.findAll("div",{"class":"postings-group"})
    create_table()
    for job in jobs:
        temp=job.find("div",{"class":"posting"})
        temp2=temp.find("a",{"class":"posting-title"})
        link=temp2["href"]
        h5_tag = temp.find('a', class_='posting-title').find('h5', {'data-qa': 'posting-name'})
        role=h5_tag.text.strip()
        location_element = temp.find('span', class_='sort-by-location posting-category small-category-label location')
        place=location_element.text.strip()
        commitment_element = temp.find('span', class_='sort-by-commitment posting-category small-category-label commitment')
        if(commitment_element==None):
            position='Intern'
        else:
            postion=commitment_element.text.strip()
        insert_to_table(role, place, link, postion, 'Benz')
    return "Done"