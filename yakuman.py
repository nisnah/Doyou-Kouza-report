import sys
import random

#上がられたとき
def fin():
    print("お疲れさまでした。")
    sys.exit()

#牌の操作
def haisousa(hai,handan):
    global judge
    if hai[1]=='m':
        if 0<int(hai[0]) and int(hai[0])<=9:
            if handan=="yes":
                manzu[int(hai[0])-1]+=1
            nokorimanzu[int(hai[0])-1]=nokorimanzu[int(hai[0])-1]-1
        else:
            print("入力方法が違います。")
            judge=1
    elif hai[1]=='p':
        if 0<int(hai[0]) and int(hai[0])<=9:
            if handan=="yes":
                pinzu[int(hai[0])-1]+=1
            nokoripinzu[int(hai[0])-1]=nokoripinzu[int(hai[0])-1]-1
        else:
            print("入力方法が違います。")
            judge=1
    elif hai[1]=='s':
        if 0<int(hai[0]) and int(hai[0])<=9:
            if handan=="yes":
                souzu[int(hai[0])-1]+=1
            nokorisouzu[int(hai[0])-1]=nokorisouzu[int(hai[0])-1]-1
        else:
            print("入力方法が違います。")
            judge=1
    elif hai[1]=='j':
        if 0<int(hai[0]) and int(hai[0])<=7:
            if handan=="yes":
                jihai[int(hai[0])-1]+=1
            nokorijihai[int(hai[0])-1]=nokorijihai[int(hai[0])-1]-1
        else:
            print("入力方法が違います。")
            judge=1
    else:
        print("入力方法が違います。")
        judge=1
    return judge

def yakuman():
    suteruhai=""
    if target=="k":
        suteruhai=kokusi()
    elif target=="ty":
        suteruhai=tyuren()
    elif target=="tu":
        suteruhai=tuiso()
    return suteruhai

def kokusi():
    sutekouho=[]
    tobidasi=0
    suteyao=[]
    for k in range(7):
        if manzu[k+1]>0:
            sutekouho.append(str(k+2)+"m")
        if pinzu[k+1]>0:
            sutekouho.append(str(k+2)+"p")
        if souzu[k+1]>0:
            sutekouho.append(str(k+2)+"s")
    for k in range(7):
        if jihai[k+1]>1:
            tobidasi=tobidasi+jihai[k+1]-1
            suteyao.append(str(k+1)+"j")
    for k in range(2):
        if manzu[k*8]>1:
            tobidas=tobidasi+manzu[k*8]-1
            suteyao.append(str(k*8+1)+"m")
        if souzu[k*8]>1:
            tobidas=tobidasi+souzu[k*8]-1
            suteyao.append(str(k*8+1)+"s")
        if pinzu[k*8]>1:
            tobidas=tobidasi+pinzu[k*8]-1
            suteyao.append(str(k*8+1)+"p")
    if len(suteyao)>1:
        sutekouho=sutekouho+suteyao
    return sutekouho[random.randint(0,len(sutekouho)-1)]
    
def tyuren():
    sutekouho=[]
    sutekamo=[]
    tobidasi=0
    neraime=input("なにで九蓮宝燈を狙いますか？(\'m\'or\'p\'or\'s\')")
    if neraime!="m":
        for k in range(9):
            if manzu[k]>0:
                sutekouho.append(str(k+1)+"m")
    if neraime!="p":
        for k in range(9):
            if pinzu[k]>0:
                sutekouho.append(str(k+1)+"p")
    if neraime!="s":
        for k in range(9):
            if souzu[k]>0:
                sutekouho.append(str(k+1)+"s")
    for k in range(7):
        if jihai[k]>0:
            sutekouho.append(str(k+1)+"j")
    if neraime=="m":
        for k in range(7):
            if manzu[k+1]>1:
                tobidasi=tobidasi+manzu[k+1]-1
                sutekamo.append(str(k+2)+"m")
        for k in range(2):
            if manzu[k*8]>3:
                tobidasi=tobidasi+manzu[k*8]-3
                sutekamo.append(str(k*8+1)+"m")
    if neraime=="p":
        for k in range(7):
            if pinzu[k+1]>1:
                tobidasi=tobidasi+pinzu[k+1]-1
                sutekamo.append(str(k+2)+"p")
        for k in range(2):
            if pinzu[k*8]>3:
                tobidasi=tobidasi+pinzu[k*8]-3
                sutekamo.append(str(k*8+1)+"p")
    if neraime=="s":
        for k in range(7):
            if souzu[k+1]>1:
                tobidasi=tobidasi+souzu[k+1]-1
                sutekamo.append(str(s+2)+"s")
        for k in range(2):
            if souzu[k*8]>3:
                tobidasi=tobidasi+souzu[k+1]-1
                sutekamo.append(str(k*8+1)+"s")
    if tobidasi>1:
        sutekouho=sutekouho+sutekamo
    return sutekouho[random.randint(0,len(sutekouho)-1)]
        
