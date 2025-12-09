import requests

def slack_notification_send(webhook_url, message):
    payload = {
        "text": message
    }
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification. Status Code: {response.status_code}, Response: {response.text}")
# Example usage
webhook_url = "https://hooks.slack.com/services/your/webhook/url"
message = "This is a test notification from Python."
slack_notification_send(webhook_url, message)
