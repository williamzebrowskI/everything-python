import json
import sys
import random
import requests
if __name__ == '__main__':
    url = "https://hooks.slack.com/services/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"
    message = ("Test Message")
    title = (f"Incoming Test Results :zap:")
    slack_data = {
        "username": "PyBot",
        "icon_emoji": ":snake:",
        #"channel" : "#somerandomcahnnel",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)

        