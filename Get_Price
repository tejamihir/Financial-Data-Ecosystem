####Price####
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
global index
index=stock
url_bs = "https://in.finance.yahoo.com/quote/"+index+"/"
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/balance-sheet?p=’+ index
read_data = ur.urlopen(url_bs).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list

for l in soup_is.find_all('td'): 
     ls.append(l.string)
global price        
price=float(ls[1].replace(",",""))

price
