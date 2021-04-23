#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from cdk_lambda_dynamodb_fargate.cdk_lambda_dynamodb_stack import CdkLambdaDynamodbStack
from cdk_lambda_dynamodb_fargate.cdk_fargate_stack import FargateStack

app_env = {
    "region": "us-east-1"
}
app = cdk.App()

CdkLambdaDynamodbStack(app, "cdk-lambda-dynamodb", env=app_env)
FargateStack(app, "cdk-fargate", env=app_env)

app.synth()
