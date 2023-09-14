import json

message = []
# Open the JSON file and read it line by line
with open('libfaq_cleaned.json', 'r') as json_file:
    # Load the JSON data as a list of dictionaries
    data_list = json.load(json_file)

    # Loop through each JSON object in the list
    for item in data_list:
        prompt = item["Question"]
        response = item["Answer"]
        message.append(f'prompt-----------{prompt}-----------response-----------{response}-----------, ') 

# Specify the path where you want to save the JSON file
file_path = "testprompt.json"

# Open the file in write mode and save the data as JSON
with open(file_path, "w") as json_file:
    json.dump(message, json_file, indent=4)  # The 'indent' parameter adds formatting for readability

print(f"Data saved as JSON in {file_path}")
