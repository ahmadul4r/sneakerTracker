import requests
from bs4 import BeautifulSoup
import json
import re

search_query = input("Enter name of sneaker: ")
search_query = search_query.replace(' ', '+')

print("\nGenerating search link..")
url = 'https://www.laced.com/search?utf8=%E2%9C%93&search%5Bsorted_by%5D=relevance&search%5Bterm%5D='+ search_query
print(url)

print("")
print("Products found on laced:")

def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def scrape_product_names(soup):
    product_names = []
    script_tag = soup.find('script', class_='js-react-on-rails-component', attrs={"data-component-name": "ProductGrid"})
    
    if script_tag:
        script_text = script_tag.string
        json_data = json.loads(script_text)
        
        if 'products' in json_data:
            for product in json_data['products']:
                product_names.append(product['title'])
    
    return product_names

def size_and_price(chosen_title):
    chosen_title = chosen_title.replace(' ', '-')
    uk_size = input("\nEnter UK size of the shoe to see its price: ")
    url2 = 'https://www.laced.com/products/'+ chosen_title.lower() + '?uk_size=' + uk_size
    
    print(url2)
    
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    
    price_element = soup2.find('h1', class_='css-1s6vnk3')
    
    if price_element:
        price = price_element.get_text(strip=True)
        print("Price:", price)
    else:
        print("Price information not found for this product.")


    

def parse(soup):
    product_names = scrape_product_names(soup)
    
    for index, product_name in enumerate(product_names, start=1):
        print(f"[{index}] {product_name}")
    
    while True:
        try:
            choice = int(input("\nSelect a product number to see its size and price (or 'q' to quit): "))
            if choice < 1 or choice > len(product_names):
                print("Invalid choice. Please enter a valid product number.")
            else:
                chosen_title = product_names[choice - 1]
                print("The chosen product is:", chosen_title)
                size_and_price(chosen_title)
        except ValueError:
            choice = input("Invalid input. Enter a number or 'q' to quit: ")
            if choice.lower() == 'q':
                break

# Call the code 
soup = get_data(url)
parse(soup)


