#amra ekhon json ke dictonary te convert korbo and dictonary ke json e 

import json


#python to json convertion: (serialization)
data = {
    'name' : "Tarek",
    'age' : 23,
    'is_logged_in' : True,
    'test' : None
}

json_string = json.dumps(data,indent=4)
print(json_string) 
print(type(json_string)) #amra dict ---> string e convert korlam thats mean python theke json e


# ---------------------------------------------


#json to python convertion: (De-serialization)
data = '{"name" : "Tarek","age" : 23,"is_logged_in" : true}'

python_dict = json.loads(data)
print(python_dict)
print(type(python_dict))