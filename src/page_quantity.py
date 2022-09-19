import requests
from bs4 import BeautifulSoup as BS


# this url resirect us to last page

max_url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{}/c37l1700273'.format(999)

def get_pages_quantity(url, headers):
    """ We can take selected page from bottom nav-bar and use this number for async loop later """

    html = requests.get(url, headers)
    soup = BS(html.text, 'html.parser')
    pages = soup.find('div', class_='bottom-bar').find('div', class_='pagination').find('span', class_='selected').get_text(strip=True)
    print (f'[INFO] {pages} pages was found, starting ...')
    return (int(pages))


