import requests
import selectorlib
from emailing import send_email
import time
import sqlite3

URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")
def scrap(url):
    response = requests.get(url,headers = HEADERS)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file('extract.yaml')
    value = extractor.extract(source)['tours']
    return value


def store(extracted):
    row  = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)",row)
    connection.commit()


def read(extracted):
    row  = extracted.split(",")
    row = [item.strip() for item in row]
    band,city,date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?",(band,city,date))
    rows = cursor.fetchall()
    print(rows)
    return rows

while True:

    scraped = scrap(URL)
    extracted = extract(scraped)
    print(extracted)
    
    if extracted != "No upcoming tours":
        row = read(extracted)
        if not row:  #check the list is empty or not
            store(extracted)
            send_email(message= "Hey New Event is Just added")
    time.sleep(2)
