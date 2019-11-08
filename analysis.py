#HELPER
#https://pypi.org/project/yfinance/
#print(msft.financials)
#print(msft.financials.loc['Total Revenue'])
#WILL BE DELETED WHEN PROGRAM WILL BE FINALISED
import yfinance as yf

def PresentValue(TICKER,BEPyears):
    years = BEPyears
    #print(TICKER)
    Stock = yf.Ticker(TICKER)
    #print(Stock.financials)
    MarketCap = Stock.info["marketCap"]
    Price = Stock.info["previousClose"]
    Volume = MarketCap / Price
    Revenue = Stock.financials.loc['Total Revenue']
    cogs = Stock.financials.loc['Cost Of Revenue']
    research = Stock.financials.loc['Research Development']
    admin = Stock.financials.loc['Selling General Administrative']
    other_Opex = Stock.financials.loc['Other Operating Expenses']
    # calculate future revenue
    FutureRevenue = []
    try:
        growth_multiplier = round((Revenue[2]/Revenue[3] + Revenue[1]/Revenue[2] + Revenue[1]/Revenue[2] + Revenue[0]/Revenue[1] + Revenue[0]/Revenue[1] + Revenue[0]/Revenue[1]) / 6,2)
        x = 0
        while x < years + 1:
            FutureRevenue.append(round(Revenue[0]*(growth_multiplier**x),0))
            x = x + 1
    except:
        x = 0
        while x < years + 1:
            FutureRevenue.append(0)
            x = x + 1
    #calculate future cost of revenue
    cogs_multiplier = round((cogs[3]/Revenue[3] + cogs[2] / Revenue [2] + cogs[1] / Revenue[1] + cogs[0] / Revenue[0])/4,2)
    futurecogs = []
    for rev in FutureRevenue:
        futurecogs.append(round(rev * cogs_multiplier,0))
    x = 0

    grossProfit = []
    while x < years + 1:
        grossProfit.append(FutureRevenue[x] - futurecogs[x])
        x = x + 1

    #opex calculation
    #calculate research and developement costs
    futureResearch = []
    try:
        research_multiplier = round(
            (research[2]/research[3] + research[1]/research[2] + research[1]/research[2] + research[0]/research[1] + research[0]/research[1] + research[0]/research[1]) / 6,2
            )
        x = 0
        while x < years + 1:
            futureResearch.append(round(research[0]*(research_multiplier**x),0))
            x = x + 1
    except:
        x = 0
        while x < years + 1:
            futureResearch.append(0)
            x = x + 1

    #calculate admin costs of the company
    futureAdmin = []
    try:
        admin_multiplier = round(
            (admin[2]/admin[3] + admin[1]/admin[2] + admin[1]/admin[2] + admin[0]/admin[1] + admin[0]/admin[1] + admin[0]/admin[1]) / 6,2
            )
        x = 0
        while x < years + 1:
            futureAdmin.append(round(admin[0]*(admin_multiplier**x),0))
            x = x + 1
    except:
        x = 0
        while x < years + 1:
            futureAdmin.append(0)
            x = x + 1

    # calculate other oprex cost of the company
    FutureOtherOpex = []
    try:
        otherOpexMultiplier = round(
            (other_Opex[2]/other_Opex[3] + other_Opex[1]/other_Opex[2] + other_Opex[1]/other_Opex[2] + other_Opex[0]/other_Opex[1] + other_Opex[0]/other_Opex[1] + other_Opex[0]/other_Opex[1]) / 6,2
            )
        x = 0
        while x < years + 1:
            FutureOtherOpex.append(round(other_Opex[0]*(otherOpexMultiplier**x),0))
            x = x + 1
    except:
        x = 0
        while x < years + 1:
            FutureOtherOpex.append(0)
            x = x + 1
    opex = []
    x = 0
    while x < years + 1:
        opex.append(futureResearch[x] + futureAdmin[x] + FutureOtherOpex[x])
        x = x + 1
    ebitda = []
    x = 0
    while x < years + 1:
        ebitda.append(grossProfit[x] - opex[x])
        x = x + 1



    #calculate EBT
    toe = Stock.financials.loc['Total Operating Expenses']
    oldebitda = []
    x = 0
    while x < 4:
        oldebitda.append(Revenue[x] - toe[x])
        x = x + 1
    ebt = Stock.financials.loc["Income Before Tax"]
    ebt_multiplier = round((ebt[3]/oldebitda[3] + ebt[2] / oldebitda [2] + ebt[1] / oldebitda[1] + ebt[0] / oldebitda[0])/4,2)
    print(ebt_multiplier)
    future_ebt = []
    for ni in ebitda:
        future_ebt.append(round(ni * ebt_multiplier,0))

    present_value1 = []
    present_value2 = []
    x = 0
    while x < years + 1:
        present_value1.append(future_ebt[x]/((1+0.03)**(x)))
        #tax adjusted
        present_value2.append((future_ebt[x]*(1-0.28))/((1+0.03)**(x)))
        x = x + 1
    prices = []
    prices.append(TICKER)
    prices.append(Price)
    present_total_value1 = 0
    for ni in present_value1:
        present_total_value1 = present_total_value1 + ni
    prices.append(round(present_total_value1/Volume,2))

    present_total_value2 = 0
    for ni in present_value2:
        present_total_value2= present_total_value2 + ni
    prices.append(round(present_total_value2/Volume,2))
    return prices

print(PresentValue("ATVI",7))