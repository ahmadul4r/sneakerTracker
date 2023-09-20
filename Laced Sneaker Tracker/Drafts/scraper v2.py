import requests
from bs4 import BeautifulSoup

def product_scraper(search_query):
  url = f"https://laced.com/search?q={search_query}"
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html.parser')
  products = soup.find_all('span', class_='product-grid__title')
  return [product.text.strip() for product in products]

# Prompt user for search query
search_query = input("Enter the search query: ")
# Scrape product names and store in a list
product_names = product_scraper(search_query)
# Print the list of product names
print("\n".join(product_names))
