#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys

''' This is a command line application built using python3 to search for mobiles using various filters. This module is used by webscraping. '''

def help():
    # Help module listing various filters and syntax
    print("-"*100)
    print("Please enter one of the below filters")
    print("[*] OPTIONS")
    print("enter exit to quit")
    print("\n")
    print("TO SEARCH BY RAM VALUE FOLLOW THE SYNTAX BELOW")
    print("    [*] RAM-VALUE")
    print("""                      => 6GB & ABOVE - 6GBA
                      => 4GB
                      => 3GB
                      => 2GB""")
    print("\n")
    print("TO SEARCH BY BRAND FOLLOW THE SYNTAX BELOW")
    print("    [*] BRAND-VALUE")
    print("""                      => Realme
                      => POCO
                      => Infinix
                      => Motorola
                      => Samsung
                      => Mi
                      => Asus
                      => Blackberry""")
    print("\n")
    print("TO SEARCH BY PRICE LIMIT FOLLOW THE SYNTAX BELOW")
    print("     [*] PRICE-VALUE")
    print(""""                     => Maximum price - Max
                      => Minimum price - 2000
                      """)
    print("'\n")
    print("TO SEARCH BY INTERNAL STORAGE FOLLOW THE SYNTAX BELOW")
    print("     [*] INTERNAL-VALUE")
    print(""""                     => INTERNAL-32
                      => INTERNAL-64
                      => INTERNAL-128
                      => INTERNAL-256A (256GB and above)""")
    print("\n")
    print("TO SEARCH BY SCREEN SIZE (IN INCHES) FOLLOW THE SYNTAX BELOW")
    print("     [*] SCREEN-VALUE")
    print("""                      => SCREEN-5-5.1
                      => SCREEN-5.2-5.4
                      => SCREEN-5.5-5.6
                      => SCREEN-5.7-5.9""")
    print("-"*100)


# To search the mobile phones via brand filter
def brand_flipkart(brand):
    # URL
    url_start = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.brand%255B%255D%3D"
    brand = str(brand)
    final_url = url_start+brand
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36"}
    req = requests.get(final_url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml') # Using lxml as a parser
    # Using fina_all function getting the information
    product_am = soup.find_all("div", {'class':'_3wU53n'})
    price_am = soup.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    rating_am = soup.find_all('div', {'class':'hGSR34'})

    # Printing out the information
    for index in range(len(product_am)):
        try:
            print("Product Name :", product_am[index].string)
            print("Product Price : ", price_am[index].string)
            print("Product Rating : ", rating_am[index].text)
            print("\n")
        except IndexError:
            continue

# To search mobile phones via ram capacity
def ram_flipkart(ram):
    # Getting the url
    end = ''
    url_start = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&p%5B%5D=facets.ram%255B%255D%3D"
    ram = str(ram)
    if ram == "6GBA":
        end = '6%2BGB%2B%2526%2BAbove'
    elif ram == "4GB":
        end = "4%2BGB"
    elif ram == "3GB":
        end = "3%2BGB"
    elif ram == "2GB":
        end = "2%2BGB"
    else:
        print("\n")
        print("UNKNOWN RAM SIZE")
        print("Please refer help")
        print("\n")
        main()
    
    # Pulling up the contents
    final_url = url_start+end
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36"}
    req = requests.get(final_url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    product = soup.find_all("div", {'class':'_3wU53n'})
    price = soup.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    rating = soup.find_all('div', {'class':'hGSR34'})
    
    # Printing out the information
    for index in range(0, len(product)):
        try:
            print("Product Name: ", product[index].string)
            print("Product Price : ", price[index].string)
            print("Product Rating : ", rating[index].text)
            print("\n")
        except IndexError:
            continue

# To search the mobile phones via price limit
def price_limit(price):
    url = "https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=HISTORY&suggestionId=mobiles%7CMobiles&requestId=55999c83-0a5d-4b08-ab06-7246a47bfc87&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D"+str(price)
    # Headers
    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36"
    req = requests.get(url, headers=headers).text
    html = BeautifulSoup(req, 'lxml')
    product = html.find_all("div", {'class':'_3wU53n'})
    price = html.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    rating = html.find_all('div', {'class':'hGSR34'})
    
    # Printing out the information
    for index in range(len(product)):
        try:
            print("Product Name : ", product[index].text)
            print("Product Price : ", price[index].text)
            print("Product Rating : ", rating[index].text)
            print("\n")
        except IndexError:
            continue

# To search mobile phones via internal storage capacity
def internal(size):
    # Obtaining the URL
    url_start = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on&p%5B%5D=facets.internal_storage%255B%255D%3D"
    end = ''
    if size == "64":
        end = "64%2B-%2B127.9%2BGB"
    elif size == "32":
        end = "32%2B-%2B63.9%2BGB"
    elif size == "128":
        end = "128%2B-%2B255.9%2BGB"
    elif size == "256A":
        end = "256%2BGB%2B%2526%2BAbove"
    else:
        print("\n")
        print("UNKNOWN STORAGE SIZE")
        print("Please refer help")
        print("\n")
        main()

    final_url = url_start+end

    # Headers
    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36"
    req = requests.get(final_url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    product = soup.find_all('div',{'class':'_3wU53n'})
    price = soup.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    rating = soup.find_all('div', {'class':'hGSR34'})
    
    # Printing out the information
    for index in range(len(product)):
        try:
            print("Product Name : ", product[index].string)
            print("Product Price : ", price[index].string)
            print("Product Rating : ", rating[index].text)
            print("\n")
        except IndexError:
            continue

# To search mobile phone via screen size of the mobile
def screen(size):
    # Getting the URL
    url_start = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on&p%5B%5D=facets.screen_size%255B%255D%3D"
    end = ''
    size = str(size)
    if size == "5-5.1":
        end = '5%2B-%2B5.1%2Binch'
    elif size == "5.2-5.4":
        end = "5.2%2B-%2B5.4%2Binch"
    elif size == "5.5-5.6":
        end = "5.5%2B-%2B5.6%2Binch"
    elif size == "5.7-5.9":
        end = "5.7%2B-%2B5.9%2Binch"
    else:
        print("\n")
        print("SIZE UNKNOWN")
        print("Please refer help")
        print("\n")
        main()

    final_url = url_start+end

    # Headers
    headers = dict()
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36"
    req = requests.get(final_url, headers=headers).text
    soup = BeautifulSoup(req, 'lxml')
    product = soup.find_all('div', {'class':'_3wU53n'})
    price = soup.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    rating = soup.find_all('div', {'class':'hGSR34'})
    
    # Printing out the information
    for index in range(len(product)):
        try:
            print("Product Name : ", product[index].string)
            print("Product Price : ", price[index].string)
            print("Product Rating : ", rating[index].text)
            print("\n")
        except IndexError:
            continue

# The main program to get the filters
def main():
    print("[*] For help enter -H or --help")
    inp = str(input("[*] Enter the filter : "))
    if (inp == "-H" or inp == "--help"):
        help()
        main()
    elif inp[0:5] == "BRAND":
        brand_flipkart(inp[6:])
    elif inp[0:5] == "PRICE":
        price_limit(inp[6:])
    elif inp[0:3] == "RAM":
        ram_flipkart(inp[5:])
    elif inp[0:8] == "INTERNAL":
        internal(inp[9:])
    elif inp[0:6] == "SCREEN":
        screen(inp[7:])
    elif inp == "exit":
        sys.exit()
    else:
        print("\n")
        print("CONDITION UNKNOWN")
        print("[*] Enter exit to quit")
        print("\n")
        main()


if __name__ == '__main__':
    help()
    main()
