import requests
from bs4 import BeautifulSoup

def get_price(product_name):
    # Make a request to the website
    url = f"https://laced.com/search?q={product_name}"
    page = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(page.text, "html.parser")

    # Find the product element in the HTML
    pr = soup.find_all("div", {"class": "product-grid__item"})
    if pr is None:
        return "Product not found"

    products = soup.find_all('span', class_='product-grid__title')
    return [product.text.strip() for product in products]




    # Extract the product name and price
    #name = product.find("h3").text
    #price = product.find("span", {"class": "price"}).text
    #name = product.find("h1", {"class": "product-grid__title"}).text

    #return name + ": " + price
    

# Get the product name from the user
product_name = input("Enter product name: ")

# Get the price of the product
names = get_price(product_name)

# Print the result
print("\n".join(names))
