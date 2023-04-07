# Uploading data to mongoDB
import pymongo
from pymongo import MongoClient
import os
import numpy as np

# cluster = MongoClient('mongodb+srv://root:<password>@routectijuana.aziov99.mongodb.net/?retryWrites=true&w=majority')
# db = cluster['SignAI']
# collection = db['signs']

DATA_PATH = os.path.join('data','ABC')
signs = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 
                    'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

def get_frames(sign, sequence_num):
    for frame in range(30):
        array = np.load(os.path.join(DATA_PATH,sign,str(sequence_num),str(frame)+'.npy'))
        if frame == 0:
            frames_collection = array
        else:
            frames_collection = np.vstack((frames_collection,array))
    print(frames_collection.shape)
    return frames_collection

def get_sequences(sign):
    for sequence in range(30):
        frames = get_frames(sign, sequence)
        if sequence == 0:
            sequence_collection = frames
        else:
            sequence_collection = np.vstack((sequence_collection,frames))
    return sequence_collection


for sign in signs:
    print(sign)
    videos = get_sequences(sign)

