import json
from botocore.vendored import requests

#Update following variables before test.
SLACK_WEBHOOK_URL='https://hooks.slack.com/services/<SLACK_WEBHOOK_DETAILS>'
SLACK_CHANNEL_NAME=<SLACK_CHANNEL_NAME>     #Exaple: '#my-reporting-slack-channel'
SLACK_USERNAME=<SLACK_USERNAME>        #Exaple: 'reporting-user'
SLACK_ICON_EMOJI=':robot_face:'

#Slack Message function
def lambda_to_slack(SLACK_MSG):
    payload = {'text':SLACK_MSG,'channel':SLACK_CHANNEL_NAME,'icon_emoji':SLACK_ICON_EMOJI,'username':SLACK_USERNAME}
    print('Sending Message to Slack')
    r = requests.post(SLACK_WEBHOOK_URL, json=payload)
    return 'Message sent to Slack' 

#Lamdba Function Code
def lambda_handler(event, context):
    # Calling Slack function
    lambda_to_slack('Hello from Python')
    return 0
