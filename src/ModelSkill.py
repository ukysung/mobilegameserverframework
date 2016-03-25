
from Model import Model

class ModelSkill(Model):
    def __init__(self):
        self.table_name = 'skil'
        self.test_key = {'char_name': 'test_char_01', 'skill_id': 1}
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
                    'AttributeName': 'skill_id',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'char_name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'skill_id',
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

