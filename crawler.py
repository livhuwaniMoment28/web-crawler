import requests
from bs4 import BeautifulSoup
import csv

#Function to extract product information
def extract_product_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    product = {}
    product["url"] = url
    product["image"] = soup.select_one(".wp-post-image")["src"]
    
    product_title_element = soup.select_one(".product_title")
    
    product["name"] = product_title_element.text if product_title_element else "N/A"
        
    product ["price"] = soup.select_one(".price")
    
    return product

   
initial_url = "htpps://scrapeme.live/shop/"    

urls = [initial_url]

products = list(map(extract_product_info, filter(lambda url: "https://scrapeme.live/shop" in url, urls)))
        
with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
        
    for product in products:
        writer.writerow(product.values())
        
        

