import requests
from bs4 import BeautifulSoup
def get_urls():
    with open("data.txt","r") as f:
        data = f.read()
    return data.split("\n") if data else []

def get_soup(url):
    return BeautifulSoup(requests.get(url).content,"html.parser")

def get_val(d,id):
    x = d.find("span",{"class":f"wprm-recipe-ingredient-{id}"})
    return x.text if x else ""

def handle_int(amount):
    if amount == "":
        return 0
    elif "-" in amount:
        x,y = amount.split("-")
        return int((int(x)+int(y))/2)
    elif "/" in amount:
        x,y = amount.split("/")
        return round(int(x)/int(y),2)
    else:
        return int(amount)


def get_raw(urls):
    # item : {unit: value}
    raw_data = {}
    for url in urls:
        result = get_soup(url).find_all("li",{"class":"wprm-recipe-ingredient"})
        for d in result:
            amount = get_val(d,"amount")
            if amount:
                amount = handle_int(amount)
            unit = get_val(d,"unit")
            name = get_val(d,"name")
            if name in raw_data:
                if unit in raw_data:
                    raw_data[name][unit] += amount
                else:
                    raw_data[name][unit] = amount
            else:
                raw_data[name] = {unit:amount}
    return raw_data
