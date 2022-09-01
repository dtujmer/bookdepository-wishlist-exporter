import requests
from bs4 import BeautifulSoup
import sys

books = []

def scrape():
    for num in range(1, 4):
        url = sys.argv[1] + f"?page={num}"
        r = requests.get(url)
        content = r.content
        soup = BeautifulSoup(content, 'html.parser')

        for book in soup.find_all('div', class_="book-item"):
            name = book.find_all(itemprop="name")[0].get("content")
            author = book.find_all(itemprop="contributor")[0].get("content")
            books.append((name, author))

scrape()


for pair in books:
    print("- " + pair[0] + ", " + pair[1])
