# SMU-Library-Assistant-Chatbot

## Aim
The SMU Library Assistant Chatbot aims to improve the nature of SMU Library's 'Ask Library' chat with limited hours and fully human-operated to 24/7 with full automation.

## Main Capabilities
1. Open AI GPT-3.5 Integration: Users can communicate with the bot and it will act as ChatGPT.
2. `/lksbot`: Talk to the bot's alternate version, which is finetuned on the FAQs of SMU Library website. Start your prompt with `/lksbot`
3. `/libsearch`: Talk to the alternate version of the bot that performs a search in the SMU Database using Primo API and retrieves data structured by ChatGPT. Start your prompt with `/libsearch`
4. `/lks` or `/kgc`: Retrieve the occupancy level in the respective libraries.


## Files
- See `tele-bot.ipynb` for telegram integration of all models mentioned above.
- Replace API keys in their respective placeholders.


## Areas for Improvement
- The bot can be finetuned on the conversation history as well (see the raw data in the merged output folder) which will complement the FAQs finetuning and improve the conversation. Hope to reduce hallucinations and more contextualize the conversation to SMU Libraries.
- Improve the Primo API search area for the bot as the current level of this part is very basic.
