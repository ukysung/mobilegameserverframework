
import json

import boto3
import g

class ModelUsers:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='',
                                       endpoint_url=g.CFG['dynamodb']['endpoint_url'])

    def create(self):
        table = self.dynamodb.create_table(
            TableName='users',
            KeySchema=[
                {
                    'AttributeName': 'userid',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'userid',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        table.meta.client.get_waiter('table_exists')
        print('table status: ' + table.table_status)

    def put(self):
        userid = 'userid'
        passwd = 'passwd'

        table = self.dynamodb.Table('users')

        result = table.put_item(
            Item={
                'userid': userid,
                'passwd': passwd
            }
        )

        print(json.dumps(result))

