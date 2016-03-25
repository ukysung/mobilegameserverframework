
from Model import Model

class ModelQuest(Model):
    def __init__(self):
        self.table_name = 'quest'
        self.test_key = {'char_name': 'test_char_01', 'quest_mid': 1}
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
                    'AttributeName': 'quest_mid',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'char_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'quest_mid',
                    'AttributeType': 'N'
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

