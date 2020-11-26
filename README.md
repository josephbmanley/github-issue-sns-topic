![Build & Ship](https://github.com/josephbmanley/github-issue-sns-topic/workflows/Build%20&%20Ship/badge.svg)

# GitHub Issues SNS Topic

Simple CloudFormation stack for creating a SNS Topic that creates issues on GitHub.

![Diagram](https://static.cloudsumu.com/github-issues/diagram.png)

## Launch Options

### Launch from CloudFormation Console

Make sure you are logged into the AWS Console and have permissions then click:

[![Launch Stack](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=Nakama&templateURL=https://sumu-stacks.s3.amazonaws.com/github-issues/top.yaml)

Then fill out the parameters!

**Note:** Your secret must contain your token as a raw string.

### Download Template

The template is public accessible at: [https://sumu-stacks.s3.amazonaws.com/github-issues/top.yaml](https://sumu-stacks.s3.amazonaws.com/github-issues/top.yaml)

You can either download the template from your web browser or use something like the wget command.

`wget https://sumu-stacks.s3.amazonaws.com/github-issues/top.yaml`

Then use your prefered deployment method!