def tuiso():
    sutekouho=[]
    for k in range(9):
        if manzu[k]>0:
            sutekouho.append(str(k+1)+"m")
        if pinzu[k]>0:
            sutekouho.append(str(k+1)+"p")
        if souzu[k]>0:
            sutekouho.append(str(k+1)+"s")
    for k in range(7):
        if jihai[k]==1 and nokorijihai[k]==0:
            return str(k+1)+"j"
    if len(sutekouho)>0:
        return sutekouho[random.randint(0,len(sutekouho)-1)]
    else:
        for k in range(7):
            if jihai[k]==2 and nokorijihai[k]==0:
                return str(k+1)+"j"
        for k in range(7):
            if jihai[k]==1:
                return str(k+1)+"j"
        for k in range(7):
            if jihai[k]==2:
                return str(k+1)+"j"

def suteru(hai):
    if hai[1]=='m':
        if 0<int(hai[0]) and int(hai[0])<=9:
            manzu[int(hai[0])-1]=manzu[int(hai[0])-1]-1
    elif hai[1]=='p':
        if 0<int(hai[0]) and int(hai[0])<=9:
            pinzu[int(hai[0])-1]=pinzu[int(hai[0])-1]-1
    elif hai[1]=='s':
        if 0<int(hai[0]) and int(hai[0])<=9:
            souzu[int(hai[0])-1]=souzu[int(hai[0])-1]-1
    elif hai[1]=='j':
        if 0<int(hai[0]) and int(hai[0])<=7:
            jihai[int(hai[0])-1]=jihai[int(hai[0])-1]-1

manzu=[0,0,0,0,0,0,0,0,0]#自分の持ち萬子
pinzu=[0,0,0,0,0,0,0,0,0]#自分の持ちピンズ
souzu=[0,0,0,0,0,0,0,0,0]#自分の持ちそうず
jihai=[0,0,0,0,0,0,0]#自分の持ち字牌

nokorimanzu=[4,4,4,4,4,4,4,4,4]#見えていない萬子
nokoripinzu=[4,4,4,4,4,4,4,4,4]#見えていないピンズ
nokorisouzu=[4,4,4,4,4,4,4,4,4]#見えていないそうず
nokorijihai=[4,4,4,4,4,4,4]#見えていない字牌

me=int(input("\'1\'or\'2\'or\'3\'or\'4\'(東家=1,南家=2,西家=3,北家=4):"))
if int(me)<1 or 4<int(me):
    print("間違った入力です")
    sys.exit()
judge=0#ミス判断

j=0
while j<1:
    syodora=input("ドラを入力してください。(萬子=〇m,筒子=〇p,索子=〇s,字牌=〇j(東南西北白發中=1~7)):")
    judge=0
    judge=haisousa(syodora,"no")
    if judge==0:
        j+=1

i=0
while i <13:
    myhai = input(str(i+1) +"個目の牌を入力してください。(萬子=〇m,筒子=〇p,索子=〇s,字牌=〇j(東南西北白發中=1~7)):")
    judge=0
    judge=haisousa(myhai,"yes")
    if judge==1:
        continue
    i+=1

#print(me)
#print(manzu)
#print(pinzu)
#print(souzu)
#print(jihai)
#print(nokorimanzu)
#print(nokoripinzu)
#print(nokorisouzu)
#print(nokorijihai)

now=0
me=int(me)-1

n=0
while n<1:
    target=input("何の役満を狙いますか？(k(国士無双),ty(九蓮宝燈),tu(字一色):")
    if target=="k" or target=="ty" or target=="tu":
        n=n+1
    else:
        print("間違った入力です。")

