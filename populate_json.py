import json

# Read current database
with open('tables.json', 'r') as f:
    tables = json.load(f)

# Read temporary table file
with open('temp.txt', 'r') as f:
    temp = [line.rstrip() for line in f]

# update JSON. Remember to adjust the keys
#tables['UNE'] = {}  # uncomment if new system table (e.g. UNE, MYTHIC, ironsworn...)
tables['UNE']['NPC-focus'] = temp
with open('tables.json', 'w') as f:
    json.dump(tables, f, indent=2)
