####Income Statement
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
index=stock
url_is = "https://finance.yahoo.com/quote/" + index + "/financials?p=" + index
url_bs = "https://finance.yahoo.com/quote/" + index +"/balance-sheet?p="+ index
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/cash-flow?p=’+ index
read_data = ur.urlopen(url_is).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list
for l in soup_is.find_all('div'): 
     ls.append(l.string) # add each element one by one to the list
 
ls = [e for e in ls if e not in ("Operating Expenses","Non-recurring Events")] # Exclude those columns
new_ls = list(filter(None,ls))
new_ls
new_ls = new_ls[12:]
new_ls
is_data = list(zip(*[iter(new_ls)]*5))#### Change this 5 to 6 if Annual reoprt of your company is already released
global Income_st
Income_st = pd.DataFrame(is_data[0:])

Income_st.columns = Income_st.iloc[0] # Name columns to first row of dataframe
Income_st = Income_st.iloc[1:,] # start to read 1st row
Income_st = Income_st.T # transpose dataframe
Income_st.columns = Income_st.iloc[0] #Name columns to first row of dataframe
Income_st.drop(Income_st.index[0],inplace=True) #Drop first index row
Income_st.index.name = "" # Remove the index name
Income_st.rename(index={"ttm":'12/31/2019'},inplace=True) #Rename ttm in index columns to end of the year
#Income_st=income_st["Total Revenue","Net Income",]
Income_st=Income_st.replace(to_replace ="-", 
                 value =float(0.0)) 
Income_st.head()# remove last 5 irrelevant column'
