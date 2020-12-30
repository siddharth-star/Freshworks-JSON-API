#======== Library Import ==========#
import os
import json
import datetime
#==========Path Find============#
def findPath():
    i=1
    path=''
    while i:
        filepath=input("Choose option for file path\n1.Default Path\n2.User Define Path\n -> ")
        if filepath=='1':
            i=0
            path=("userDetails.json")
            try:
                with open(path) as f:
                    pass
            except:
                with open(path,'w') as f:
                    temp={"person":[]}
                    json.dump(temp,f,indent=2)
        elif filepath=='2':
            i=0
            givenpath=input('Enter the path in this formate : --/--/--\n')
            path= os.path.join(givenpath, 'userDetails.json')
            try:
                with open(path) as f:
                    pass
            except:
                with open(path,'w') as f:
                    temp={"person":[]}
                    json.dump(temp,f,indent=2)
        else:
            print("Please enter a valid input\n------------")
    
    return path
#------------Read Funtion------------#
def read(path,_id):
    
    with open(path) as f:
            data = json.load(f)
    h=0
    temp="================\nKey does not exist\n=================="
    for i in data['person']:
            if i['_id']!=_id:
                pass
            else:
                h=1
                curr=int(datetime.datetime.now().timestamp())
                if curr>=(int(i['life_time'])+int(i['time_build'])):
                    delete(path,_id)
                else:
                    temp=json.dumps(i,indent=2,sort_keys=True)
                    print(temp)
    if h==0: 
        print(temp)
                    
#------------Delete Funtion------------#
def delete(path,item):
        with open(path) as f:
            data = json.load(f)
        
        temp={"person":[]}
        for i in data['person']:
            if i['_id']==item:
                curr=int(datetime.datetime.now().timestamp())
                if curr>int(i['life_time'])+int(i['time_build']):
                    print('================\nThis Key does not exist due to Time Stamp\n===============')
            else:
                temp['person'].append(i)
        with open(path,'w') as f:
                json.dump(temp,f,indent=2)
#------------Read All Data------------#
def readall(path):
    with open('userDetails.json') as f:
        data = json.load(f)
    for i in data['person']:
        read(path,i['_id'])
    # read=json.dumps(data,indent=2,sort_keys=True)
    # print(read)
#------------Create Funtion------------#
def create(path):
        check_key=1
        while check_key:
            check_key=0
            with open(path) as f:
                data =json.load(f)
            
            with open(path) as f:
                data =json.load(f)
                temp=data['person']
                _id=input('Enter the id : ')
                if len(_id)>32:
                    print("========\nEnter a key under 32 character\n========")
                    check_key=1
                    continue
                #=========
                f=0
                for i in data['person']:
                    if i['_id']==_id:
                        print("=========\nThis id already exists\n========")
                        f=1
                        check_key=1
                if f==1:
                    continue
                #=========
                citizen=input("Enter the life time of request : ")
                name=input("Enter Name : ")
                query=str(int(datetime.datetime.now().timestamp()))
                y={"_id":_id,"name":name,"life_time":citizen,"time_build":query}
                temp.append(y)
            if check_key==0:
                with open(path,'w') as f:
                    json.dump(data,f,indent=2)

#=================== Choice Operation ==================
path=findPath()
while True:
    oper=input("Choose option for operation\n1.Create data\n2.Delete data\n3.Read data \n4.Read All\n5.Exit \n-> ")
    if oper=='5':
        break
    elif oper=='1':
        create(path)        
    elif oper=='2':
        item=input("Enter the id which you want to delete : ")
        delete(path,item)            
    elif oper=='3':
        _id=input("Enter the key which you want to read : ")
        read(path,_id)
    elif oper=='4':
        readall(path)
    else:
        print("------------\nPlease enter a valid input\n------------")