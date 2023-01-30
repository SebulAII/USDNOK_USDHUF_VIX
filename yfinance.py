import yfinance as yf
import os
import datetime
instruments = ['XLE',
'XLF',
'XLU',
'XLI',
'GDX',
'XLK',
'XLV',
]
period = 'max'
interval = '1D'
log_path=os.getcwd() + '/results/' + datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
os.makedirs(log_path)
for instrument in instruments:
    ticker = yf.Ticker(instrument)
    df = ticker.history(period=period, interval=interval)
    df.to_csv(os.path.join(log_path, instrument + '.csv'))