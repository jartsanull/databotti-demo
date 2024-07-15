import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine


def data_fetch():
    global data
    data = [{"id": 1, "name": "Toni"}]
    return data

data = [{"id": 1, "name": "Toni"}, {"id": 2, "name": "Al"}]

def data_clean(data):
    data.pop(1)
    return data

clean = data_clean(data)

def data_analyse(clean):
    print(f"Result: ${clean}")


print(data_analyse(clean))
