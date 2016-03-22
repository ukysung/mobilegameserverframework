
import sys

import g
import config
from ModelUsers import ModelUsers

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 ./create_dynamodb_tables.py develop')
        sys.exit()

    g.PHASE = sys.argv[1]

    config.load()

    model_users = ModelUsers()
    model_users.create_table()
    #model_users.put()

if __name__ == '__main__':
    main()

