import json
chat = []
name_1 = input('Enter first name: ')
name_2 = input('Enter second name: ')
while True:
    chat_1 = input(f'{name_1} >>> ')
    if chat_1 == 'Exit':
        break
    else:
        chat.append(chat_1)
    chat_2 = input(f'{name_2} >>> ')
    if chat_2 == 'Exit':
        break
    else:
        chat.append(chat_2)
intents = json.loads(open('intensts.json').read())
intents2 = json.dumps(intents)
intents3 = ''
for i in range(len(intents2)-2):
    intents3 += intents2[i]
def add_tag(i, message, message2):
    tag_templateNoTag = """,{"tag":"""
    tag_templateNopatterns = ""","patterns":"""
    tag_templateNoresponses = """, "responses":"""
    tag_templateEND = """",context":[""]}"""
    intent = str(f'{intents3}{tag_templateNoTag}{i}{tag_templateNopatterns}{message}{tag_templateNoresponses}{message2}{tag_templateEND}')
    return intent

for i in range(len(chat)-1):
    exec(f"intents3 = (add_tag({i}, [\'{chat[i]}\'], [\'{chat[i+1]}\']))")
print(intents3)
