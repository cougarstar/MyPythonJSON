''' JavaScript Object Notation '''
import json

with open('states.json') as f:
  data = json.load(f)

for state in data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)

"""
new_string = json.dumps(data, indent = 2, sort_keys=False)
print(new_string)

  """
