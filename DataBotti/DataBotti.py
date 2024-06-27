import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


def data_fetch():
    global data
    data = [{"id": 1, "name": "Toni"}]
    return data

data = [{"id": 1, "name": "Toni"}]

def data_clean(data):
    data.pop(0)
    return data

clean = data_clean(data)

print(clean)
