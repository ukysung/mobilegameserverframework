
from Model import Model

class ModelFriend(Model):
    def __init__(self):
        self.table_name = 'friend'
        self.test_key = {'char_name': 'test_char_01', 'friend_char_name': 'test_char_02'}
        Model.__init__(self)

    def create_table(self):
        new_table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'char_name',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'friend_char_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'char_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'frined_char_name',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        new_table.meta.client.get_waiter('table_exists')
        print('new table status: ' + new_table.table_status)

