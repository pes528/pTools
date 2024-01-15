import requests, subprocess, json, time, asyncio

class ToolPhi:
    
    def __init__(self, rep=None):
        self.search = {
        1:"termux+phishing",
        2:rep,
        }
        self.__DATA = {
            "url":f"https://github.com/search?q={self.search.get(2 if rep != None else 1)}&type=respositories",
        }
        self.sites = {}
        self.names = []
        self.__cont = 1
        self.otherCount = 1
        #self.add_data()
        
    def __str__(self):
        return self.sites[0]
    
    async def add_data(self, num_page=None):

        async def req(url):
            return requests.get(url).json()
        time.sleep(2)
        #body = requests.get(self.__DATA["url"]+num_page).json() if num_page != None else requests.get(self.__DATA["url"]).json()
        body = await req(self.__DATA["url"]+num_page) if num_page != None else await req(self.__DATA["url"])
        
        time.sleep(2)
        for i in body['payload']['results']:

            self.sites[self.__cont] =i['repo']['repository']['owner_login'] + "/" +i['repo']['repository']['name'] 
            self.names.append(i['repo']['repository']['name'])    
            self.__cont += 1
        return True
    
    def get_data(self):

        verde = "\033[1;32m"
        fin = "\033[1;0m"

        for i in self.names:

    
            print(self.otherCount, "->",verde+i+fin)
            self.otherCount += 1
            self.names = []
        return True
        

def banner() -> str:
    with open("./src/banner", "r") as f:
        _banner = f.read();return _banner