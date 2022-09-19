from bs4 import BeautifulSoup as BS
import asyncio

from convert_date import get_correct_date
from settings import headers
from alt_database import add_data_to_database


def get_image(card):
    try:
        img_box = card.find('div', class_='left-col').find('div', class_='image')
        img = img_box.find('picture')
        try:
            image = img.find('source').get('data-srcset')
        except AttributeError:
            image = 'null'
        return image
    except:
        print("Info wsn't fount")
        return 'No info'


def get_title(info_box):
    try:
        title = info_box.find('div', 'title').get_text(strip=True)    
        return title
    except:
        print("Info wsn't fount")
        return 'No info'

def get_location(info_box):
    try:
        title = info_box.find('div', 'location').find('span').get_text(strip=True)    
        return title
    except:
        print("Info wsn't fount")
        return 'No info'

def get_posted_date(info_box):
    try:
        posted = info_box.find('div', 'location').find('span', class_='date-posted').get_text(strip=True) 
        return get_correct_date(posted)
    except:
        print("Info wsn't fount")
        return 'No info'

def get_bathrooms(card):
    try:
        bedrooms = card.find('div', class_='rental-info').find('span', class_='bedrooms').get_text(strip=True)
        beds = bedrooms.replace('\n', '').replace(' ', '')
        return beds
    except AttributeError:
        print("Info wsn't fount")
        return 'No info'

def get_description(info_box):
    try:
        description = info_box.find('div', class_='description').get_text(strip=True)
        return description
    except:
        print("Info wsn't fount")
        return 'No info'

def get_price(info_box):
    try:
        full_price = info_box.find('div', class_='price').get_text(strip=True)
        if full_price[0].isalpha():        
            return (None, full_price)
        if full_price[0] == '$':
            currency = 'CAD'
        else:
            currency = full_price[0]
        price = full_price[1:]
        return (currency, price)
    except:
        print("Info wsn't fount")
        return 'No info'
    
db = []
def get_content(soup):
    items = soup.find_all('div', class_='search-item')

async def get_page_data(session, tasks: list, page_id: int):
    url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{}/c37l1700273'.format(page_id)
    async with session.get(url, headers=headers) as resp:
        if resp.status == 200:
            print(f'get url: {url} || status {resp.status}')
            resp_text = await resp.text()
            try:
                soup = BS(resp_text, 'html.parser')
                items = soup.find_all('div', class_='search-item')
            except:
                print('WTF ? ? ? ')

            for el in items:
                db.append(el)
                
                try:
                    card = el.find('div', class_='clearfix')
                    info_box = card.find('div', class_='info').find('div', class_='info-container')

                    data = {
                        'image': get_image(card),
                        'title': get_title(info_box),
                        'location': get_location(info_box),
                        'published_date': get_posted_date(info_box),
                        'bedrooms': get_bathrooms(card),
                        'description': get_description(info_box),
                        'full_price': get_price(info_box)
                    }

                    add_data_to_database(data)

                except Exception as ex:
                    print('icant beelive', ex)

        else:
            print(resp.status)

        

