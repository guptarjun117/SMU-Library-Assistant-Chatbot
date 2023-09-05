import requests
import json
import openai


def mega_get(d, i, j, k):
  return d.get(i, {}).get(j, {}).get(k, [None])[0]

def search_results(search): 
    search2 = ""
    base_url = f"https://api-ap.hosted.exlibrisgroup.com/primo/v1/search?vid=65SMU_INST%3ASMU_NUI&tab=Everything&scope=Everything&q=any%2Ccontains%2C{search}%20{search2}&lang=eng&offset=0&limit=10&sort=rank&pcAvailability=true&getMore=0&conVoc=true&inst=65SMU_INST&skipDelivery=true&disableSplitFacets=true&apikey=l8xxce68e59740b24a3e96d67f05ab25da03"

    response = requests.get(base_url)

    # Parse JSON response content
    response_json = response.json()

    count = 1
    results = []

    for item in response_json['docs']:
        # print()
        # print(f'#{count}:')
        # print(item['pnx']['display']['type'])

        item_type = item['pnx']['display']['type']

        if item_type[0] == 'article':
            result = {}
            result['type'] = mega_get(item, 'pnx', 'display', 'type')
            result['title'] = mega_get(item, 'pnx', 'display', 'title')
            result['description'] = mega_get(item, 'pnx', 'display', 'description')
            result['author'] = mega_get(item, 'pnx', 'display', 'creator')
            result['date'] = mega_get(item, 'pnx', 'sort', 'creationdate')
            result['url']  = item.get('delivery', {}).get('almaOpenurl', None)
            result['index'] = count
            results.append(result)

        elif item_type[0] == 'newsletterarticle':
            result = {}
            result['type'] = mega_get(item, 'pnx', 'display', 'type')
            result['title'] = mega_get(item, 'pnx', 'display', 'title')
            result['source'] = mega_get(item, 'pnx', 'display', 'source')
            result['author'] = mega_get(item, 'pnx', 'display', 'publisher')
            result['date'] = mega_get(item, 'pnx', 'sort', 'creationdate')
            result['url']  = item.get('delivery', {}).get('almaOpenurl', None)
            result['index'] = count
            results.append(result)

        elif item_type[0] == 'journal':
            result = {}
            result['type'] = mega_get(item, 'pnx', 'display', 'type')
            result['title'] = mega_get(item, 'pnx', 'display', 'title')
            result['publisher'] = mega_get(item, 'pnx', 'display', 'publisher')
            result['date'] = mega_get(item, 'pnx', 'sort', 'creationdate')
            result['index'] = count
            results.append(result)

        elif item_type[0] == 'book':
            result = {}
            result['type'] = mega_get(item, 'pnx', 'display', 'type')
            result['title'] = mega_get(item, 'pnx', 'display', 'title')
            result['author'] = mega_get(item, 'pnx', 'sort', 'author')
            result['description'] = mega_get(item, 'pnx', 'display', 'description')
            result['date'] = mega_get(item, 'pnx', 'sort', 'creationdate')
            result['index'] = count
            results.append(result)

        count += 1

    return results


def parse_gpt(search):
    openai.api_key = "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"

    first_prompt = 'hellos! I will be sending you a search prompt and the results retrieved from my library database with the search prompt. Please look through the search results and return the top 3 most relevant results parsed nicely. If the title of the search results are referring to the same book/item, provide only one of the result.'
    results = search_results(search)

    chat_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f'{first_prompt} \n search prompt: {search} \n results: {results}'}])


    GPT_reply = "libsearch reply: " + chat_response['choices'][0]['message']['content']

    return GPT_reply    


def main():
    GPT_reply = parse_gpt("War and Peace")
    print(GPT_reply) 


if __name__ == '__main__':
    main()