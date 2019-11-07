
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





# Set the ticker
analysis.Multiplir("ATVI")
'''
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
'''