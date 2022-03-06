import json, unittest, datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)



def convertFromFormat2 (jsonObject):
    jsonObject['deviceID']=jsonObject['device']['id']
    jsonObject['deviceType']=jsonObject['device']['type']
    l_index = ['country','city','area','factory','section']
    l_dict = {}
    for item in l_index:
      l_dict[item]=jsonObject[item]
    jsonObject['location'] =l_dict
    time_str = jsonObject['timestamp']
    dat = datetime.datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    jsonObject['timestamp'] = int(str((dat - datetime.datetime(1970, 1, 1)).total_seconds()*1000)[:-2])
    [jsonObject.pop(key) for key in ['device','country','city','area','factory','section',]]
    return jsonObject

def convertFromFormat1 (jsonObject):
    l_index = ['country','city','area','factory','section']
    l_str = jsonObject['location']
    l_value = l_str.split('/')
    new_loc = dict(zip(l_index,l_value))
    jsonObject['location'] = new_loc
    jsonObject['data'] = {'status':jsonObject['operationStatus'],
    'temprature':jsonObject['temp']
    }
    [jsonObject.pop(key) for key in ['operationStatus','temp']]
    
    return jsonObject 

x = convertFromFormat2(jsonData2)
print(x)

#y = convertFromFormat1(jsonData1)
