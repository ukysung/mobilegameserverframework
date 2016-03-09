
import sys
import json

import g
from ModelUsers import ModelUsers

import config

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 ./create_dynamodb_tables.py develop')
        sys.exit()

    phase = sys.argv[1]
 
    config.load(phase)

    model_users = ModelUsers()
    #model_users.create()
    #model_users.put()

if __name__ == '__main__':
    main()

