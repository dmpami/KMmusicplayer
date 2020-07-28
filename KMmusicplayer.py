# beta 02 ///
from ftplib import FTP
import ftplib
import time
from time import sleep
from datetime import datetime
import os
from playsound import playsound
import random


directory_music = 'music/'
directory_ad = 'ad/'

def track_update():
    global Error_code_1
    Error_code_1 = 999
    try:
        os.remove("files_list.txt")
    except:
        pass

        #Соединяемся с FTP-сервером
    #после чего каждую переменную подключим к авторизации:
    ftp = FTP()
    HOST = '****************'
    PORT = 21
    login = '****************'
    password = '****************'
    ftp.connect(HOST, PORT)
    ftp.login(login,password)
    directory = ftp.cwd('music') # Меняем директорию
    ftp.encoding = 'cp1251' # Windows-1251
    sub_directory_list = ftp.nlst() #Получаем список файлов в папке
    def track_download():
        global Error_code_1
        if len(sub_directory_list) == 0:
            print (" На сервере нихрена нет!! Это странно")
            Error_code_1 = 0
        elif len(sub_directory_list) != 0:
            local_files = os.listdir(directory_music )

            result = list(set(sub_directory_list) - set(local_files))

            if len(result) == 0:
                print ("\nНовых  музыкальных файлов на сервере нет!! Обновлять нечего, слушаем то что есть! ")
                Error_code_1 = 1

            elif len(result) > 0:
                print ("\nНа компе не хватает файлов музыки")
                print (result)
                print('Длина списка')
                print(len(result))

                len_sub_directory_list = len(result)

                global i
                i = 0
                while i < len_sub_directory_list:
                    #print ( "i= " + str(i))
                    try:
                        remained = len_sub_directory_list - i
                        print (" Осталось загрузить музыкальных треков: " + str(remained))
                        str_sub_directory_list = ''.join(result[i])
                        print ("  *** Загрузка " + str_sub_directory_list)
                        f = open("music/" + str_sub_directory_list,"wb")
                        ftp.encoding = 'cp1251'
                        ftp.retrbinary("RETR " + result[i],f.write)
                        f.close()
                        #log_track = open("files_list.txt", 'a', encoding='utf8')
                        #log_track.write(str_sub_directory_list  + '\n')
                    except:
                        print("Ошибка")
                        pass
                    i += 1
                print ("\n  Успешно!") # Хуешно, проверки нет!
                Error_code_1 = 10
    track_download()
    def track_dell():
        global Error_code_2
        Error_code_2 = 999
        local_files = os.listdir(directory_music)
        del_result = list(set(local_files) - set(sub_directory_list))
        global y
        y = 0
        while y < len(del_result):
            str_del_result = ''.join(del_result[y])
            os.remove(directory_music + str_del_result)
            print ( "-Удалил с компьютера " + str_del_result)
            y += 1
        Error_code_2 = 20
        try:
            os.remove(directory_music + "renamer.py")
            print ( "-Удалил с компьютера renamer.py")
        except:
            pass
    track_dell()
    def ad_download():
        directory = ftp.cwd('..') # Меняем директорию
        directory = ftp.cwd('ad') 
        ftp.encoding = 'cp1251' # Windows-1251
        global ad_sub_directory_list
        ad_sub_directory_list = ftp.nlst() #Получаем список файлов в папке
        global Error_code_3
        if len(ad_sub_directory_list) == 0:
            print (" На сервере нихрена нет!! Это странно")
            Error_code_3 = 0
        elif len(ad_sub_directory_list) != 0:
            local_files = os.listdir(directory_ad )

            result = list(set(ad_sub_directory_list) - set(local_files))

            if len(result) == 0:
                print ("\n Новых файлов рекламы на сервере нет!! Обновлять нечего, слушаем то что есть! ")
                Error_code_3 = 1

            elif len(result) > 0:
                print ("\n На компе не хватает файлов рекламы")
                print (result)
                print(' Длина списка')
                print(len(result))

                len_sub_directory_list = len(result)




                global i
                i = 0
                while i < len_sub_directory_list:
                    #print ( "i= " + str(i))
                    try:
                        remained = len_sub_directory_list - i
                        print (" Осталось загрузить рекламных треков: " + str(remained))
                        str_sub_directory_list = ''.join(result[i])
                        print ("  *** Загрузка " + str_sub_directory_list)
                        f = open("ad/" + str_sub_directory_list,"wb")
                        ftp.encoding = 'cp1251'
                        ftp.retrbinary("RETR " + result[i],f.write)
                        f.close()
                        #log_track = open("files_list.txt", 'a', encoding='utf8')
                        #log_track.write(str_sub_directory_list  + '\n')
                    except:
                        print("Ошибка")
                        pass
                    i += 1
                print ("\n  Успешно!") # Хуешно, проверки нет!
                Error_code_3 = 10
    ad_download()
    def track_dell():
        global Error_code_4
        Error_code_4 = 999
        local_files = os.listdir(directory_ad)   
        del_result = list(set(local_files) - set(ad_sub_directory_list))
        global y
        y = 0
        while y < len(del_result):
            str_del_result = ''.join(del_result[y])
            os.remove(directory_ad + str_del_result)
            print ( "-Удалил с компьютера " + str_del_result)
            y += 1
        Error_code_4 = 20
        try:
            os.remove(directory_ad + "renamer.py")
            print ( "-Удалил с компьютера renamer.py")
        except:
            pass
    track_dell()



