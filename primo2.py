import requests
import json


search = 'cats'
search2 = 'dogs'
base_url = f"https://api-ap.hosted.exlibrisgroup.com/primo/v1/search?vid=65SMU_INST%3ASMU_NUI&tab=Everything&scope=Everything&q=any%2Ccontains%2C{search}%20{search2}&lang=eng&offset=0&limit=10&sort=rank&pcAvailability=true&getMore=0&conVoc=true&inst=65SMU_INST&skipDelivery=true&disableSplitFacets=true&apikey=l8xxce68e59740b24a3e96d67f05ab25da03"

response = requests.get(base_url)

# Parse JSON response content
response_json = response.json()

# Save the JSON response to a file
output_filename = "response2.json"
with open(output_filename, "w") as output_file:
    json.dump(response_json, output_file, indent=4)

# Pretty-print the parsed JSON response
print(json.dumps(response_json, indent=4))
