#HELPER
#https://pypi.org/project/yfinance/
#print(msft.financials)
#print(msft.financials.loc['Total Revenue'])
#WILL BE DELETED WHEN PROGRAM WILL BE FINALISED

# Fist version of the app gives most basic valuation of the stock and than compares it to the value of the current price
#import libraries
import yfinance as yf
import pandas as pd
import csv
# actual code
#get basic analysis

import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)

    return tickers
tickers = []
for a in save_sp500_tickers():
    tickers.append(a.replace("\n", ""))
#print(tickers)



def Multiplir(TICKER):
    #print(TICKER)
    Stock = yf.Ticker(TICKER)
    MarketCap = Stock.info["marketCap"]
    Price = Stock.info["previousClose"]
    Volume = MarketCap / Price
    Revenue = Stock.financials.loc['Total Revenue']
    growth_multiplier = round(( float(Revenue[0])/float(Revenue[1]) + float(Revenue[1])/float(Revenue[2]) + float(Revenue[2])/float(Revenue[3]) )/3,2)
    NetIncome = Stock.financials.loc['Total Revenue']
    year1Profit = NetIncome[0] * growth_multiplier
    year2Profit = year1Profit * growth_multiplier
    year3Profit = year2Profit * growth_multiplier
    year4Profit = year3Profit * growth_multiplier
    year5Profit = year4Profit * growth_multiplier

    TotalV = (NetIncome[0] + year1Profit/(1+0.015) + year2Profit/((1+0.015)**2) + year3Profit/((1+0.015)**3) + year4Profit/((1+0.015)**4) + year5Profit/((1+0.015)**5))
    realP = TotalV / Volume
    return_Value = [TICKER,Price,round(realP,2)]
    return return_Value


# Set the ticker
Multiplir("ATVI")
with open('datav2.csv', mode='w') as dt:
    dt_writer = csv.writer(dt, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dt_writer.writerow(["NAME","Current","Real"])
    for t in tickers:
        print(t)
        try:
            dt_writer.writerow(Multiplir(t))
            #print(Multiplir(t))
        except:
            dt_writer.writerow([t,"not Found"])
            pass