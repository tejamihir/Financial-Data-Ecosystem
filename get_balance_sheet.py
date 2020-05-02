#### Balance Sheet####
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
index=stock
url_bs = "https://finance.yahoo.com/quote/" + index +"/balance-sheet?p="+ index
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/cash-flow?p=’+ index
read_data = ur.urlopen(url_bs).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list

for l in soup_is.find_all('div'): 
     ls.append(l.string)
ls = [e for e in ls if e not in ( 'AXISBANK.NS - Axis Bank Limited', 'NSE - NSE Real Time Price. Currency in INR',' react-empty: 2 ',
 'Tip: Try a valid symbol or a specific company name for relevant results',
 'Cancel',' react-empty: 6 ', "No matching results for ''", '© 2020 Verizon Media. All rights reserved.')] # Exclude those columns
new_ls = list(filter(None,ls))
new_ls
new_ls = new_ls[5:]###Change this to 4 Axisbank-like stocks
new_ls
bs_data = list(zip(*[iter(new_ls)]*4))### 4-If 2020 balance Sheet not relaeased ###5 if released
global Balance_st
Balance_st = pd.DataFrame(bs_data[0:])
Balance_st
Balance_st.columns = Balance_st.iloc[0] # Name columns to first row of dataframe
Balance_st = Balance_st.iloc[1:,] # start to read 1st row
Balance_st = Balance_st.T # transpose dataframe
Balance_st.columns = Balance_st.iloc[0] #Name columns to first row of dataframe
Balance_st.drop(Balance_st.index[0],inplace=True) #Drop first index row
Balance_st.index.name = "" # Remove the index name
Balance_st.head()
Balance_st=Balance_st[["Total Cash","Inventory","Total Assets","Total Liabilities","Total stockholders' equity"]]
#Balance_st.drop(columns=['Common Stock',"Total liabilities and stockholders' equity"],inplace=True)
Balance_st
