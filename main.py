from sec_edgar_downloader.Downloader import Downloader
from sec_edgar_downloader.FreeProxyFactory import FreeProxyFactory
from joblib import Parallel, delayed
import multiprocessing

identifiers = ["MSFT", "APPL", "FB"]
#with open("NASDAQ_20171018.txt", "r") as f:
#    lines = f.readlines()
#    for line in lines:
#        identifiers.append(line.split(",", 1)[1])


num_cores = multiprocessing.cpu_count()

print("starting download use " + str(num_cores) +" task.")
dl = Downloader("./filings/", FreeProxyFactory())

#identifiers = ["AAPL", "MSFT", "0000102909", "V", "FB"]
#for id in identifiers:
#    dl.get_all_available_filings(id, 1)

def downloadSymbol(symbol, dl):
    dl.get_all_available_filings(symbol, 100)


for s in identifiers:
    downloadSymbol(s, dl)