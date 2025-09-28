import json
import boto3
import urllib.request
import xml.etree.ElementTree as ET

def lambda_handler(event, context):
    # Fetch all global GDACS events
    url = "https://gdacs.org/xml/rss.xml"
    
    print(f"URL: {url}")
    
    try:
        with urllib.request.urlopen(url) as f:
            data = ET.fromstring(f.read().decode())
        print("API Status: 200")
    except Exception as e:
        print(f"Fetch error: {type(e).__name__}: {e}")
        return {"statusCode": 500, "body": f"Failed: {e}"}
    
    alerts = []
    for item in data.findall(".//item"):
        title = item.find("title").text
        alerts.append(f"Alert: {title}")
    
    if alerts:
        ses = boto3.client("ses", region_name="us-east-1")
        try:
            ses.send_email(
                Source="abhinavranascorpio@gmail.com",  
                Destination={"ToAddresses": ["abhinavranascorpio@gmail.com"]}, 
                Message={
                    "Subject": {"Data": "Disaster Alert"},
                    "Body": {"Text": {"Data": "\n".join(alerts)}}
                }
            )
            print(f"Sent {len(alerts)} alerts")
        except Exception as e:
            print(f"SES error: {e}")
            return {"statusCode": 500, "body": f"SES failed: {e}"}
    
    return {"statusCode": 200, "body": f"{len(alerts)} alerts"}
