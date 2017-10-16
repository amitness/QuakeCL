#!/usr/bin/env python3
'''
Get details of recent earthquakes occurred in Nepal.
Author: Amit Chaudhary
'''
from datetime import date
from urllib.request import urlopen

SHEET_ID = '1eeIOB58Dn5qRNWTySqrL35U8xY3JjZ7yhg5Dpxvbz8s'
SHEET_URL = 'https://docs.google.com/spreadsheets/u/0/d/{}/export?format=csv'


def get_page(url):
    try:
        return urlopen(url).read().decode('utf-8')
    except:
        return None


def create_dictionary(data):
    sheet = []
    rows = data.splitlines()
    for row in rows:
        cells = row.split(',')
        sheet.append({'date': convert_to_date(cells[0]),
                      'time': cells[1],
                      'magnitude': cells[2],
                      'location': cells[3]})
    return sort_by_date(sheet)


def sort_by_date(rows):
    return sorted(rows, key=lambda row: row.get('date'), reverse=True)


def convert_to_date(text):
    """Convert date in Y-M-D to date object."""
    year, month, day = map(int, text.split('-'))
    return date(year, month, day)


def main():
    data = get_page(SHEET_URL.format(SHEET_ID))
    if data:
        details = create_dictionary(data)
        today = date.today()
        print(today.strftime('Today: %B %d, %Y'))
        last_quake = details[0]['date']
        delta = (today - last_quake).days
        print('Last Earthquake: {} days ago'.format(delta))
        print
        headers = ['Date', 'Time', 'Magnitude', 'Location']
        row = '{:>15s} {:>15s} {:>15s} {:>15s}'
        print(row.format(*headers))
        for detail in details:
            fields = (detail['date'].strftime('%b %d, %Y'), detail['time'],
                      detail['magnitude'], detail['location'])
            print(row.format(*fields))
    else:
        print('Please check your internet connection.')

if __name__ == '__main__':
    main()
