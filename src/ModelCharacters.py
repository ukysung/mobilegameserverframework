
from Model import Model

class ModelCharacters(Model):
    def __init__(self):
        self.table_name = 'characters'
        self.test_key = {'char_name': 'test_char_01'}
        Model.__init__()

    def create_table(self):
        new_table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'char_name',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'char_name',
                    'AttributeType': 'S'
                }
                '''
                ,
                {
                    'AttributeName': 'user_id',
                    'AttribyteType': 'S'
                }
                '''
            ],
            '''
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'user_id',
                    'KeySchema': [
                        {
                            'AttributeName': 'user_id',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                }
            ],
            '''
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        new_table.meta.client.get_waiter('table_exists')
        print('new table status: ' + new_table.table_status)

