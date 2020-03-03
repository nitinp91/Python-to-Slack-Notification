import logging, os, json
from base64 import b64decode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#Update following variables before test.
SLACK_WEBHOOK_URL='https://hooks.slack.com/services/<SLACK_WEBHOOK_DETAILS>'
SLACK_CHANNEL_NAME=<SLACK_CHANNEL_NAME>     #Exaple: '#my-reporting-slack-channel'
SLACK_USERNAME=<SLACK_USERNAME>        #Exaple: 'reporting-user'
SLACK_ICON_EMOJI=':robot_face:'

#Logging Variables
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Slack Message function
def lambda_to_slack(SLACK_MSG):
    payload = {'text':SLACK_MSG,'channel':SLACK_CHANNEL_NAME,'icon_emoji':SLACK_ICON_EMOJI,'username':SLACK_USERNAME}
    print('Sending Message to Slack')
    req = Request(SLACK_WEBHOOK_URL, json.dumps(payload).encode('utf-8'))
    try:
        response = urlopen(req)
        response.read()
        logger.info("Message posted to %s", payload['channel'])
    except HTTPError as e:
        logger.error("Request failed: %d %s", e.code, e.reason)
    except URLError as e:
        logger.error("Server connection failed: %s", e.reason)
    return 0

#Lamdba Function Code
def lambda_handler(event, context):
    # TODO implement
    lambda_to_slack('hello from AWS')
    return 0
