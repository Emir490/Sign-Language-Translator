from pymongo import MongoClient
import json
from bson import json_util
import os
import sys
import numpy as np

# Set up a connection to the MongoDB server
client = MongoClient('mongodb+srv://root:gachiin@routectijuana.aziov99.mongodb.net/SignAI')

# Select the database and collection that contains the data
db = client['SignAI']
collection = db['actions']

ACTION_LIST = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
JSON_PATH = os.path.join('JSON')
DATA_PATH = os.path.join('data')
MONGO_FIELDS = { '_id':0, 'action':1, 'sequence':1, 'keypoints':1}

# Save action to json file
# record=json string    action=filename
def save2json(record):
    action = record['action']
    sequence = record['sequence']
    file_path = os.path.join(JSON_PATH,action,'{}.json'.format(sequence))
    with open( file_path,'w') as file:
        json_data = json.dumps(record, indent=3, default=json_util.default)
        file.write(json_data)
        file.close()
    print('Saved sequence [{}] to json.'.format(sequence))

# Gets all the documents from MongoDB
def getMongoData(actions):
    for action in actions:
        dir = os.path.join(JSON_PATH,action)
        try:
            os.makedirs(dir)
        except(FileExistsError):
            pass
        for i in range(1,31):
            query = { 'sequence':'{}-{}'.format(action,i) }
            record = collection.find_one(query,MONGO_FIELDS)
            if record is not None: save2json(record)
            else: pass

# Converts the JSON files to numpy arrays
def json2numpy(actions):
    for action in actions:
        for i in range(30):
            sequence = i + 30
            dir = os.path.join(DATA_PATH,'ABC',action,str(sequence))
            try:
                os.mkdir(dir)
            except(FileExistsError):
                pass
            filePath = os.path.join(JSON_PATH,action,'{}-{}.json'.format(action,i+1))
            f = open( filePath, 'r')
            data = json.load(f)
            frames = data['keypoints']
            frame_count = 0
            f.close()
            for frame in frames:
                pose = np.array(frame['pose'])
                face = np.array(frame['face'])
                lh = np.array(frame['leftHand'])
                rh = np.array(frame['rightHand'])
                keypoints = np.concatenate([pose, face, lh, rh])
                print('Sequence {}, frame {}, size {}.'.format(data['sequence'],frame_count,keypoints.size))
                npy_path = os.path.join(dir,str(frame_count))
                np.save(npy_path,keypoints)
                frame_count += 1

def main():
    try:
        os.mkdir(JSON_PATH)
    except(FileExistsError):
        pass
    finally:
        # getMongoData(ACTION_LIST)
        getMongoData(['A','B','C'])
    # json2numpy(ACTION_LIST)
    json2numpy(['A','B','C'])


if __name__ == '__main__':
    main()
