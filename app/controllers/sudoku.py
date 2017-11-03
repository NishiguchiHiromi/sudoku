#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from numpy import *

lst=a = [[[i for i in range(1,10)] for j in range(9)]for k in range(9)]

# QWidgetを継承(Escで閉じる)
class MyWidget(QWidget):
    # キーボードイベントをオーバーライド
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape: # キーがエスケープなら
            self.close() # 閉じる


app = QApplication(sys.argv)
window = MyWidget()
table = QTableWidget(9,9)
tableItem = QTableWidgetItem()
window.setWindowTitle("Sudoku")
window.resize( 470,450)
for a in range(9):
    table.setColumnWidth( a, 45 )


layout = QVBoxLayout()
button = QPushButton('Answer')
layout.addWidget(button)
layout.addWidget(table)
window.setLayout(layout)
lstlst=[]



def test():
    return "hey!"


def nyuryoku():
    global table
    global lst

    #打ち込んだ数をリストに保存
    for a in range(9):
        for b in range(9):
            try:
                lst[a][b]=[int(table.item (a, b).text())]
            except:
                pass

def kaiseki():
    global lst
    global lstlst
    import copy
    #c通りの可能性がc箇所あれば
    lstlst=copy.deepcopy(lst)
    for a in range(9):
        for b in range(9):
            z=lst[a][b]
            for c in range(1,4):
                if len(z) is c:
                    #横
                    if lst[a].count(z)==c:
                        for d in range(c):
                            for e in range(9):
                                if set(lst[a][e])!=set(z):
                                    try:
                                        lst[a][e].remove(z[d])
                                    except:
                                        pass

                    #縦
                    x=0
                    for g in range(9):
                        if lst[g][b]==z:
                            x+=1
                    if x==c:
                        for d in range(c):
                            for e in range(9):
                                if set(lst[e][b])!=set(z):
                                    try:
                                        lst[e][b].remove(z[d])
                                    except:
                                        pass

                    #四角
                    x=0
                    for g in range(3):
                        for h in range(3):
                            if lst[a-a%3+g][b-b%+3+h]==z:
                                x+=1
                    if x==c:
                        for d in range(c):
                            for e in range(3):
                                for f in range(3):
                                    if set(lst[a-a%3+e][b-b%+3+f])!=set(z):
                                        try:
                                            lst[a-a%3+e][b-b%+3+f].remove(z[d])
                                        except:
                                            pass





    #唯一探し
    #横
    for a in range(9):
        lstaa=[]
        for b in range(9):
            lstaa +=lst[a][b]

        for b in range(1,10):
            if lstaa.count(b)==1:
                for c in range(9):
                    if b in lst[a][c]:
                        lst[a][c]=[b]





    #縦
    for a in range(9):
        lstaa=[]
        for b in range(9):
            lstaa +=lst[b][a]
        for b in range(1,10):
            if lstaa.count(b)==1:
                for c in range(9):
                    if b in lst[c][a]:
                        lst[c][a]=[b]

    #四角
    for a in range(3):
        for b in range(3):
            for c in range(9):
                aa=[]
                bb=[]
                for d in range(3):
                    for e in range(3):
                        if c in lst[a*3+d][b*3+e]:
                            aa.append(a*3+d)
                            bb.append(b*3+e)
                if len(aa)==1:
                    lst[aa[0]][bb[0]]=[c]

                elif len(aa)==2:
                    if aa[0]==aa[1]:
                        for d in range(9):
                            try:
                                lst[aa[0]][d].remove(c)
                            except:
                                pass
                        lst[aa[0]][bb[0]].append(c)
                        lst[aa[0]][bb[0]].sort()
                        lst[aa[0]][bb[1]].append(c)
                        lst[aa[0]][bb[1]].sort()
                    if bb[0]==bb[1]:
                        for d in range(9):
                            try:
                                lst[d][bb[0]].remove(c)
                            except:
                                pass
                        lst[aa[0]][bb[0]].append(c)
                        lst[aa[0]][bb[0]].sort()
                        lst[aa[1]][bb[0]].append(c)
                        lst[aa[1]][bb[0]].sort()

                elif len(aa)==3:
                    if aa[0]==aa[1] and aa[1]==aa[2]:
                        for d in range(9):
                            try:
                                lst[aa[0]][d].remove(c)
                            except:
                                pass
                        lst[aa[0]][bb[0]].append(c)
                        lst[aa[0]][bb[1]].append(c)
                        lst[aa[0]][bb[2]].append(c)
                        lst[aa[0]][bb[0]].sort()
                        lst[aa[0]][bb[1]].sort()
                        lst[aa[0]][bb[2]].sort()
                    if bb[0]==bb[1] and bb[1]==bb[2]:
                        for d in range(9):
                            try:
                                lst[d][bb[0]].remove(c)
                            except:
                                pass
                        lst[aa[0]][bb[0]].append(c)
                        lst[aa[1]][bb[0]].append(c)
                        lst[aa[2]][bb[0]].append(c)
                        lst[aa[0]][bb[0]].sort()
                        lst[aa[1]][bb[0]].sort()
                        lst[aa[2]][bb[0]].sort()
    #X-wing
    for c in range(1,10):
        memo=[]
        for a in range(9):
            lstaa=[]
            lstbb=[]
            aa=0
            for b in range(9):
                lstaa+=lst[a][b]
            if lstaa.count(c)==2:
                lstbb.append(a)
                for b in range(9):
                    if c in lst[a][b]:
                        lstbb.append(b)
                memo.append(lstbb)
        if len(memo)==2 and memo[0][1]==memo[1][1] and memo[0][2]==memo[1][2]:

            for a in range(9):
                try:
                    lst[a][memo[0][1]].remove(c)
                except:
                    pass
                try:
                    lst[a][memo[0][2]].remove(c)
                except:
                    pass
            lst[memo[0][0]][memo[0][1]].append(c)
            lst[memo[0][0]][memo[0][2]].append(c)
            lst[memo[1][0]][memo[1][1]].append(c)
            lst[memo[1][0]][memo[1][2]].append(c)
            lst[memo[0][0]][memo[0][1]].sort()
            lst[memo[0][0]][memo[0][2]].sort()
            lst[memo[1][0]][memo[1][1]].sort()
            lst[memo[1][0]][memo[1][2]].sort()



    #仮想
