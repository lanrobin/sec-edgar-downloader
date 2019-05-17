from .IProxyFactory import IProxyFactory


class FreeProxyFactory(IProxyFactory):
    def __init__(self):
        self._proxies =["http://3.213.222.172:8080", "http://167.99.155.123:80"]
        self._index = 0
    def get_new_proxies_dict(self):
        if(self._index < len(self._proxies)):
            index = self._index
            self._index += 1
            return {"http": self._proxies[index], "https":self._proxies[index]}
        else:
            print("no more proxy.")
            return None