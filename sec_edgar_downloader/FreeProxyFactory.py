from .IProxyFactory import IProxyFactory
import requests
import time
import json


class FreeProxyFactory(IProxyFactory):
    def __init__(self):
        self._usedIps =[]
        self._proxies =[]
        self._get_proxy_from_internet()
        
    def get_new_proxies_dict(self):
        if(self._index < len(self._proxies)):
            index = self._index
            self._index += 1
            return {"http": self._proxies[index], "https":self._proxies[index]}
        else:
            print("no more proxy. try to get new proxy from internet")
            self._get_proxy_from_internet()
            while(len(self._proxies) == 0):
                print("no proxy found, sleep for a while and try again.")
                time.sleep(30)
                self._get_proxy_from_internet()
        index = self._index
        self._index += 1
        return {"http": self._proxies[index], "https":self._proxies[index]}


    def _get_proxy_from_internet(self):
        self._proxies.clear()
        self._index = 0

        # first source
        resp = requests.get("https://proxy.rudnkh.me/txt")
        lines = resp.text.split('\n')
        for line in lines:
            ip = line.split(":")[0]
            if(not ip in self._usedIps):
                self._proxies.append(f"http://{line}")
                self._usedIps.append(ip)
        # second source
        resp = requests.get("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list")
        lines = resp.text.split('\n')
        for line in lines:
            try:
                e = json.loads(line)
                ip = e["host"]
                port = e["port"]
                protocol = e["type"]
                if(not ip in self._usedIps):
                    self._proxies.append(f"{protocol}://{ip}:{port}")
                    self._usedIps.append(ip)
            except json.decoder.JSONDecodeError as e:
                print(f"invalid json:{line}")