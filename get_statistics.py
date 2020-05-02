#### Statistics####
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
index=stock
url_bs = "https://finance.yahoo.com/quote/" + index +"/key-statistics?p="+ index
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/key-statistics?p=’+ index
read_data = ur.urlopen(url_bs).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list


for l in soup_is.find_all(['span','td']): 
     ls.append(l.string)
ls 
ls=ls[14:]
ls=ls[:len(ls)-11]
ls = [e for e in ls if e not in ( 'Valuation Measures','Balance Sheet', 'Dividends & Splits', 'Management Effectiveness', 'Share Statistics'
                                'Financial Highlights','Income Statement','Profitability','Cash Flow Statement','Financial Highlights','Trading Information',
 'Stock Price History','Fiscal Year',
 'Fiscal Year Ends',
 'Mar 31, 2019',
 'Most Recent Quarter',
                                 
 'Dec 31, 2019','Share Statistics')]# Exclude those columns
ls=list(filter(None,ls))
#index=[8,11,20,45,48,51,54,57,60,63,74,79,92,95,106,121,124,129]
index = []
num = len(ls)
i = 0

while i < num-1:
    if ls[i] == ls[i+1] and ls[i] == 'N/A':
        index.append(ls[i])
        i += 2
    else:
        index.append(ls[i])
        i = i + 1
index
new_ls=index
new_ls
stat_data = list(zip(*[iter(new_ls)]*2))
stat_data
global stat_st
stat_st = pd.DataFrame(stat_data[0:])
stat_st = stat_st.T # Transpose Dataframe
stat_st.columns = stat_st.iloc[0] #Name columns to first row of dataframe
stat_st.drop(stat_st.index[0],inplace=True) #Drop first index row
stat_st
stat_st.index.name = "" # Remove the index name
stat_st=stat_st.replace(to_replace="N/A",value=float(0.0))
stat_st.head()

#stat_st.columns
