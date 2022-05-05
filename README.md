# Cumberland Cloud Backend

This repository houses the source code and deployment configuration files for the backend of my personal website and portfolio. Logic is implemented and deployed to [AWS Serverless Lambda Functions](). These functions are integrated with a variety of triggers: [CloudWatch events](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html), [SES Receipt Rules](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html) and [API Gateway Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

The frontend source for this application can be found [here](https://github.com/chinchalinchin/cumbercloud-web).

## Quickstart

### Local

```shell
docker build --tag cumbercloud-send-email:latest --file Dockerfile ./lambdas/email/send/
docker build --tag cumbercloud-forward-email:latest --file Dockerfile ./lambdas/email/forward/
```

TODO

### Deployment

TODO

## Architecture

TODO
