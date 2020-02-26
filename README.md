# Python-to-Slack-Notification

Slack has limitations in creating Webhooks in Free plan. However, we can use existing Webhook to send a notification in different Slack Channels. If we send Slack Payload to Webhook without mentioning Slack Channel name, the message will send to the default Slack Channel.

* Create Slack Webhook using https://slack.com/apps/A0F7XDUAZ this link and update SLACK_WEBHOOK_URL in code.
* Update SLACK_CHANNEL_NAME and SLACK_USERNAME
