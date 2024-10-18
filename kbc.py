qestions= [
    [
        "which language was used to create fb?","python","none","php","javascript","d"
    ],
    [
        "india prime minister name?","modi","rahul","sagar","nirbhay","a"
    ],
    [
        "surat kesa city he","smart","cleane","green","none","a"
    ],
    [
        "apdi company kevi che?","Gosod","v.Good","Bed","none","c"
    ],
]

levels=[1000,2000,3000,5000,10000,20000,40000,50000,100000,500000]

for i in range(0,len(qestions)):
    qestion=qestions[i]
    print(f"Qestions for rs.{levels[i]} is {qestions[i][0]}")
    print(f"a.{qestions[i][1]}   b.{qestions[i][2]}")
    print(f"c.{qestions[i][3]}   d.{qestions[i][4]}")
    reply=str(input("Enter your amswer:- "))
    if (reply == qestions[i][5]):
        print(f"correct answer , you have win rs.{levels[i]}")
    else:
        print("wrong answer!")
        break