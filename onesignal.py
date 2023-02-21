import requests
import os

def send_email():

    url = "https://onesignal.com/api/v1/notifications"

    payload = {
        "include_email_tokens": "alexanderray113@gmail.com",
        "email_subject": "Your Scheduled Reminder",
        "email_body": "this is a test email",
        "name": "REMINDERS",
        # "send_after": date,
        "app_id": "1d537ec0-da13-4d18-a15b-76c8cd68588b"
    }
    headers = {
        "accept": "application/json",
        "Authorization": "Basic MzJiYzhjOGEtNTE0ZC00MzUzLWIwMGItZmM1ODY4YTA1ODc2",
        "content-type": "application/json"
    }

    requests.post(url, json=payload, headers=headers)
    return print("Confirm function ran")
    