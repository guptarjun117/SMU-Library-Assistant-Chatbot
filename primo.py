import requests
search = "financial accounting"
import xml.etree.ElementTree as ET

# url = f'<api-gateway-url>/primo/v1/search?vid=Auto1&tab=default_tab&scope=default_scope&q=any%2Cany%2C{search}%2Ccontains%2Cwater&apikey=l8xxce68e59740b24a3e96d67f05ab25da03'


url = 'https://api-eu.hosted.exlibrisgroup.com/primo/v1/search?vid=Auto1&tab=default_tab&scope=default_scope&q=any%2Cany%2Cfinancial&lang=eng&offset=0&limit=10&sort=rank&pcAvailability=true&getMore=0&conVoc=true&inst=VOLCANO&skipDelivery=true&disableSplitFacets=true&apikey=l8xxce68e59740b24a3e96d67f05ab25da03'

response = requests.get(url)

if response.status_code == 500:
    data = response.json()
    print(data)

else:
    print(response.status_code)

# <any>,<any>,<{search}>

# any,any,search