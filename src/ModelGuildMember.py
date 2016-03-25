
from Model import Model

class ModelGuildMember(Model):
    def __init__(self):
        self.table_name = 'guild_member'
        self.test_key = {'guild_name': 'test_guild_01', 'char_name': 'test_char_01'}
        Model.__init__(self)

    def create_table(self):
        new_table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'guild_name',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'char_name',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'guild_name',
                    'AttributeType': 'S'
                },
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

