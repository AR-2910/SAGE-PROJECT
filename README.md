# SAGE PROJECT: Serverless Analysis & Alerting for Geospatial Events

## Project Description
SAGE PROJECT is a serverless AWS pipeline delivering real-time global disaster alerts by analyzing geospatial data from USGS (earthquakes) and GDACS (floods, cyclones) APIs, using Lambda, EventBridge, and SES for scalable, cost-efficient alerting.

## Serverless Architecture and Features
SAGE PROJECT leverages a serverless distributed architecture with AWS Lambda, EventBridge, and SES for real-time geospatial event alerting.

### Key Features
- **Scalability**: Automatically scales with event volume, handling thousands of API requests without manual infrastructure.
- **Cost-Efficiency**: Pay-per-use model (~$0.06-0.08 for ~100 invocations, non-free tier), lower than traditional server-based systems.
- **Event-Driven Processing**: EventBridge triggers Lambdas every 15 minutes, ensuring low-latency alerts.
- **Decoupled Components**: Independent Lambda functions for modularity and fault tolerance.
- **USGS Earthquake Analysis**: Fetches magnitude, location, and time from USGS API.
- **GDACS Disaster Analysis**: Extracts flood, cyclone details from GDACS RSS feed.
- **Real-Time Email Alerts**: Sends structured SES emails.

**Advantages Over Existing Solutions**:
- **Lower Latency**: AWS global infrastructure ensures faster alerts than region-specific platforms.
- **Zero Infrastructure Management**: Serverless design avoids server overload during disasters, unlike traditional tools.
- **Cost Savings**: Pay only for invocations, cheaper than maintained servers (e.g., ~$0.06 vs. $10+/month for hosted alternatives).
- **Easy Customization**: Modular Lambdas allow quick additions (e.g., more APIs), unlike monolithic disaster monitoring software.

### How It Works
1. **Data Fetch**: Queries USGS API (JSON) and GDACS RSS feed (XML) for geospatial event data.
2. **Data Analysis**: Lambdas functions process JSON and XML data, extracting magnitude, location, time, and severity.
3. **Alerting Email**: EventBridge triggers Lambdas every 15 minutes; SES sends formatted email alerts with event details.


## Setup
1. **SES Configuration**:
   - Verify sender/recipient emails in AWS SES.
   - Replace `your-verified-sender@example.com` and `your-recipient@example.com` in `code` with verified emails.
2. **Lambda Deployment**:
   - Deploy Python 3.12 functions (`USGS`, `GDACS`) with `SimpleAlertRole` (IAM policies: `AWSLambdaBasicExecutionRole`, `AmazonSESFullAccess`).
3. **EventBridge Scheduling**:
   - Set `AlertSchedule` for 15-minute triggers.
4. **Testing**:
   - Run `{trigger: manual}` in Lambda console; check CloudWatch logs and emails.

## Visuals
- **Architecture**: [Architecture.png](Architecture.png)
- **Screenshots**: [Aws-Console/](Aws-Console/)

## Benefits and Limitations
- **Benefits**:
  - Delivers timely alerts with serverless scalability.
  - Minimizes costs and maintenance using AWS services.
  - Showcases AWS, Python, and API integration.
  
- **Limitations**:
  - Requires SES email verification to avoid delivery failures.

## Notes
- **Key Issues to Note**: Verify SES emails before deployment to avoid send failures; disable EventBridge rule after testing to prevent unnecessary costs (~$0.01/day if active).
- **Configuration Tips**: Ensure `SimpleAlertRole` has `AWSLambdaBasicExecutionRole` and `AmazonSESFullAccess`; check CloudWatch logs for API errors (e.g., network issues).
- **Cost Management**: Use AWS Cost Explorer or Budgets to monitor ~$0.06-0.08 costs; leverage free tier for initial testing.

## License
MIT License
