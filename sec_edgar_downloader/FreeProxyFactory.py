from .IProxyFactory import IProxyFactory


class FreeProxyFactory(IProxyFactory):
    def __init__(self):
        self._proxies =["http://104.216.26.189:5606", "http://66.172.114.113:44989"]
        self._index = 0
    def get_new_proxies_dict(self):
        if(self._index < len(self._proxies)):
            index = self._index
            self._index += 1
            return {"http": self._proxies[index], "https":self._proxies[index]}
        else:
            print("no more proxy.")
            return None