def files_list():
    try:
        os.remove("files_list.txt")
    except:
        pass
    files_music = os.listdir(directory_music)
    for track_name in files_music:
        log_track = open("files_list.txt", 'a', encoding='utf8')
        log_track.write(track_name  + '\n')
        print (track_name)

def play_m(Track):
    playsound("music/" + Track)
def play_a(Track):
    playsound("ad/" + Track)

def music_ad_play():
    global files_music
    files_music = os.listdir(directory_music) # Строим список музыки
    random.shuffle(files_music) # Перемешиваем
    files_ad = os.listdir(directory_ad)  # Строим список рекламы
    random.shuffle(files_ad)  # Перемешиваем
    global Al 
    global Bl
    Al = len(files_music)  # Длина списка музыки
    Bl = len(files_ad)  # Длина списка рекламы
    #print ("##debug Al") #debug
    #print (Al)   #debug
    #print ("##debug Bl") #debug
    #print (Bl)     #debug
    global A
    global B
    A = 0
    B = 0
    def music_play():
        global A
        #print ("##debug A") #debug
        #print (A)   #debug
        str_files_music = ''.join(files_music[A])
        print ( "\n  -#- Играю музыкальный трек: " +  str_files_music)
        play_m(files_music[A])
        A += 1
    def ad_play():
        global B
        #print ("##debug B") #debug
        #print (B)   #debug
        str_files_ad = ''.join(files_ad[B])
        print ( "\n  -$- Играю рекламный трек: " +  str_files_ad)
        play_a(files_ad[B])
        B += 1

    while True:   # Cея конструкция играет по кругу все музыкальные и рекламные треки, на каждые два музыкальных один рекламный 
        if A < Al:
            #print ("##debug A")
            #print (A)
            music_play()
            if A < Al:
                #print ("##debug A") #debug
                #print (A)   #debug
                music_play()
                if B == Bl:
                    B = 0
 #                   print ("##debug B") #debug
 #                   print (B)   #debug
                    ad_play()
                    #B += 1
                else:
#                    print ("##debug B") #debug
#                    print (B)   #debug
                    ad_play()
        if A == Al:
            A = 0


def file_availability(directory_scan):
    list_music = os.listdir(directory_scan)
    if len(list_music) == 0:
        print ("\n  !!!!! !!!!!!!!!!! !!!!!!      В папке " + directory_scan + " файлов нет!!! Живо Загрузите их!       !!!!! !!!!!!!!!!! !!!!!!")
        return 0
    if len(list_music) > 0:
        #print ("\n Количество файлов в папке  " + directory_scan + " : " + str(len(list_music)))
        return 1
def info():
    print ("""\n          О Программе 

        Музыкальный плеер, разработан специально для Керамир.

        Реализованные функции:
        - Обновление музыки и рекламы с сервера Ural-K "Централизованная библиотека"
        - Загрузка обновленной версии плеера
        - Вывод информации Программе 







        """)

def program_update():
    try:
        ftp = FTP()
        HOST = '****************'
        PORT = 21
        login = '****************'
        password = '****************'
        ftp.connect(HOST, PORT)
        ftp.login(login,password)
        directory = ftp.cwd('music player') # Меняем директорию
        f = open("KMmusicplayer.py","wb")
        ftp.retrbinary("RETR " + "KMmusicplayer.py",f.write)
        f.close()
        print ("\n Загрузил! После обновления плеер нужно перезапустить.")
        sleep(1.0)
        print ("\n Программа завершится автоматически!")
        sleep(3.0)
    except:
        print ("Ошибка обновления программы!")  
        pass  



def commands():
    print ("\n Выбирите действие:\n\n   1    Загрузить/Обновить музыку и рекламу с сервера  \n   2 >> Играть музыку\n   3    Обновить плеер\n   4    Вывести справку/информацию")
    command = input()
    if command == "1":
        track_update()
        commands()
    if command == "2":
        if file_availability(directory_music) == 0:
            commands()
        if file_availability(directory_music) == 1:
            music_ad_play()
    if command == "3":
        program_update()
        raise SystemExit
    if command == "4":
        info()
        commands()    
    else:
        print ("\n Ошибка команды")
        commands()


print (" \n\n    News:\n     -Теперь музыка играет в случайном порядке\n\n\n     Музыкальный плеер: beta 0.2")
#print ("                             Designed for Keramir\n" )
print ("""
        █░▄▀ █▀▀ █▀▀▄ ▄▀▄ █▄░▄█ ▀ █▀▀▄ 
        █▀▄░ █▀▀ █▐█▀ █▀█ █░█░█ █ █▐█▀ 
        ▀░▀▀ ▀▀▀ ▀░▀▀ ▀░▀ ▀░░░▀ ▀ ▀░▀▀ 
            music            player
""")
commands()


"""
if Error_code_1 == 0:
    print ("Прога вернула 0! Выполняю действие....(На сервере нихрена нет!! Это странно)")
elif Error_code_1 == 1:
    print ("Прога  вернула 1! Выполняю действие....(Новых файлов на сервере нет!! Обновлять нечего, слушаем то что есть!)")
elif Error_code_1 == 10:
    print ("Прога   вернула 10! Выполняю действие....")
if Error_code_2 == 20:
    print ("Прога   вернула 20! Выполняю действие....")

"""