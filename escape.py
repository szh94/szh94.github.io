import json

with open('oldblock.txt', 'r', encoding='utf-8') as f:
    old = f.read()
with open('newblock.liquid', 'r', encoding='utf-8') as f:
    new = f.read()

old_escaped = json.dumps(old)
new_escaped = json.dumps(new)

# Remove surrounding quotes
print(old_escaped[1:-1])
print('---')
print(new_escaped[1:-1])