
#import libraries

import pandas as pd
import csv
#my library
import sp500Ticker as sp
import analysis
# actual code
#get basic analysis

tickers = []
for a in sp.save_sp500_tickers():
    tickers.append(a.replace("\n", ""))


with open('datav2.csv', mode='w') as dt:
    dt_writer = csv.writer(dt, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    dt_writer.writerow(["NAME","Current","Real","Real Tax"])
    for t in tickers:
        print(t)
        try:
            dt_writer.writerow(analysis.PresentValue(t,7))
            #print(Multiplir(t))
        except:
            dt_writer.writerow([t,"not Found"])
            pass
