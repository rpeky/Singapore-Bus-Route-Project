from flask import Flask, request
from watson_developer_cloud import ConversationV1
import json
import requests
import os
import handle_conversation
import lta_api
import pprint
import textrec

app = Flask(__name__)

#Facebook Page Access Token
PAT = "EAACC9mbh3H0BAJFevcHgTWTZA5ljFmtd1EAZAqIUo8ukaMfBLkktCl7qZBcoYLPIiZCiA693oDtLUNtArdnkGZBa2yFVhyu2nH6FGgny80D3Vo9UNmYcUg6HOZCJGwF1U7ZBZCvgG6F5M9cwDjJlc3scZBtwLc4qgq4zJhdo1zECqSAZDZD"

#Watson Conversation service credentials
USERNAME = "1c276a86-e188-42ab-ac51-c4b589abe702"
PASSWORD = "3tzwkaqnG0on"
WORKSPACE_ID = "279d0b2a-4058-4593-86df-e9349e895218"
 
#Watson Conversation data
conversation = ConversationV1(
  username = USERNAME,
  password = PASSWORD,
  version = '2017-05-26'
)

curr_bus_stop = ""
service_no = ""


@app.route('/',methods=['GET']) 
def handle_verification(): #verify sending of data from Facebook to webhook
	print ("Handling Verification")
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if request.args.get("hub.verify_token") == "token123":
			print ("Verification successful!")
			return request.args.get("hub.challenge"), 200
		else:
			print ("Verification failed.")
			return "Error: Wrong verification token", 403

	return "ok", 200 

context = {}

#to handle user messages
@app.route('/', methods=['POST']) 
def handle_messages():
	print ("Handling Messages")

	global curr_bus_stop
	global service_no
	global context
	
	data = request.get_json()
	if data["object"] == "page":
		print("Receiving message, printing data...")
		print(data)

		for entry in data["entry"]:
			for messaging_event in entry["messaging"]:        
				if messaging_event.get("message"): #user sent a message
					recipient_id = messaging_event["recipient"]["id"] # the recipient's ID
					message_info = messaging_event["message"]  #information about the message sent (may be text or image)
					sender_id = messaging_event["sender"]["id"] #the facebook ID of the user

					if "attachments" in message_info: #User sent an attachment(image) - will NOT send data to Watson Conversation

						#Need to consider exception handling for other types of attachments
						img_url = message_info["attachments"][0]["payload"]["url"]
						send_message(sender_id,"I am processing your image...")
						print("Processing image")
						text = textrec.findcoderect(img_url)
						if text: #if a bus stop code was recognised
							print("Detected a code, replying...")
							send_message(sender_id,"The recognised code was " + "'" + text + "'.\n" + "I am finding the arrival times now..." )
							print("Finding all arrival data...")
							ans = lta_api.all_arrival_data(text) 
							reply = "These are the buses at your bus stop:\n\n" + ans
							send_message(sender_id,reply)

						else:
							print("Could not detect a code, replying...")
							send_message(sender_id, "I'm sorry, I could not recognise a bus stop code.\n\nTips:\n\n - I work best with pictures where the stop code directly faces the camera.\n\n - Make sure the image is taken such that the code is parallel to the ground.")
						
						print("TEXTREC FIN")
						
					elif "text" in message_info: #User sent a text message - will send data to Watson Conversation

						message_text = message_info["text"]
						newJSON, context = handle_conversation.command(message_text,context)
						print(json.dumps(newJSON,indent=2))
						reply = newJSON['output']['text'][0]

						send_message(sender_id,reply) #sends reply from Watson

						#newJSON['context']['node'] only refers to the node that was just finished, not the node reached.

						if not newJSON['context'].get('node'):
							print("No registered node")
							return "ok", 200

						if newJSON['context']['node'] == "Help":
							print("Help")

						if newJSON['context']['node'] == "Greetings":
							print("Greetings")

						if newJSON['context']['node'] == "Farewell":
							print("Farewell")

						if newJSON['context']['node'] == "Thanks":
							print("Thanks")

						if newJSON['context']['node'] == "Enquiry for bus services":
							if newJSON['context'].get('service_no'):
								service_no = newJSON['context']['service_no']  
								print("Enquiry for bus services (bus no. provided)") 
							
							else:
								print("Enquiry for bus services (bus no. not provided)")

						if newJSON['context']['node'] == "Find arrival times":
							curr_bus_stop = newJSON['context']['curr_bus_stop']
							nextbus,nextbus2,nextbus3 = lta_api.single_arrival_data(curr_bus_stop,service_no) #consider case where curr_bus_stop and service_no = ""
							reply = "Bus " + str(service_no) + ":\n\n" + "The next 3 buses are coming in:\n" + nextbus + "\n" + nextbus2 + "\n" + nextbus3 + "\n" 
							send_message(sender_id,reply)
							print("Find arrival times") #just received bus stop name
							context = {}

						if newJSON['context']['node'] == "Enquiry for bus routes":
							selected_bus_route = lta_api.route_data(newJSON['context']['service_no'])
							reply = ""
							for stop in selected_bus_route:
								reply += (stop + "\n")
							send_message(sender_id,reply)

						if newJSON['context']['node'] == "Anything else":
							print("Anything else")
							newJSON = {} #to prevent context mixup errors
							context = {} 

					else: 
						pass

	return "ok", 200 

def send_message(recipient,message):

	params = {
		"access_token": PAT
	}
	
	headers = {
		"Content-Type": "application/json"
	}
	
	data = json.dumps({
		"recipient" : {
			"id": recipient
		 },
		"message" : {
			"text": message
		 }
	})
	
	r = requests.post("https://graph.facebook.com/v2.6/me/messages", #sends the message for directed user to the Facebook Graph API
	params = params,
	headers = headers,
	data = data)
	
	print (r.text)


port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=int(port))