
import sys
import json

import boto3

import g
import config

from ModelUsers import ModelUsers
from ModelCharacters import ModelCharacters
from ModelItems import ModelItems
from ModelSkill import ModelSkill
from ModelDungeon import ModelDungeon
from ModelQuest import ModelQuest
from ModelGuild import ModelGuild
from ModelGuildMember import ModelGuildMember
from ModelFriend import ModelFriend

def main():
    if len(sys.argv) < 3:
        print('Usage: python3 ./dynamodb_tables_tools.py develop create')
        sys.exit()

    g.PHASE = sys.argv[1]
    command = sys.argv[2]

    if command == 'delete':
        #pass
        sys.exit()

    config.load()

    models = []
    #models.append(ModelUsers())
    #models.append(ModelCharacters())
    #models.append(ModelItems())
    models.append(ModelSkill())
    #models.append(ModelDungeon())
    #models.append(ModelQuest())
    #models.append(ModelGuild())
    #models.append(ModelGuildMember())
    #models.append(ModelFriend())

    if command == 'list':
        dynamodb = boto3.resource('dynamodb',
                                  aws_access_key_id=None,
                                  aws_secret_access_key=None,
                                  region_name='',
                                  endpoint_url=g.CFG['dynamodb']['endpoint_url'])

        for table in dynamodb.tables.all():
            print(table.name)

    elif command == 'create':
        for model in models:
            response = model.create_table()
            print(json.dumps(response))

    elif command == 'test':
        for model in models:
            response = model.test()

    elif command == 'delete':
        for model in models:
            response = model.delete_table()
            print(json.dumps(response))

if __name__ == '__main__':
    main()