while 0<1:
    if now!=me:
        te=input("\'s(捨て)\'or\'a(上がり)\'or\'kk(加槓)\'or\'dmk(大明槓)\'or\'r(流局)\':")
        if te=="s":
            sutehai=input("捨て牌を入力してください。:")
            if target=="tu":
                for i in range(7):
                    if str(i+1)+"j"==sutehai:
                        if jihai[i]>=2:
                            print("カン、またはポン、もしくはロンしてください。")
            dounaru=input("\'mr(自家のロン)\'or\'tr(他家のロン)\'or\'mp(自分のポン)\'or\'mk(自分のカン)\'or\'p(ポン)\'or\'t(チー)\'or\'ak(暗槓)\'or\'n(何もない)\':")
            if dounaru=="mr":
                fin()
            elif dounaru=="tr":
                fin()
            elif dounaru=="mp":
                now=me
            elif dounaru=="mk":
                haisousa(sutehai,"yes")
                now=me
            elif dounaru=="p":
                for i in range(3):
                    haisousa(sutehai,"no")
                ponh=input("だれがポンをしましたか？(1,2,3,4=東,南,西,北):")
                now=int(ponh)-1
            elif dounaru=="t":
                syotihai=input("チー牌の中で一番小さいものを入力してください。:")
                for i in range(3):
                    tihai=syotihai[0]+str(int(syotihai[1])+i)
                    haisousa(tihai,"no")
                now=(now+1)%4
            elif dounaru=="ak":
                for i in range(4):
                    haisousa(sutehai,"no")
                akh=input("だれがカンをしましたか？(1,2,3,4=東,南,西,北):")
                now=int(akh)-1
                nd=input("新しいドラを入力してください。:")
                haisousa(nd,"no")
            elif dounaru=="n":
                haisousa(sutehai,"no")
                now=(now+1)%4
            else:
                print("間違った入力です。")
        elif te=="a":
            fin()
        elif te=="kk":
            kkhai=input("カン牌を入力してください。:")
            tyankan=input("槍槓ですか？\'y\'or\'n\':")
            if tyankan=="y":
                fin()
            else:
                for s in range(4):
                    haisousa(kkhai,"no")
                nd=input("新しいドラを入力してください。:")
                haisousa(nd,"no")
                continue
        elif te=="dmk":
            dmkhai=input("カン牌を入力してください。:")
            for s in range(4):
                haisousa(dmkhai,"no")
            nd=input("新しいドラを入力してください。:")
            haisousa(nd,"no")
            continue
        elif te=="rk":
            print("流局です。")
            sys.exit()
        else:
            print("間違った入力です。")
            continue
    else:
        tumohai=input("自摸牌またはポンもしくはロンした牌を入力してください。:")
        agari=input("上がりですか？\'y\'or\'n\'")
        if agari=="y":
            fin()
        if target=="tu":
            print("字牌でカンできる場合はカンしてください。")
        haisousa(tumohai,"yes")
        sutehai=yakuman()
        print(sutehai + "を捨ててください。")
        suteru(sutehai)
        dounaru=input("\'tr(他家のロン)\'or\'p(ポン)\'or\'t(チー)\'or\'ak(暗槓)\'or\'n(何もない)\'or\'rk(流局):")
        if dounaru=="tr":
            fin()
        elif dounaru=="rk":
            print("流局です。")
            sys.exit()
        elif dounaru=="p":
            for s in range(3):
                haisousa(sutehai,"no")
            ponh=input("だれがポンをしましたか？(1,2,3,4=東,南,西,北):")
            now=int(ponh)-1
        elif dounaru=="t":
            syotihai=input("チー牌の中で一番小さいものを入力してください。:")
            for s in range(3):
                tihai=syotihai[0]+str(int(syotihai[1])+i)
                haisousa(tihai,"no")
                now=(now+1)%4
        elif dounaru=="ak":
            for s in range(4):
                haisousa(sutehai,"no")
            akh=input("だれがカンをしましたか？(1,2,3,4=東,南,西,北):")
            now=int(akh)-1
        elif dounaru=="n":
            haisousa(sutehai,"no")
            now=(now+1)%4
        else:
            print("間違った入力です。")
            continue
