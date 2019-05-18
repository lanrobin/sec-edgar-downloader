from sec_edgar_downloader.Downloader import Downloader
from sec_edgar_downloader.FreeProxyFactory import FreeProxyFactory
from joblib import Parallel, delayed
import multiprocessing

#identifiers = ['JD', 'BIDU']
identifiers = []
with open("symbols.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        identifiers.append(line.split('\n')[0])


num_cores = multiprocessing.cpu_count()

print("starting download use " + str(num_cores) +" task.")
dl = Downloader("./filings/", FreeProxyFactory())

#identifiers = ["AAPL", "MSFT", "0000102909", "V", "FB"]
#for id in identifiers:
#    dl.get_all_available_filings(id, 1)

def downloadSymbol(symbol, dl):
    dl.get_all_available_filings(symbol, 100)


for s in identifiers:
    if downloadSymbol(s, dl) == 0:
        print(f"download:{s} failed.")
        break