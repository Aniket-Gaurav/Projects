import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrap(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize an empty list to store tuples of (link text, href)
    links = [(link.text.strip(), link.get('href')) 
             for link in soup.find_all('a')]
    
    return links

if __name__ == "__main__":
    url = 'https://linktr.ee/hiten.codes'
    links = scrap(url)

    df = pd.DataFrame(links, columns=['Text','Link'])
    df.to_csv('Links.csv', index=False)