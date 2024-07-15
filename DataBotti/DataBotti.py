import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


def data_fetch():
    global data
    data = [{"id": 1, "name": "Toni"}]
    return data

data = [{"id": 1, "name": "Toni"}, {"id": 2, "name": "Al"}] #< - temporary stuff for testing

def data_clean(data):
    data.pop(1)
    return data

clean = data

def data_analyse(clean):
   #cleaned = ", ".join(clean for item in clean)
   #print(f"Result: ${cleaned}")
    return ", ".join(f'id: {item["id"]}, name: {item["name"]}' for item in data) #< - this one is temporary


data_clean(data)
print(data_analyse(clean))
