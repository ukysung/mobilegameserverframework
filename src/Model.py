
import json
#import decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import g

class Model:
    def __init__(self):
        self.table_name = ''
        self.test_key = {}

        self.dynamodb = boto3.resource('dynamodb',
                                       aws_access_key_id=None,
                                       aws_secret_access_key=None,
                                       region_name='',
                                       endpoint_url=g.CFG['dynamodb']['endpoint_url'])

        self.table = self.dynamodb.Table(self.table_name)

    def delete_table(self):
        response = self.table.delete()

        print(response)
        #print(json.dumps(response))

        self.table.meta.client.get_waiter('table_exists')
        print('table status: ' + self.table.table_status)

    def put(self, item):
        response = self.table.put_item(Item=item)

        print(json.dumps(response))

    def put_if_not(self, item, attr, value):
        try:
            response = self.table.put_item(
                Item=item,
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
        response = self.table.query(KeyConditionExpression=Key(key).eq(value))

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def get(self, key):
        response = self.table.get_item(Key=key)

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def update(self, key, data):
        expression = 'set '
        names = {}
        values = {}

        i = 0
        for name, value in data.items():
            i += 1
            if i > 1:
                expression += ', '

            expression += 'attr' + str(i) + ' = :value' + str(i)
            names['attr' + str(i)] = name
            values[':value' + str(i)] = value

        response = self.table.update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
            #ReturnValues='ALL_NEW'
        )

        print(json.dumps(response))

    '''
    def update_if(self, key, data):
        try:
            response = self.table.update_item(
                Key=key,
                UpdateExpression='remove actors[0]',
                ConditionExpression='size(actors) > :num',
                ExpressionAttributeValues={
                    ':num': data['num']
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
    '''

    def increase(self, key, data):
        expression = 'set '
        names = {}
        values = {}

        i = 0
        for name, value in data.items():
            i += 1
            if i > 1:
                expression += ', '

            expression += 'attr' + str(i) + ' = attr' + str(i) + ' + :value' + str(i)
            names['attr' + str(i)] = name
            values[':value' + str(i)] = value

        response = self.table.update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
        )

    def append(self, key, attr, value):
        response = self.table.update_item(
            Key=key,
            UpdateExpression='set ' + attr + ' = list_append(' + attr + ', :value)',
            ExpressionAttributeValues={
                ':value': [value],
            },
            ReturnValues='UPDATED_NEW'
        )

        print(json.dumps(response))

    def delete(self, key):
        response = self.table.delete_item(Key=key)

        print(json.dumps(response))

    '''
    def delete_if(self, key, attr, value):
        try:
            response = self.table.delete_item(
                Key=key,
                ConditionExpression='rating <= :value',
                ExpressionAttributeValues={
                    ':value': value
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
    '''
