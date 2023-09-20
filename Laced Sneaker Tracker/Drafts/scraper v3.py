import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import re



search_query = input("Enter name of sneaker: ")
search_query = search_query.replace(' ', '+')



print("\nGenerating search link..")
url = 'https://www.laced.com/search?utf8=%E2%9C%93&search%5Bsorted_by%5D=relevance&search%5Bterm%5D='+ search_query


#print(url)
print("")

print("Products found on laced:")
def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


    

def size_and_price(chosen_title):
    
    
    chosen_title = chosen_title.replace(' ', '-')
    
    

    uk_size = input("\nEnter UK size of the shoe to see its price")
    

    url2 = 'https://www.laced.com/products/'+ chosen_title.lower() + '?uk_size=' + uk_size
    print(url2)
    r2 = requests.get(url2)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    


    
    size_results = str(soup2.find_all('div', {'data-react-class': 'product_show/ProductInfo'}))
    
    price = re.findall(r'"price":\s*"([^}]+)"', size_results)
    
    
    print(price)



def parse(soup):
    #results = str(soup.find_all('div', {'data-react-class': 'search_index/ProductGrid'}))
    #print(results)

    #titles = re.findall(r'"title":\s*"([^}]+)"', results)

    product_divs = soup.find_all('div', class_='product-picture')
    
    for index, product_div in enumerate(product_divs, start=1):
        img = product_div.find('img')
        alt_text = img.get('alt', 'No alt text available')
        print(f"[{index}] {alt_text}")
    
    # Extract the text until a comma is encountered
##    stopped_at_comma_titles = [title.strip() for title in titles]
##
##    title_list = stopped_at_comma_titles
##
##    for index, title in enumerate(title_list):
##            print("[", index+1,"]", title)

    
    while True:
        
        choice = int(input("\nSelect an option to see its size and price."))
        chosen_title = title_list[choice]

        try:
            choice = int(choice)
            if choice < 0 or choice >= len(title_list):
                print("Invalid choice. Please enter a number within the range of available indices.")
            else:
                # Print the chosen title
                
                print("The chosen product is:", chosen_title)

                # Do something when the user's choice matches a title in the title_list
                for title in title_list:
                    if chosen_title == title:
                        size_and_price(chosen_title)
                        break
                else:
                    print("The chosen title is not in the title_list.")

                break
        except ValueError:
            print("Invalid choice. Please enter a number.")
    
    


#call the code 
soup = get_data(url)
parse(soup)


#url = f"https://laced.com/search?q={product_name}"
#https://www.laced.com/search?utf8=%E2%9C%93&search%5Bsorted_by%5D=relevance&search%5Bterm%5D=
#page = requests.get(url)
