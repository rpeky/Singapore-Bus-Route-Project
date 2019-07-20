from watson_developer_cloud import conversation_v1
import pprint
import json

USERNAME = "1c276a86-e188-42ab-ac51-c4b589abe702"
PASSWORD = "3tzwkaqnG0on"
WORKSPACE_ID = "279d0b2a-4058-4593-86df-e9349e895218"

def command(command, context):
    #Receives commands directed at the bot and returns the response from Watson Conversation
    conversation = conversation_v1.ConversationV1(
        username = USERNAME,
        password = PASSWORD,
        version = '2017-05-26'
        )

    responseFromWatson = conversation.message(
        workspace_id = WORKSPACE_ID,
        input = {'text': command},
        context = context
       )

    context = responseFromWatson['context']
    return responseFromWatson, context

if __name__ == "__main__":
    context_1 = {}
    newJSON,context_1 = command("bus 12",context_1)
    print(json.dumps(newJSON, indent=2))
    print(newJSON['intents'][0]['intent'])
    print(newJSON['output']['text'][0])
    newJSON,context_1 = command("blk 429",context_1)
    print(json.dumps(newJSON, indent=2))
    print(newJSON['output']['text'][0])
    print(newJSON['context']['service_no'])

    if (newJSON['output']['text'][0] == "Ok, I am searching for the arrival times..."):
        print("Yes it works")