import logging, boto3, os
from github import Github

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):

    # Secret Client
    secretsmanager = boto3.client('secretsmanager')

    # Get Secrets
    token = secretsmanager.get_secret_value(SecretId=os.environ.get("GITHUB_TOKEN_SECRET")).get("SecretString")
    
    # GitHub client
    github = Github(base_url=f"https://{os.environ.get('GITHUB_HOSTNAME','github.com')}/api/v3", login_or_token=token)

    repo = github.get_repo(os.environ.get("REPOSITORY"))

    if not "Records" in event:
        raise Exception("Missing key Records in event!")
        
    for record in event["Records"]:
        if "Sns" in record:
            sns_event = record["Sns"]
            repo.create_issue(sns_event["Subject"], body=sns_event["Message"] + "\nThis was generated by " + os.environ.get("GENERATED_OWNER", "AWS"))