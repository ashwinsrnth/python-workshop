
import json

with open('my_data.json', 'r') as f:
    dat = json.load(f)

print dat['TestName']
print dat['alpha']['x']