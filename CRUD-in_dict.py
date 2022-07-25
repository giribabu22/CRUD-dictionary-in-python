print('welcome to school !!!')
d={'prem': {'email': 'prem@gmail.com', 'rollno': '33', 'age': '23', 'phoneNumder': '3222222222'},'giri': {'email': 'prem@gmail.com', 'rollno': '33', 'age': '23', 'phoneNumder': '3222222222'}}
ask=['email','rollno','age','phonenum']
while True:
    print('''    1) Creat
    2) Read 
    3) Update
    4) Delete
press 8 to getout (_)\n''')
    c= int(input('enter the choice :'))
    if c ==1:
        x=0
        n= input('enter the name :')
        if n not in d:
            d2={}
            while  x <len(ask):
                print('enter the ',ask[x])
                res=input('~~~~~~~~~~~~~~~~:')
                d2[ask[x]]=res
                if ask[x] =='email':
                    fp=res[-10:]
                    if  fp == '@gmail.com':
                        d2[ask[x]]=res
                    else:
                        del d2[ask[x]]
                        print('you enter wrong gmail',d)
                        break
                x+=1
                if len(d2)==1:pass
                else:d[n]=d2
            print(d)
        else:
            print('\n >>> this name is avalable ',n,d[n],'\n')
            pass
    elif c ==2:
        while True:
            stu= input('enter the name :')
            if stu in d.keys():
                print(stu,d[stu],'\n~~~~~~~~~~~~~~~~~~~~~~~')
                break
            else:
                print('\n >>>>this name is not in the data \n')
                pass
    elif c ==3:
        ma=input('which student data you will Update  :')
        if len(d)!=0:
            for k,v in d.items():
                if ma !=k:print(k)
                elif ma==k:           
                    li=list(k1 for k1 in d.keys())
                    if ma in d:
                        dh5=input('if you want to update the name y/n :')
                        if dh5 =='y':                       
                            name2=input('enter your changing name :')
                            if name2 in li:
                                print('this name is avalable')
                                continue
                            else:
                                print(k)
                                del d[k]
                                d[name2]=v
                                print(d)
                                break
                        elif ma in li:
                            li4=list(h for h in v)
                            print(li4)
                            da=input('enter what you want to Update :')
                            if da in v.keys():
                                l6=list(r for r in v.keys())
                                q=1
                                print('enter the ',da)
                                res=input('~~~~~~~~~~~~~~~~:')
                                if da =='email':
                                    fp=res[-10:]
                                    if  fp == '@gmail.com':
                                        v[da]=res
                                        d[ma]=v
                                        print('update successfully !!\n',d[ma])

                                    else:
                                        print('\n>>>> wrong gmail \n')
                                else:
                                    v[da]=res
                                    d[ma]=v
                                    print(d)
                                    print('update successfully !!\n',d[ma])
                        
                    else:
                        print("\n>>> this name is avalable ",ma,"\n")
                        pass
        else:print('\n>>>empty data add some data',"\n")   
    elif c ==4:
        l5=list(k for k in d.keys())
        while True:
            print("enter this name's only",l5)
            e=input('enter the student name to Delete data :')
            if e not in d.keys():
                print('this name "not" in the records #\n~~~~~~~~~~~~~~~~~~~~~~~',e)
                pass  
            else:
                del d[e]
                print('\n>>>  Deleted successfully !!!\n')
                break
    else:
        print('<<<<<<<<< Come again >>>>>>>>>>')
        break