# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:51:45 2020

@author: mihir.rao
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur

global df
global stock
stock='UPL.NS'
stock
global ls
####Income Statement
global index
index=stock
url_is_ind="https://in.finance.yahoo.com/quote/"+index+"/financials?p="+index
url_is = "https://finance.yahoo.com/quote/" + index + "/financials?p=" + index
url_bs = "https://finance.yahoo.com/quote/" + index +"/balance-sheet?p="+ index
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/cash-flow?p=’+ index
read_data = ur.urlopen(url_is_ind).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list
for l in soup_is.find_all('div'): 
     ls.append(l.string) # add each element one by one to the list
 
ls = [e for e in ls if e not in ("Operating Expenses","Non-recurring Events")] # Exclude those columns
new_ls = list(filter(None,ls))
new_ls
# remove last 5 irrelevant column'
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
Income_st.head()

#### Balance Sheet####
index=stock
url_bs = "https://in.finance.yahoo.com/quote/" + index +"/balance-sheet?p="+ index
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
Balance_st=Balance_st[["Total assets","Total liabilities","Total stockholders' equity"]]#Mofiy here fro Axis Bank like columns
#Balance_st.drop(columns=['Common Stock',"Total liabilities and stockholders' equity"],inplace=True)
Balance_st


#### Statistics####
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
####Price####
#global index
index=stock
url_bs = "https://in.finance.yahoo.com/quote/"+index+"/"
url_bs
#url_cf = ‘https://finance.yahoo.com/quote/' + index + ‘/balance-sheet?p=’+ index
read_data = ur.urlopen(url_bs).read() 
soup_is= BeautifulSoup(read_data,"lxml")
ls= [] # Create empty list

for l in soup_is.find_all('span'): 
     ls.append(l.string)
global price        
price=float(ls[13].replace(",",""))

price
## data Manipulation to create table strucutrue
import pandas as pd
import numpy as np
Balance_st.head()## remov ecommon stock

##### Get data from Balance sheet for your sheet

ls=[]
for x in Balance_st.loc['31/3/2019']:
        y=x.replace(",","")
        ls.append(int(y))
    
ls=pd.DataFrame(ls)  
ls=ls.T
ls.columns=Balance_st.columns
ls["% liabilities"]=ls['Total liabilities']/ls['Total assets']*100
ls["Leverage"]=ls['Total assets']/ls["Total stockholders' equity"]
ls["Book Value"]=ls["Total stockholders' equity"]
###Income Statement
Income_st.head() 
global ls_inc
ls_inc=[]
for x in Income_st.loc['31/3/2019']:
        if type(x)!=float:
            y=x.replace(",","")
            ls_inc.append(float(y))
        else:
            ls_inc.append(y)
ls_inc=pd.DataFrame(ls_inc)  
ls_inc=ls_inc.T
ls_inc.columns=Income_st.columns 
ls['Profit this year']=ls_inc['Net income']
ls['Profit Last Year']="Bf"
ls.loc[0,'Profit Last Year']=float(Income_st.loc['31/3/2018','Net income'].replace(",",""))
ls['Profit Change']=(float(ls['Profit this year'])/float(ls['Profit Last Year'])-1)*100
ls['EPS This Year']=float(Income_st.loc['31/3/2019','Basic EPS'])
ls['EPS last Year']=float(Income_st.loc['31/3/2018','Basic EPS'])
ls['EPS Change']=(float(ls['EPS This Year'])/float(ls['EPS last Year'])-1)*100
ls['Book Value Per Share']=float(stat_st['Book Value Per Share'].replace(",",""))
ls['EV/EBITDA']=stat_st['Enterprise Value/EBITDA']
ls['Price']=float(price)

Income_st.loc['12/31/2019','Basic EPS']=float(0.0)
df1=pd.DataFrame()
df1['Teja']=Income_st['Basic EPS']
df1['Teja']=df1['Teja'].astype('float')
ls['EPS Avg']=df1['Teja'].mean(skipna=True)
ls['EPS Avg Growth']=(ls['EPS This Year']/ls['EPS Avg']-1)*100
ls['P/E']=ls['Price']/ls['EPS This Year']
ls['P/PEG']=ls['P/E']/ls['EPS Change']
ls['P/PEG Avg']=ls['P/E']/ls['EPS Avg Growth']
ls['P/BV']=ls['Price']/ls['Book Value Per Share']
ls['ROA']=(ls['Profit this year']/ls['Total assets'])*100
ls['ROE']=(ls['Profit this year']/ls['Book Value'])*100
ls['Payout Ratio']=stat_st['Payout Ratio'][1]
ls['5 Avg Dividend Yield']=stat_st['5 Year Average Dividend Yield'][1]
ls['Forward Dividend Yield']=stat_st['Forward Annual Dividend Yield'][1]
ls["Profit Margin"]=stat_st['Profit Margin'][1]
ls['Operating Margin']=stat_st['Operating Margin'][1]
ls['Debt/Equity']=stat_st['Total Debt/Equity'][1]
ls1=[float(x.replace(",","")) for x in Income_st['Total revenue']]
ls1=np.array(ls1)
revenue_mean=ls1.mean()
ls['Avg Revenue Growth%']=(float(Income_st.loc['31/3/2019','Total revenue'].replace(",",""))/revenue_mean-1)*100
ls2=[float(x.replace(",","")) for x in Income_st['Net income']]
ls2=np.array(ls2)
profit_mean=ls2.mean()
ls['Avg Profit Growth%']=(float(Income_st.loc['31/3/2019','Net income'].replace(",",""))/profit_mean-1)*100
ls=ls.rename(index={0:stock})

if(len(df)>1):
    df=df.append(ls,sort=False)
else:
    
    df=pd.DataFrame()
df.head()
#ls['% Liabilities']=float(ls.iloc[0]['Total Liabilities'])/float(ls.iloc[0]['Total Assets'])
