# coding: utf-8

import sqlite3


conn = sqlite3.connect("c:/users/liuyong/desktop/PipeDiameter.db")
print("Connected Success!")
c = conn.cursor()
try:
    c.execute('''
        CREATE TABLE Elbow
        (NAME TEXT,
        DN TEXT,
        D TEXT,
        WT TEXT,
        WEIGHT TEXT,
        PAGE TEXT);''')

    print("Elbow Create Success!")
    conn.commit();
except:
    print("Elbow is Existed!")
finally:
    with open(input("请输入数据所在txt文件路径:"), "rb") as f:
        for eachline in f.readlines():
            linecontent = eachline.split(b"\t")
            c.execute('INSERT INTO Elbow (NAME,DN,D,WT,WEIGHT,PAGE) VALUES (?,?,?,?,?,?)',(linecontent[0].strip(b"\t\n").decode(), linecontent[1].strip(b"\t\n").decode(), linecontent[2].strip(b"\t\n").decode(), linecontent[3].strip(b"\t\n").decode(), linecontent[4].strip(b"\t\n").decode(), linecontent[5].strip(b"\t\n").decode()))
            print("Insert Success!")
            conn.commit();
conn.close();
