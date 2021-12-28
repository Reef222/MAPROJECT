from msg_server.client import Client
import json
import time
from threading import Thread
c1 = Client(input('Enter your name: '))
intents = json.loads(open('intensts.json').read())
intents2 = json.dumps(intents)
intents3 = ''
for i in range(len(intents2)-2):
    intents3 += intents2[i]


def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    global msgs
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 1/10 of a second
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages
        for msg in new_messages:  # display new messages
            print(msg)

            if msg == "{quit}":
                run = False
                break


Thread(target=update_messages).start()
while True:
    def add_tag(i, message, message2):
        tag_templateNoTag = """,{"tag":"""
        tag_templateNopatterns = """\n,"patterns":"""
        tag_templateNoresponses = """\n, "responses":"""
        tag_templateEND = """"\n, "context":[""]}]}"""
        message = f"[\"{message[0]}\", \"{message[0]}\", \"{message[0]}\"]"
        message2 = f"[\"{message2[0]}\", \"{message2[0]}\", \"{message2[0]}\"]"
        intent = str(f'{intents3}{tag_templateNoTag}\"{i}\"{tag_templateNopatterns}{message}{tag_templateNoresponses}{message2}{tag_templateEND}')
        intent = intent.replace(']\"', "]")
        intent = intent.replace("[\'", '[\"')
        intent = intent.replace("\']", '\"]')
        return intent
    msg = input()
    if msg == 'Make A Clone':
        chat_1 = msgs
        END_chat = []
        for msg in msgs:
            if 'has joined the chat!' in msg:
                chat_1.remove(msg)
        msgs = chat_1
        for msg in chat_1:
            _, msgg = msg.split(': ')
            END_chat.append(msgg)

        print(END_chat)
        for i in range(len(msgs) - 1):
            exec(f"intents3 = (add_tag({i}, [\"{END_chat[i]}\"], \n[\"{END_chat[i + 1]}\"]))")
        print(intents3)
        with open('intensts.json', 'w') as outfile:
            intents3 = json.loads(intents3)
            json.dump(intents3, outfile)


    else:
        c1.send_message(msg)
