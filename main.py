#HELPER
#https://pypi.org/project/yfinance/
#print(msft.financials)
#print(msft.financials.loc['Total Revenue'])
#WILL BE DELETED WHEN PROGRAM WILL BE FINALISED

#import libraries
import yfinance as yf
import pandas as pd
# actual code
#get basic analysis


def Multiplir(TICKER):
    Stock = yf.Ticker(TICKER)
    MarketCap = Stock.info["marketCap"]
    Price = Stock.info["previousClose"]
    Volume = MarketCap / Price
    Revenue = Stock.financials.loc['Total Revenue']
    for ai in Revenue:
        print(ai/1000000)
    growth_multiplier = round(( float(Revenue[0])/float(Revenue[1]) + float(Revenue[1])/float(Revenue[2]) + float(Revenue[2])/float(Revenue[3]) )/3,2)
    print(growth_multiplier)
    NetIncome = Stock.financials.loc['Net Income']
    year1Profit = NetIncome[0] * growth_multiplier
    year2Profit = year1Profit * growth_multiplier
    year3Profit = year2Profit * growth_multiplier
    year4Profit = year3Profit * growth_multiplier
    year5Profit = year4Profit * growth_multiplier

    TotalV = (NetIncome[0] + year1Profit/(1+0.015) + year2Profit/((1+0.015)**2) + year3Profit/((1+0.015)**3) + year4Profit/((1+0.015)**4) + year5Profit/((1+0.015)**5))
    print(TotalV)
    realP = TotalV / Volume
    print(realP)
    return growth_multiplier


# Set the ticker as MSFT



Multiplir("ATVI")

