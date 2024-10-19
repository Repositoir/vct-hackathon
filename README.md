# VCT Hackathon - Riot Games x AWS - Submission

This is the official code repository containing code useful in creating an LLM that provides
information regarding VALORANT games and players using the features provided by 
Amazon Bedrock on the operations side of the LLM.

## Basic Instructions

Ensure all packages and dependencies are up-to-date with

```shell
pip install -r requirements.txt
```
---
## Contents

This project contains two files `lambda.py` and `local.py`. Both of these files attribute
to some similar tasks which are

- Read the S3 bucket data
- Unzip the file using `gzip` library
- Delete S3 bucket occurrences of any files with a `.gz` extension

### Lambda

The `lambda.py` file is the code written for an AWS Lambda function which can be
tested and deployed on the AWS Console. The event and context parameters are automatically passed when deploying.

**Ensure you have the required permissions from IAM for depolying this function.**

### Local

The second file `local.py` is for completing the task using a simple Python 3.10 or higher
interpreter for an S3 bucket on your account.

**Ensure you have the Secret Access Keys configured using `aws configure` for your account**
