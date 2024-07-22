import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine

from databotti_functions.py import *

def main():
    databotti_functions.data_clean(data)
    #databotti_functions.data_analyse(clean)
    #databotti_functions.data_result(result)

if __name__ == "__main__":
    main()
