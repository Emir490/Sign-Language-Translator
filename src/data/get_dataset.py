import os
import json
from ..utils.index import actions

PATHS =  ['ABC', 'ABCRAUL', 'ABCSignAI', 'Abecedario', 'Actions']

merged_data = {}

# for path in PATHS:
#     for filename in os.listdir(f"Actions/{path}"):
#         print(filename)
#         if filename == 'RR.json' or filename == 'LL.json':
#             print(filename)
#             with open(os.path.join(f"Actions/{path}", filename), 'r') as f:
#                 data = json.load(f)
                
#             letter = filename[:2]
            
#             if letter in merged_data:
#                 merged_data[letter].extend(data)
#             else:
#                 merged_data[letter] = data
            
# for letter, data in merged_data.items():
#     with open(os.path.join("merged", f"{letter}.json"), 'w') as f:
#         json.dump(data, f)

for action in actions:
    with open(f'merged/{action}.json', 'r') as file:
        print(action)
        data: list = json.load(file)
        counter = len(data)
        print(counter)
        if counter < 240: print(f"!!!REPETIR {action}!!!")
        
        for element in data:
            sign = element["action"]
            if action != sign:
                print(action, sign)
                
        # if action == 'Ñ':
        #     for element in data:
        #         sign = element["action"]
        #         if action != sign:
        #             element["action"] = action
        #     with open(f"{action}.json", 'w') as f:
        #         json.dump(data, f)
                
        # if counter > 48:
        #     if counter == 50:
        #         data.pop()
        #         data.pop()
        #     else: data.pop()
        #     with open(f"{action}.json", 'w') as f:
        #         json.dump(data, f)