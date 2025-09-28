import json
import boto3
import urllib.request
import datetime

def lambda_handler(event, context):
    # Fetch global earthquakes data (last 15 min)
    start_time = datetime.datetime.now(datetime.UTC) - datetime.timedelta(minutes=15)
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start_time:%Y-%m-%dT%H:%M:%SZ}&minmagnitude=0.0&limit=5"
    
    try:
        with urllib.request.urlopen(url) as f:
            data = json.loads(f.read().decode())
    except Exception as e:
        print(f"Fetch error: {type(e).__name__}: {e}")
        return {"statusCode": 500, "body": f"Failed: {e}"}
    
    alerts = []
    for event in data.get("features", []):
        props = event["properties"]
        time = datetime.datetime.fromtimestamp(props['time']/1000, tz=datetime.timezone.utc)
        alerts.append(f"Quake: Magnitude {props['mag']} at {props['place']} on {time:%Y-%m-%d %H:%M:%S UTC}")
    
    if alerts:
        ses = boto3.client("ses", region_name="us-east-1")
        try:
            ses.send_email(
                Source="your-verified-sender@example.com",  
                Destination={"ToAddresses": ["your-recipient@example.com"]},  
                Message={
                    "Subject": {"Data": "Earthquake Alert"},
                    "Body": {"Text": {"Data": "\n".join(alerts)}}
                }
            )
            print(f"Sent {len(alerts)} quakes")
        except Exception as e:
            print(f"SES error: {e}")
            return {"statusCode": 500, "body": f"SES failed: {e}"}
    
    return {"statusCode": 200, "body": f"{len(alerts)} quakes"}
