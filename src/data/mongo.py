# Uploading data to mongoDB
import pymongo
from pymongo import MongoClient
import os
import numpy as np
import json

# cluster = MongoClient('mongodb+srv://root:<password>@routectijuana.aziov99.mongodb.net/?retryWrites=true&w=majority')
# db = cluster['SignAI']
# collection = db['signs']

DATA_PATH = os.path.join('data','ABC')
JSON_PATH = os.path.join('JSON','ABC')
signs = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 
                    'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

action = {
    'action':'',
    'categorie':'',
    'sequences':{
        
    }
}

# Returns a list of lists with all frames's landmarks
def get_frames(sign, sequence_num):
    sequence = []
    for frame in range(30):
        array = np.load(os.path.join(DATA_PATH,sign,str(sequence_num),str(frame)+'.npy'))
        to_list = array.tolist()
        sequence.append(to_list)
    return sequence

# Adds the secuences to the dictionary
def get_sequences(sign):
    for sequence in range(30):
        frames = get_frames(sign,sequence)
        action['sequences'][str(sequence)] = frames
    print('Got all sequences for "{}".'.format(sign))

# Saves the sequences to .json file
action['categorie'] = 'abc'
for sign in signs:
    action['action'] = sign.lower()
    get_sequences(sign)
    with open(os.path.join(JSON_PATH,sign+'.json'),'w') as outfile:
        json.dump(action,outfile)
        print('Saved action "{}" to JSON.'.format(sign))