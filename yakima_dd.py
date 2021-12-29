# coding = utf-8

import requests, time
import vk_api
import tkinter, time
from threading import Thread
from tkinter import PhotoImage
from tkinter import *

VERSION = "v.0.2.0"


#Raid Funcions
print("""
⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⣿ 
⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿ 
⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿ 
⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠋ 
⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⢀ 
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴ 
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟ 
⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⠃ 
⣿⣿⣿⣿⣿⡆⠄ Yakima⠹⠈⢋⣽⣿⣿⣿⣿⣵⠃ 
⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠄ 
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁ 
⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁ 
⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁ 
⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃  
""")
print('Git: https://github.com/YakimaVisus')
def send_message(msg, conv_id, to_conv = True):
    if to_conv:
        user_id_ = 2000000000 + conv_id
    else:
        user_id_ = conv_id
    print(user_id_)

    return vk.messages.send(peer_id = user_id_, message = msg, random_id = 0)


def raid_launcher():
    start_btn.destroy()
    counter_text = tkinter.Label(text = "Отправлено:")
    counter_text.pack()
    Thread(target=raid, args=(int(conv_id.get()), is_to_ls.get(), counter_text )).start()

#Auth
token = "ТУТ ВАШ ТОКЕН"
session = vk_api.VkApi(token = token)
vk = session.get_api()


#Draw simple UI
root = tkinter.Tk()

#Temp vars
counter = 0
is_to_ls = tkinter.BooleanVar()
is_to_ls.set(0)
root.title("Troll_Bot By Yakima Visus " + VERSION)


tkinter.Label(text = "Настройка бота...", font = "Arial 35").pack()
tkinter.Label(text = "ID беседы/ЛС для обзывалок").pack()
conv_id = tkinter.Entry()
conv_id.pack()
tkinter.Label(text = "Ссылка на цель (пример @yakima_visus)").pack()
conv_ip = Entry(textvariable=send_message)
conv_ip.insert(0, " ")
conv_ip.pack()
def raid(conv_id, is_to_ls, counter_text):
    global counter
    while True:
        file = open('dialog.txt', encoding='utf-8', newline='')
        while True:
            for line in file:
                time.sleep(6)
                send_message (conv_ip.get()+"   "+ line ,conv_id, is_to_ls)
        counter += 1
        counter_text["text"] = "Отправлено: " + str(counter)
to_ls_checkbox = tkinter.Checkbutton(text = "Обзывалки в беседу", variable = is_to_ls)
to_ls_checkbox.pack()
tkinter.Label(text = "Чтобы поменять интервал замените в 77 строке \n time.sleep(ЧИСЛО) \n но нулчше это не трогать хз ", font = "Arial 8").pack()
start_btn = tkinter.Button(text = "Запуск ботика", command = raid_launcher , font = "Arial 10")
start_btn.pack()


root.mainloop()
