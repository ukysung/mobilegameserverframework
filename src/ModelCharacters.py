
from Model import Model

class ModelCharacters(Model):
    def __init__(self):
        self.table_name = 'characters'
        self.test_key = {'char_name': 'test_char_01'}
        Model.__init__(self)

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
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        new_table.meta.client.get_waiter('table_exists')
        print('new table status: ' + new_table.table_status)

    def test(self):
        self.put(self.test_key)
        self.get(self.test_key)
        self.delete(self.test_key)

