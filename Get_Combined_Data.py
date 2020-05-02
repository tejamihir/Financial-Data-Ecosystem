## data Manipulation to create table strucutrue
import pandas as pd
Balance_st.head()## remov ecommon stock

##### Get data from Balance sheet for your sheet
global ls
ls=[]
for x in Balance_st.loc['3/31/2019']:
        y=x.replace(",","")
        ls.append(int(y))
    
ls=pd.DataFrame(ls)  
ls=ls.T
ls.columns=Balance_st.columns
ls["% liabilities"]=ls['Total Liabilities']/ls['Total Assets']*100
ls["Leverage"]=ls['Total Assets']/ls["Total stockholders' equity"]
ls["Book Value"]=ls["Total stockholders' equity"]
###Income Statement
Income_st.head() 
global ls_inc
ls_inc=[]
for x in Income_st.loc['3/31/2019']:
        if type(x)!=float:
            y=x.replace(",","")
            ls_inc.append(float(y))
        else:
            ls_inc.append(y)
ls_inc=pd.DataFrame(ls_inc)  
ls_inc=ls_inc.T
ls_inc.columns=Income_st.columns 
ls['Profit this year']=ls_inc['Net Income']
ls['Profit Last Year']="Bf"
ls.loc[0,'Profit Last Year']=float(Income_st.loc['3/31/2018','Net Income'].replace(",",""))
ls['EPS This Year']=float(Income_st.loc['3/31/2019','Basic EPS'])
ls['EPS last Year']=float(Income_st.loc['3/31/2018','Basic EPS'])
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
ls['ROA']=(ls['Profit this year']/ls['Total Assets'])*100
ls['ROE']=(ls['Profit this year']/ls['Book Value'])*100
ls['Payout Ratio']=stat_st['Payout Ratio'][1]
ls['5 Avg Dividend Yield']=stat_st['5 Year Average Dividend Yield'][1]
ls['Forward Dividend Yield']=stat_st['Forward Annual Dividend Yield'][1]
ls["Profit Margin"]=stat_st['Profit Margin'][1]
ls['Operating Margin']=stat_st['Operating Margin'][1]
ls['Debt/Equity']=stat_st['Total Debt/Equity'][1]
ls=ls.rename(index={0:stock})
global df
#df=pd.DataFrame()
df=df.append(ls,sort=False)
df.head()
#ls['% Liabilities']=float(ls.iloc[0]['Total Liabilities'])/float(ls.iloc[0]['Total Assets'])
()