def kasou():
    global lst
    global lstlst
    global muri
    import copy


    for a in range(9):
        for b in range(9):
            for zzz in range(len(lst[a][b])):
                OKflag=True
                lstlstvvv=copy.deepcopy(lst)
                lst[a][b]=[int(lst[a][b][zzz])]
                print(lst[a][b])
                print(a,b)
                lstlstone=copy.deepcopy(lst)
                print(lstlstone)
                print('bbb')
                kaiseki()
                print(lst)
                print('ccc')
                if lstlstone!=lst:
                    print('aaa')
                    while lstlst!=lst:
                        kaiseki()
                flag=True
                for c in range(9):
                    for d in range(9):
                        if len(lst[c][d])!=1:
                            flag=False
                            OKflag=False
                            lst=list(lstlstvvv)
                            break
                    if flag==False:
                        break
                if flag==True:
                    #kensho(縦横)
                    for c in range(9):
                        lstaa=[]
                        lstbb=[]
                        for d in range(9):
                            if len(lst[c][d])==1:
                                lstaa +=lst[c][d]
                            if len(lst[d][c])==1:
                                lstbb +=lst[d][c]

                        for e in range(1,10):
                            if lstaa.count(e)> 1 or lstbb.count(e)>1 :
                                lst=list(lstlstvvv)
                                OKflag=False
                                break
                        if OKflag==False:
                            break
                    if OKflag==True:
                        print('xxx')
                        for c in range(3):
                            for d in range(3):
                                lstaa=[]
                                for e in range(3):
                                    for f in range(3):
                                        if len(lst[c*3+e][d*3+f])==1:
                                            lstaa += lst[c*3+e][d*3+f]
                                for e in range(1,10):
                                    if lstaa.count(e)> 1:
                                        lst=list(lstlstvvv)
                                        OKflag=False
                                        break
                                if OKflag==False:
                                    break
                            if OKflag==False:
                                break


                else:
                    OKflag=False
                    lst=list(lstlstvvv)

                if OKflag==True:
                    break
            if OKflag==True:
                print('ddd')
                break
        if OKflag==True:
            break










def syutsuryoku():


    #出力
    print(lst)
    print('sss')
    for a in range(9):
        for b in range(9):
            if len(lst[a][b]) is 1:
                table.setItem(a,b, QTableWidgetItem(str(lst[a][b][0])))

def answer():
    global flag
    global muri
    global lstlst

    nyuryoku()

    while lstlst!=lst:
        kaiseki()

    flag=True
    for a in range(9):
        for b in range(9):
            if len(lst[a][b])!=1:
                flag=False
                break
        if flag==False:
            break
    if flag==False:
        kasou()

    syutsuryoku()



button.clicked.connect(answer)

window.show()
sys.exit(app.exec_())




'''
def main():
    global app
    global window
    global table
    global tableItem
    window.setWindowTitle("Sudoku")
    window.resize( 470,450)
    for a in range(9):
        table.setColumnWidth( a, 45 )

    layout = QVBoxLayout()
    button = QPushButton('Answer')

    global answer
    button.clicked.connect(answer)

    layout.addWidget(button)
    layout.addWidget(table)
    window.setLayout(layout)

    window.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
'''
