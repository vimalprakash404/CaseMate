import json

def insert():
    f = open('data.json')
    data = json.load(f)
    for i in data['states']:
        print(i["state"])
        print("_________")
        for j in i["districts"]:
            print(j)
    f.close()

insert()