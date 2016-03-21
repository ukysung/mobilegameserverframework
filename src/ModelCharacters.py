
import json
#import decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import g

class ModelUsers:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='',
                                       endpoint_url=g.CFG['dynamodb']['endpoint_url'])
        self.table_name = 'characters'

    def create_table(self):
        table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'user_id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'user_id',
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

    def delete_table(self):
        table = self.dynamodb.Table(self.table_name)
        response = table.delete()

        print(json.dumps(response))

        table.meta.client.get_waiter('table_exists')
        print('table status: ' + table.table_status)

    def put(self, item_dict):
        table = self.dynamodb.Table(self.table_name)
        response = table.put_item(Item=item_dict)

        print(json.dumps(response))

    def put_if(self, item_dict, attr, value):
        table = self.dynamodb.Table(self.table_name)

        try:
            response = table.put_item(
                Item=item_dict,
                ConditionExpression=Attr(attr).ne(value) #& Attr('title').ne(title)
            )

        except ClientError as ex:
            if ex.response['Error']['Code'] == 'ConditionalCheckFailedException':
                print(ex.response['Error']['Message'])

            else:
                raise

        else:
            print('PutItem succeeded:')

        print(json.dumps(response))

    def query(self, key, value):
        table = self.dynamodb.Table(self.table_name)
        response = table.query(KeyConditionExpression=Key(key).eq(value))

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def get(self, key_dict):
        table = self.dynamodb.Table(self.table_name)
        response = table.get_item(Key=key_dict)

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def update(self, key_dict, val_dict):
        table = self.dynamodb.Table(self.table_name)
        response = table.update_item(
            Key=key_dict,
            UpdateExpression='set a = :a, b = :b',
            ExpressionAttributeValues={
                ':a': val_dict['a'],
                ':b': val_dict['b']
            },
            ReturnValues='UPDATED_NEW'
        )

        print(json.dumps(response))

    def update_if(self, key_dict, val_dict):
        table = self.dynamodb.Table(self.table_name)

        try:
            response = table.update_item(
                Key=key_dict,
                UpdateExpression='remove actors[0]',
                ConditionExpression='size(actors) > :num',
                ExpressionAttributeValues={
                    ':num': val_dict['num']
                },
                ReturnValues='UPDATED_NEW'
            )

        except ClientError as ex:
            if ex.response['Error']['Code'] == 'ConditionalCheckFailedException':
                print(ex.response['Error']['Message'])

            else:
                raise

        else:
            print('PutItem succeeded:')

        print(json.dumps(response))

    def increase(self, key_dict, val_dict):
        table = self.dynamodb.Table(self.table_name)
        response = table.update_item(
            Key=key_dict,
            UpdateExpression='set a = a + :a',
            ExpressionAttributeValues={
                ':a': val_dict['a']
            },
            ReturnValues='UPDATED_NEW'
        )

        print(json.dumps(response))

    def delete(self, key_dict):
        table = self.dynamodb.Table(self.table_name)
        response = table.delete_item(Key=key_dict)

        print(json.dumps(response))

    def delete_if(self, key_dict):
        table = self.dynamodb.Table(self.table_name)

        try:
            response = table.delete_item(
                Key=key_dict,
                ConditionExpression='rating <= :val',
                ExpressionAttributeValues={
                    ':val': 5
                }
            )

        except ClientError as ex:
            if ex.response['Error']['Code'] == 'ConditionalCheckFailedException':
                print(ex.response['Error']['Message'])

            else:
                raise

        else:
            print('PutItem succeeded:')

        print(json.dumps(response))


