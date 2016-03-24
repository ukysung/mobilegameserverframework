
import json
#import decimal

import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError

import g

class Model:
    def __init__(self):
        self.table_name = ''
        self.test_key_dict = {}

        self.dynamodb = boto3.resource('dynamodb',
                                       aws_access_key_id=None,
                                       aws_secret_access_key=None,
                                       region_name='',
                                       endpoint_url=g.CFG['dynamodb']['endpoint_url'])

        self.table = self.dynamodb.Table(self.table_name)

    def delete_table(self):
        response = table.delete()

        print(response)
        #print(json.dumps(response))

        table.meta.client.get_waiter('table_exists')
        print('table status: ' + table.table_status)

    def put(self, item_dict):
        response = table.put_item(Item=item_dict)

        print(json.dumps(response))

    def put_if_not(self, item_dict, attr, value):
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
        response = table.query(KeyConditionExpression=Key(key).eq(value))

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def get(self, key_dict):
        response = table.get_item(Key=key_dict)

        print(json.dumps(response))

        if 'Items' in response:
            return response['Items']

        else:
            return None

    def update(self, key_dict, update_dict):
        expression = 'set '
        names = {}
        values = {}

        i = 0
        for name, value in update_dict.items():
            i += 1
            if i > 1:
                expression += ', '

            expression += 'attr' + str(i) + ' = :val' + str(i)
            names['attr' + str(i)] = name
            values[':val' + str(i)] = value

        response = table.update_item(
            Key=key_dict,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
            #ReturnValues='ALL_NEW'
        )

        print(json.dumps(response))

    def update_if(self, key_dict, update_dict):
        try:
            response = table.update_item(
                Key=key_dict,
                UpdateExpression='remove actors[0]',
                ConditionExpression='size(actors) > :num',
                ExpressionAttributeValues={
                    ':num': update_dict['num']
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

    def increase(self, key_dict, increase_dict):
        expression = 'set '
        names = {}
        values = {}

        i = 0
        for name, value in increase_dict.items():
            i += 1
            if i > 1:
                expression += ', '

            expression += 'attr' + str(i) + ' = attr' + str(i) + ' + :val' + str(i)
            names['attr' + str(i)] = name
            values[':val' + str(i)] = value

        response = table.update_item(
            Key=key_dict,
            UpdateExpression=expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ReturnValues='UPDATED_NEW'
        )

        print(json.dumps(response))

        '''
        table = get_dynamodb_resource().Table("table_name")
            result = table.update_item(
                Key={
                    'hash_key': hash_key,
                    'range_key': range_key
                },
                UpdateExpression="SET some_attr = list_append(some_attr, :i)",
                ExpressionAttributeValues={
                    ':i': [some_value],
                },
                ReturnValues="UPDATED_NEW"
        )
        if result['ResponseMetadata']['HTTPStatusCode'] == 200 and 'Attributes' in result:
            return result['Attributes']['some_attr']
        '''

    def delete(self, key_dict):
        response = table.delete_item(Key=key_dict)

        print(json.dumps(response))

    def delete_if(self, key_dict):
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


