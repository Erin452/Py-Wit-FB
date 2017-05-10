import os, sys 
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAADVZBnKZBXkEBABpVLuaTNMOwGaEkhTIyppleWiZALMPlkPgVLM5WFcetEEpCeECF3jBV7aGsslMY0pSeZBtUUxTu96XKnZBZC5w77gTIRZCi5IjNYdxCyJxDJBuQnjvF1FMwbM39DNgOLPjEqk4q4HcDvPvHZBP2NLazZAWYMsiZAwZDZD"
# fan page key 

bot = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods = ['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello bot":
			return "Failed validation. Make sure the validation tokens match.", 403
		return request.args["hub.challenge"], 200
	return "Hello", 200



@app.route('/', methods = ['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:
				# ID
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'No text'

					# Response
					response = messaging_text
					bot.send_text_message(sender_id, response)

	return "ok", 200

def log(message):
	print(message)
	sys.stdout.flush()



if __name__ == "__main__":
	app.run(debug = True, port = 80)