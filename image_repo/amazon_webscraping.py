import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pprint
import sqlite3
import json


def get_url(search):
    '''return full amazon url from search term'''
    search = search.replace(' ', '+')
    template = 'https://www.amazon.ca/s?k={}&ref=nb_sb_noss'
    full_url = template.format(search)
    return full_url

def get_items_from_url(url):
    '''get list of items from full amazon url'''
    driver.get(get_url(url))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type':"s-search-result"})
    return results

def get_item_attributes(item):
    '''return attributes in a dictionary from amazon item after item has been identified'''
    global error
    #data structure to store item attributes
    item_info = {}
    #item description and url
    try:
        atag = item.h2.a
        item_info['description']= atag.text.strip()[:50]
    except:
        print('something wrong with description, likely encoding')
        error += 1
        return None
    # where you go if you click on this link
    try:
        item_info['url'] = 'https://www.amazon.ca/'+ atag.get('href')
    except:
        error += 1
        return None
    # box containing price
    try:
        price_cover = item.find('span', 'a-price')
        item_info['price'] = price_cover.find('span', 'a-offscreen').text
    except AttributeError:
        error += 1
        print('had no price here')
        return None
    try:
        item_info['rating'] = item.find('i', 'a-icon-star-small').text
    except AttributeError:
        error += 1
        print('had no star rating here')
        return None
    try:
        item_info['num_reviews'] = int(item.find('span', {'class': "a-size-base"}).text.replace(',', ''))
    except AttributeError:
        error += 1
        print('had no numbe of reviews here')
        return None
    except:
        print('something else wrong with the review number')
        return None
    try:
        item_info['image_url'] = item.find('img', {'class':'s-image'})['src']
    except AttributeError:
        error += 1
        print('had no numbe of reviews here')
        return None
    return item_info

def attributes_for_all_items(items):
    '''return list of item attribute dictionaries from list of items'''
    item_attributes = []
    i = 0
    print(f'there are {len(items)} items')
    for item in items:

        i += 1
        attributes = get_item_attributes(item)
        # attributes is None if an item does not have all the properties we want as seen in get_item_attributes(item)
        #skip the ones that are None
        if attributes:
            item_attributes.append(attributes)
    return item_attributes

def get_page_results(search):
    '''returns list of item attributes in dictionary for page of amazon given search string'''
    # get the full search url
    full_url = get_url(search)
    # get a list of front page items
    items = get_items_from_url(full_url)
    #retrieve attributes for each item, put in dictionary, collect all in a list
    item_list = attributes_for_all_items(items)
    # Prints the nicely formatted dictionary
    # SOME ITEMS CANT BE PRINTED WITH WEIRD CHARACTERS BE CAREFULL PRINTING
    return item_list

def get_all_from_list(list_of_clothes):
    '''returns list of all attributes for all items in input list of strings'''
    all_items = []
    for item in list_of_clothes:
        # print(item)
        all_items += get_page_results(item)

    return all_items

# def create_table(cur, con):
#     cur.execute('''CREATE TABLE items
#                     (id INTEGER,
#                     name text NOT NULL,
#                     image_url text NOT NULL,
#                     num_reviews int NOT NULL,
#                     price text NOT NULL,
#                     rating text NOT NULL,
#                     item_url text NOT NULL,
#                     tags text,
#                     PRIMARY KEY(id))''')
#     con.commit()
#
#     cur.execute('''CREATE TABLE users
#                     (id INTEGER,
#                     username TEXT NOT NULL,
#                     hash TEXT NOT NULL,
#                     cash NUMERIC NOT NULL DEFAULT 10000.00,
#                     PRIMARY KEY(id));''')
#     con.commit()
#
# def add_all_items(all_items, cur, con):
#     for item in all_items:
#         cur.execute('INSERT INTO items (name, image_url, num_reviews, price, rating, item_url) VALUES (?, ?, ?, ?, ?, ?);', (item['description'], item['image_url'], item['num_reviews'], item['price'], item['rating'], item['url']))
#     cur.execute('CREATE INDEX item_id ON items (name)')
#     con.commit()


def generate_list_of_clothes():
    ''''''
    # clothes = '''Sweater Dress Hoodies T-shirt Flip-flops Shorts Skirt Jeans Shoes Coat High_heels Suit Cap Sock Shirt Bra Scarf Swimsuit Hat Gloves Jacket coat Boots Sunglasses Tie Polo_shirt jackets sweatpants watches clothes dress_shirt'''
    clothes = '''Sweater Dress Hoodies T-shirt Flip-flops Shorts Skirt Jeans Shoes Coat High_heels Suit Cap'''
    all_clothes = clothes.split()
    return all_clothes



# Start webdriver
driver = webdriver.Chrome('C:/Users/holli/Documents/dependencies/chromedriver.exe')
error = 0

all_clothes = generate_list_of_clothes()
all_items = get_all_from_list(all_clothes)
with open('all_items.txt', 'w', encoding="utf-8") as f:
    i = 1
    for item in all_items:
        f.write("{} | {}\n".format(i,item))
        i += 1
driver.quit()

# con = sqlite3.connect('store.db')
# cur = con.cursor()
#
# create_table(cur, con)
# add_all_items(all_items, cur, con)
json_out = [
{'model':'repo.Item',
'pk':i+1,
'fields':{
    'name': all_items[i]['description'],
    'image_url': all_items[i]['image_url'],
    'num_reviews': all_items[i]['num_reviews'],
    'price': all_items[i]['price']
    }
}
for i in range(len(all_items))]

with open('items.json', 'w') as json_file:
    json.dump(json_out, json_file)

print('there were {} errors'.format(error))

# con.commit()
# con.close()
