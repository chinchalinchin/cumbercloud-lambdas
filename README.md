# Cumberland Cloud Backend

This repository houses the source code and deployment configuration files for the backend of my personal website and portfolio. Logic is implemented and deployed to [AWS Serverless Lambda Functions](). These functions are integrated with a variety of triggers: [CloudWatch events](https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents.html), [SES Receipt Rules](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html) and [API Gateway Integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-lambda-integration.html)

The frontend source for this application can be found [here](https://github.com/chinchalinchin/cumbercloud-web).

## Quickstart

### Build

```shell
docker build --tag cumbercloud-send-email:latest --file Dockerfile ./lambdas/mail/send/
docker build --tag cumbercloud-forward-email:latest --file Dockerfile ./lambdas/mail/forward/
docker build --tag cumbercloud-token:latest --file Dockerfile ./lambdas/auth/token/
docker build --tag cumbercloud-register:latest --file Dockrefile ./lambdas/auth/register/
```

### Run

```shell
docker run -p 9000:8080 cumbercloud-send-email:latest
docker run -p 9001:8080 cumbercloud-forward-email:latest
docker run -p 9002:8080 cumbercloud-token:latest
docker run -p 9003:8080 cumbercloud-register:latest
```

### Use

```shell
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"payload":"hello world 1!"}'
curl -XPOST "http://localhost:9001/2015-03-31/functions/function/invocations" -d '{"payload":"hello world 2!"}'
curl -XPOST "http://localhost:9002/2015-03-31/functions/function/invocations" -d '{"payload":"hello world 3!"}'
curl -XPOST "http://localhost:9003/2015-03-31/functions/function/invocations" -d '{"payload":"hello world 4!"}'

```

**NOTE**: Regardless of the **API Gateway** method integration, when the **Lambdas** are run locally, they are exposed as **POST** endpoints. This is due to **API Gateway** transforming all requests into **POSTS** before passing them off to **Lambda** when running on the cloud. 

TODO

### Deployment

TODO

## Architecture

TODO

## Docker

All of the **Lambda** images use as their base the [official AWS Python Lambda image located here](https://hub.docker.com/r/amazon/aws-lambda-python).
