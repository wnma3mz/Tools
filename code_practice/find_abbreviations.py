# coding: utf-8
import os
import argparse
import requests
from bs4 import BeautifulSoup as bs


parser = argparse.ArgumentParser(description='Find Abbreviations')
parser.add_argument('-q', '--query', type=str, 
                    help='the abbreviation what want to find')
parser.add_argument('-m', '--method', type=str, choices=['web', 'uid_token'], default='uid_token', 
                    help='the search method')

args = parser.parse_args()

def web(query):
    url = 'https://www.abbreviations.com/{}'

    html = requests.get(url.format(query)).text
    soup = bs(html, 'lxml')
    data = soup.find(class_='table tdata no-margin').find_all('tr')
    text = [line.find_all('td')[1].text.replace('»', '>') for line in data]
    return text

def uid_token(query):
    url = 'https://www.abbreviations.com/services/v2/abbr.php?uid=7241&tokenid=lNsBjsSApKzOvOaM&term={}&format=json'
    
    data = requests.get(url.format(query)).json()['result']
    text = list(map(lambda item: item['definition'] + ' > ' + item['category'], data))
    return text

def print_text(text):
    for id_, line in enumerate(text):
        print('{:2d} {}'.format(id_, line))

if args.method == 'uid_token':
    text = uid_token(args.query)
elif args.method == 'web':
    text = web(args.query)
print_text(text)