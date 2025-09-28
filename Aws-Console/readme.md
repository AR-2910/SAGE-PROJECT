# AWS Console Screenshots

This directory contains screenshots from the AWS Management Console, illustrating the configuration and execution of the SAGE PROJECT's serverless pipeline.

## Screenshot Descriptions

- **`IAM-Role.png`**  
  Displays the `SimpleAlert` IAM role with `AWSLambdaBasicExecutionRole` and `AmazonSESFullAccess` policies.

- **`Eventbridge-Rule.png`**  
  Shows the `WeatherAlert` EventBridge rule with a 15-minute schedule triggering `USGS` and `GDACS` lambda functions.

- **`Lambda-test-usgs.png`**  
  Captures logs for `USGS Lambda Function` test execution (e.g., "Sent X quakes").

- **`Lambda-test-gdacs.png`**  
  Captures logs for `GDACS Lambda Function` test execution (e.g., "Sent X alerts").
