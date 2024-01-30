import os
import pyautogui
import random

dies = 0

PlayerHP = 20
NcpHP = 20
restarLOG= 0

while dies != 5:
    if restarLOG == 1:
        PlayerHP = 20
        NcpHP = 20
        restarLOG= 0
    playerMove = pyautogui.confirm(text="-Выбери действие-",title="FUNNY_game",buttons=["Атака","Защита"])
    
    if playerMove == "Атака":
        AttakLuky = random.randint(1,6)
        
        if AttakLuky == 1:
            PlayerHP-=5
        elif AttakLuky == 3 or AttakLuky == 2:
            PlayerHP-=3
        elif AttakLuky == 4 or AttakLuky == 5:
            NcpHP-=3
        elif AttakLuky == 6:
            NcpHP-=5

        if PlayerHP < 1:
            print("[}._Вы проиграли_.{]")
            dies+=1
            restarLOG = 1
            f = open('statistik.txt', 'a', encoding="utf-8")
            f.write("\nПорожение")
            f.close()
            
        elif NcpHP < 1:
            print(":)(:_Победа_:)(:")
            restarLOG = 1
            f = open('statistik.txt', 'a', encoding="utf-8")
            f.write("\nПобеда")
            f.close()
            
        else:
            print("Ваше здоровье - "+str(PlayerHP))
            print("Здаровье врага - "+str(NcpHP))

    elif playerMove == "Защита":
        SaveLuky = random.randint(1,6)
        if SaveLuky == 1:
            PlayerHP-=2
        elif SaveLuky == 3 or SaveLuky == 2:
            pass
        elif SaveLuky == 4 or SaveLuky == 5:
            PlayerHP+=1
            if PlayerHP > 20:
                PlayerHP=20
        elif SaveLuky == 6:
            PlayerHP+=5
            if PlayerHP > 20:
                PlayerHP=20
        if PlayerHP < 1:
            print("[}._Вы проиграли_.{]")
            dies+=1
            restarLOG = 1
            f = open('statistik.txt', 'a', encoding="utf-8")
            f.write("\nПорожение")
            f.close()
            
        elif  NcpHP < 1:
            print(":)(:_Победа_:)(:")
            restarLOG = 1
            f = open('statistik.txt', 'a', encoding="utf-8")
            f.write("\nПобеда")
            f.close()
            
        else:
            print("Ваше здоровье - "+str(PlayerHP))
            print("Здаровье врага - "+str(NcpHP))
  
Print("Игра окончена")
f = open('statistik.txt', 'a', encoding="utf-8")
f.write("\nПроиграная игра")
f.close()




