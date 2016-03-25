
from Model import Model

class ModelItems(Model):
    def __init__(self):
        self.table_name = 'items'
        self.test_key = {'char_name': 'test_char_01', 'item_id': 'test_item_01'}
        Model.__init__()

    def create_table(self):
        new_table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'char_name',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'item_id',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'char_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'item_id',
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

