# Uploading data to mongoDB
import pymongo
import os
import numpy as np
import json

DATA_PATH = os.path.join('data','numbers')
JSON_PATH = os.path.join('JSON','numbers')
signs = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                    '11', '12', '13', '14', '15_v1', '15_v2', '16', '17', '18', '19', 
                    '20', '25_v1', '25_v2', '30', '40', '50', '60', '70', '80', '90',
                    '100', '200', '300', '400', '500', '600', '700', '800', '900',
                    '1000', '2000', '3000', 'MILLON',
                    'PRIMERO', 'SEGUNDO', 'TERCERO', 'CUARTO', 'QUINTO', 'SEXTO'])

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
def saveNumpy2json():
    action['categorie'] = 'number'
    for sign in signs:
        action['action'] = sign.lower()
        get_sequences(sign)
        with open(os.path.join(JSON_PATH,sign+'.json'),'w') as outfile:
            json.dump(action,outfile)
            print('Saved action "{}" to JSON.'.format(sign))