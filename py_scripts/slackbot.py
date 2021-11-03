from slack import WebClient
from slack.errors import SlackApiError
import os,sys

#create an app at https://api.slack.com/apps/
#go to General information about the app
#add following scopes
#		chat:write
#		?channels:join
slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)
if len(sys.argv) == 1:
	#print("No message received, messaging default")
	message = 'Job finished, come and have a look ..-)'
else:
	message = " ".join(sys.argv[1:])
response = client.chat_postMessage(channel="UGDV29T2L", text=message)
#Kika: UGDV29T2L
#Zoli: UGEKVC26P

print(response["ok"])