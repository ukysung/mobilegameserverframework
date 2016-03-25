
import json
#import decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import g

class Model:
    table = None
    table_name = ''
    test_key = {}

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb',
                                       aws_access_key_id=None,
                                       aws_secret_access_key=None,
                                       region_name='',
                                       endpoint_url=g.CFG['dynamodb']['endpoint_url'])

        self.table = self.dynamodb.Table(self.table_name)

    def delete_table(self):
        response = self.table.delete()
        print(response)

        self.table.meta.client.get_waiter('table_exists')
        print('table status: ' + self.table.table_status)

    def put(self, item):
        return self.table.put_item(Item=item)

    def put_if_not(self, item, attr, value):
        response = None

        try:
            response = self.table.put_item(
                Item=item,
                ConditionExpression=Attr(attr).ne(value) #& Attr('title').ne(title)
            )

        except ClientError:
            pass

        return response

    def get(self, key):
        response = self.table.get_item(Key=key)

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def query(self, key, value):
        response = self.table.query(KeyConditionExpression=Key(key).eq(value))

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

        return self.table.update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
            #ReturnValues='ALL_NEW'
        )

    '''
    def update_if(self, key, data):
        response = None

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

        except ClientError:
            pass

        return response
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

        return self.table.update_item(
            Key=key,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
        )

    def append(self, key, attr, value):
        return self.table.update_item(
            Key=key,
            UpdateExpression='set ' + attr + ' = list_append(' + attr + ', :value)',
            ExpressionAttributeValues={
                ':value': [value],
            },
            ReturnValues='UPDATED_NEW'
        )

    def delete(self, key):
        return self.table.delete_item(Key=key)

    '''
    def delete_if(self, key, attr, value):
        response = None

        try:
            response = self.table.delete_item(
                Key=key,
                ConditionExpression='rating <= :value',
                ExpressionAttributeValues={
                    ':value': value
                }
            )

        except ClientError:
            pass

        return response
    '''

