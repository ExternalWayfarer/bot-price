from bs4 import BeautifulSoup
import requests, re, urllib.parse, json, time


#country = input("Введите домен(ru - РФ,by - Беларусь,kz - Казахстан, am - Армения): ")
input_name = input("Введите наименование элемента: ")

country = 'ru'
lang = 'Язык'
url =f'https://www.chipdip.{country}/search?searchtext={input_name}' #define url variable for comfort


def parse_website(url):

    

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}   #add a some identifier
    result = requests.get(url, headers=headers) #function that get all code from webpage

    return BeautifulSoup(result.text,"lxml")  #do literally the same thing


soup = parse_website(url)



class CategoryElements:
    def __init__(self, category, quantity, link):
        self.category = category
        self.quantity = quantity
        self.link = link
    def __repr__(self):
        return  f"{self.category}: {self.quantity}"
  
class Item:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
    def __repr__(self):
        return  f"{self.name}: {self.price}"
  

category=[]
quantity = []
links = []
elements=[]

components = []
prices = []
links_comp = []


#вывод категорий на главной странице поиска
for a in soup.find_all("div", id=re.compile("^search_results")): 
    
    
    for b in a.find_all("div", class_="serp__group-section"): 
        
        header = a.find("span", class_='group-header')  
        count = a.find("sub", class_='count')
        print(header.text + ": " + count.text)
        
        for c in b.find_all("div", class_="serp__group clear"): 
        
            for d in c.find_all("a", class_="link serp__group-col-item"):
                cat_element = d.text
                category.append(cat_element)
                link=f'https://www.chipdip.{country}' + d.get("href")
                links.append(link)
            for amount in c.find_all("sub", class_='count'):
                cat_quantity = amount.text
                quantity.append(cat_quantity)


for category, quantity, link in zip(category, quantity, links):
    element = CategoryElements(category, quantity, link)
    elements.append(element)
    
#for element in elements:
#    print(element)

#print(elements[0])

time.sleep(2)
#url = 'https://www.chipdip.ru/catalog-show/arduino-sensors?gq=lm393'
url = 'https://www.chipdip.ru/catalog/ext?gq=lm393'

soup = parse_website(url)

if 'catalog-show' in url:
    for a in soup.find_all("div", id="itemlist"):
        for b in a.find_all("div", class_="item"):          
            for component in b.find_all("a", class_="link"):                
                print(component.text)
            for price in b.find_all("span", class_="price__value"):
                print(price.text)

else: 
    for a in soup.find_all("table", id="itemlist"):
        for b in a.find_all("tr", class_="with-hover"):          
            for component in b.find_all("a", class_="link"):                
                print(component.text)
            for price in b.find_all("span", id=re.compile("^price_")):
                print(price.text)   

def page_counter():
    for page in soup.find_all("li", class_="pager__page"):
        print("1")

page_counter()








'''
if len(input_name)<4:
    input_name = input_name+"    "
coded_text = urllib.parse.quote(input_name.encode('cp1251'))
url = f'https://www.platan.ru/cgi-bin/qwery_i.pl?code={coded_text}'
result = requests.get(url, headers=headers) #function that get all code from webpage
#print(result.content.decode('latin-1'))                 #decode as text
soup = BeautifulSoup(result.text,"lxml")  #do literally the same thing



prices = []
components = []

for element in soup.findAll("tr", "border-bottom"): 
    for naming in element.findAll("a", 'link'):
        component = naming.text
        if ',' in component:
            component=component[:component.index(",")]
            components.append(component)
        else: components.append(component)
       


#cycle for search span element contained "price" 
for item in soup.findAll("td", 'font-weight-bold'):
    price=item.text
    price =  round(float(price[:price.index("/")]))
    
    #price=int("".join(c for c in price if c.isdecimal()))
    prices.append(price)

price_table(components, prices)

'''