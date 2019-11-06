from json import dump,load
import os



def GetTable(tablename):
    
    with open("Table\\"+tablename,'r',encoding='utf-8') as json_file:
        return load(json_file)
def load_all(path):
    table_asset={}
    for f in os.listdir(path):
        if os.path.splitext(f)[1]=='.json':
            table_asset[os.path.splitext(f)[0]]=GetTable(f)
    return table_asset
