
import sys

import g
import config
from ModelUsers import ModelUsers

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
    models.append(ModelUsers())

    if command == 'create':
        for model in models:
            model.create_table()

    elif command == 'delete':
        for model in models:
            model.delete_table()

if __name__ == '__main__':
    main()

