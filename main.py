from bs4 import BeautifulSoup
#import pandas as pd
import requests
import sys
import csv

def get_url(url: any) -> str:
    try:
        response = requests.get(url)
        return response
    except:
        print('Invalid url, please try again.')
        sys.exit()


def main():
    res = get_url(sys.argv[1])
    if (res.status_code != 200):
        print(f"Error getting news. status code is {res.status_code}")
        if (res.status_code == 404):
            print("Page not found.")
        else:
            print("Please try again.")

def parse():
    main()
    print(sys.argv[1])
    res = get_url(sys.argv[1])
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup

def convert_csv():
    soup = parse()

    headline = soup.find(attrs={"data-qa": "headline-text"}).get_text()
    author = soup.find(attrs={'data-qa': "author-name"}).get_text()
    timestamp = soup.find(attrs={'data-testid' or 'data-qa': "timestamp"}).get_text()
    content_tag = soup.find_all(attrs={'data-el': "text"})

    content = ""
    for part in content_tag:
        content += "\n\n" + part.get_text()
    data = [headline, author, timestamp, content]

    with open('scrape.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Headline', 'Author', 'Timestamp', 'Content'])
        writer.writerow(data)

convert_csv()