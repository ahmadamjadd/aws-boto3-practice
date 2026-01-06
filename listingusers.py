import boto3

aws_management_console = boto3.session.Session(profile_name = "default")
resource = aws_management_console.resource("iam")
client = aws_management_console.client("iam")

for each_user in resource.users.all():
    print(each_user.name)

print(client.list_users())