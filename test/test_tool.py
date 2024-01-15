from src.toolphish import ToolPhi
import requests, asyncio




def test_url():assert requests.get("https://github.com/search").status_code == 200

resp = ToolPhi()
def test_tool():
    
    assert resp.sites != None
    assert type(resp.sites) == dict
    assert resp.search.get(1) == "termux+phishing"

def test_get_data():assert resp.get_data() == True


async def test_add_data():assert resp.add_data() == True
