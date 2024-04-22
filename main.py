import requests
from bs4 import BeautifulSoup

from telegram import send_telegram
from telegramchannel import send_channel

import telebot

# import schedule
# from format_message import format_pred
bot = telebot.TeleBot('5529829120:AAGsUqlqofBzekr8wSIj2UZL15YOuvQTtRo')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text="Выполняю поиск")
    main()
    
    
def main():
    # message1 = result()
    
 
    cookies = {
        'cud': 'rBMAD2YCXpW9EQt3B/I3Ag==',
        '_ga': 'GA1.2.698336348.1711431335',
        '_ym_uid': '1711431339727122409',
        '_ym_d': '1711431339',
        'xq_icm': '13000',
        'acceptCookies': 'true',
        'lang': '0',
        '_ga_Y9VSRWL1PZ': 'GS1.2.1711457699.5.1.1711457810.0.0.0',
        '_gid': 'GA1.2.959385001.1712043743',
        '_ym_isad': '2',
        '_ga_NBF6PN1P8S': 'GS1.2.1712043760.4.1.1712045541.0.0.0',
    }

    headers = {
        'authority': 'd.betcity.by',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cud=rBMAD2YCXpW9EQt3B/I3Ag==; _ga=GA1.2.698336348.1711431335; _ym_uid=1711431339727122409; _ym_d=1711431339; xq_icm=13000; acceptCookies=true; lang=0; _ga_Y9VSRWL1PZ=GS1.2.1711457699.5.1.1711457810.0.0.0; _gid=GA1.2.959385001.1712043743; _ym_isad=2; _ga_NBF6PN1P8S=GS1.2.1712043760.4.1.1712045541.0.0.0',
        'origin': 'https://betcity.by',
        'referer': 'https://betcity.by/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Opera";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
    }



    params = {
    'rev': '5',
    'ver': '457',
    'csn': 'lsmif5',
    'id_sp': '46'
    }

    response = requests.get('https://d.betcity.by/api/v1/live/line', params=params, cookies=cookies, headers=headers)

    resultline = response.json()
    # print(resultline)
    tr = 46
    tr1 = str(tr)
    mass_game = []
    
    for vid in resultline['reply']['sports'][tr1]['chmps']:
        # liga = resultline['reply']['sports'][tr1]['chmps'][vid]['name_ch']
        # print(vid)
        evts = resultline['reply']['sports'][tr1]['chmps'][vid]['evts']
        for ev in evts:
            try:    
                stat = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['stat_link']
                ext =  resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['sc_inter']
                # print(ext)
            except:
                pass
            # print(stat)

            url_stat = f'https://betcity.by/ru/mstat/{stat}'
            # print(url_stat)
            if ext == '0:0':
    
        
        

                cookies = {
                    'cud': 'rBMAD2YCXpW9EQt3B/I3Ag==',
                    'close-page-text': '1',
                    '_ym_uid': '1711431339727122409',
                    '_ym_d': '1711431339',
                    'xq_icm': '13000',
                    'acceptCookies': 'true',
                    'lang': '0',
                    '_ga_Y9VSRWL1PZ': 'GS1.2.1711457699.5.1.1711457810.0.0.0',
                    '_gid': 'GA1.2.959385001.1712043743',
                    '_ym_isad': '2',
                    'dev': '3b25649755ac9e0bfbb7b95e50a57c44',
                    '_gat_gtag_UA_97174776_3': '1',
                    '_ga_NBF6PN1P8S': 'GS1.1.1712043760.4.1.1712046207.0.0.0',
                    '_ga': 'GA1.1.698336348.1711431335',
                }

                headers = {
                    'authority': 'betcity.by',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    # 'cookie': 'cud=rBMAD2YCXpW9EQt3B/I3Ag==; close-page-text=1; _ym_uid=1711431339727122409; _ym_d=1711431339; xq_icm=13000; acceptCookies=true; lang=0; _ga_Y9VSRWL1PZ=GS1.2.1711457699.5.1.1711457810.0.0.0; _gid=GA1.2.959385001.1712043743; _ym_isad=2; dev=3b25649755ac9e0bfbb7b95e50a57c44; _gat_gtag_UA_97174776_3=1; _ga_NBF6PN1P8S=GS1.1.1712043760.4.1.1712046207.0.0.0; _ga=GA1.1.698336348.1711431335',
                    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Opera";v="108"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0',
                }

                response = requests.get(url_stat, cookies=cookies, headers=headers).text
                soup = BeautifulSoup(response, 'lxml')
                ov_mass = get_ochnye_vstrechi(soup)
                kol_ov = kol_ochnyh_vstrech(ov_mass)
                lv_mass = get_last_vstrechi(soup)
                kol_lv = kol_ochnyh_vstrech(lv_mass)
                b,m = kol_set_18_5_bolshe(ov_mass)
                blv,mlv = kol_set_18_5_bolshe(lv_mass)
                bolshe = blv + b
                menshe = mlv + m
                print(bolshe, menshe)
                id_ev = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['id_ev']
#             # with codecs.open('spisok.txt','r' ,'utf-8') as file:

#             #     for item in file.readlines():
#             #         spis =[]
#             #         line = item.strip()
#             #         # print(line)
#             #         id = line.split('--')[0]
#             #         spis.append(id)
#             #         if str(id_ev) in spis:
#             #             print('Было отправлено') 
#             #         else:
#             # print(ov_mass)
#             # print(lv_mass)
#             # print(set1)
#             # print(set2)
#             # print(set3)
#             # print(set4)
#             # print(set5)

#             # print(kol_ov)
            
#             # print(b,m)
            
#             if (kol_ov == 10) and (kol_lv == 10):
#                 # if (10 >(int(b) - int(m)) >3) or (10>(int(m) - int(b)) >3):
#                 sets = []
                
                
                
                        
    
                # print(id_ev)
                liga = resultline['reply']['sports'][tr1]['chmps'][vid]['name_ch']
                
                print(liga)
                date_ev_str = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['date_ev_str']
                
                print(date_ev_str)
                name_ht = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_ht']
                
                print(name_ht)
                name_at = resultline['reply']['sports'][tr1]['chmps'][vid]['evts'][ev]['name_at']
                
                print(name_at)
#                 # set1_mass = get_o_v_1set(ov_mass)
#                 # print(set1_mass)
#                 # summ_set1 = summ_point_set_mass(set1_mass)
#                 # print(summ_set1)
#                 # set2_mass = get_o_v_2set(ov_mass)
#                 # print(set2_mass)
#                 # summ_set2 = summ_point_set_mass(set2_mass)
#                 # print(summ_set2)
#                 # set3_mass = get_o_v_3set(ov_mass)
#                 # print(set3_mass)
#                 # summ_set3 = summ_point_set_mass(set3_mass)
#                 # print(summ_set3)
#                 # set4_mass = get_o_v_4set(ov_mass)
#                 # print(set4_mass)
#                 # summ_set4 = summ_point_set_mass(set4_mass)
#                 # print(summ_set4)
#                 # set5_mass = get_o_v_5set(ov_mass)
#                 # print(set5_mass)
#                 # summ_set5 = summ_point_set_mass(set5_mass)
#                 # print(summ_set5)
                
                    
                
                
#                 # file.write(f'\n{date_ev_str}-{liga}-{name_ht}-{name_at}-{id_ev}')          
                    
                    
                
#                 if ((b - m) >= 10) and ((mlv - blv) >= 1) and ((mlv / blv) < 2):
                    

#                     st = 'ТБ 18.5'
#                     game = []
#                     setsb = []
#                     setsm = []
#                     b1,m1 = kol_set_18_5_bolshe(set1)
#                     b2,m2 = kol_set_18_5_bolshe(set2)
#                     b3,m3 = kol_set_18_5_bolshe(set3)
#                     b4,m4 = kol_set_18_5_bolshe(set4)
#                     b5,m5 = kol_set_18_5_bolshe(set5)
#                     if (b1 > m1):
#                         setsb.append('1')
#                     else:
#                         setsm.append('1')
#                     if (b2 > m2):
#                         setsb.append('2')
#                     else:
#                         setsm.append('2')
#                     if (b3 > m3):
#                         setsb.append('3')
#                     else:
#                         setsm.append('3')
#                     if (b4 > m4):
#                         setsb.append('4')
#                     else:
#                         setsm.append('4')
#                     if (b5 > m5):
#                         setsb.append('5')
#                     else:
#                         setsm.append('5')
                    
#                     game.append(id_ev)
#                     game.append(liga)
#                     game.append(date_ev_str)
#                     game.append(name_ht)
#                     game.append(name_at)
#                     game.append(b)
#                     game.append(m)
#                     game.append(st)
#                     game.append(blv)
#                     game.append(mlv)
#                     game.append(setsb)
#                     game.append(setsm)
#                     mass_game.append(game)



#                     # bs1 = get_kol_bolshe(summ_set1)
#                     # print(bs1)
#                     # if bs1 >= 8:
#                     #     sets.append('1')
                    
#                     # bs2 = get_kol_bolshe(summ_set2)
#                     # print(bs1)
#                     # if bs2 >= 8:
#                     #     sets.append('2')
                    
#                     # bs3 = get_kol_bolshe(summ_set3)
#                     # print(bs3)
#                     # if bs3 >= 8:
#                     #     sets.append('3')
                    
#                     # bs4 = get_kol_bolshe(summ_set4)
#                     # print(bs4)
#                     # if bs4 >= 7:
#                     #     sets.append('4')
                    
#                     # bs5 = get_kol_bolshe(summ_set5)
#                     # print(bs5)
#                     # if bs5 >= 7:
#                     #     sets.append('5')



                    



                    
#                 if ((m - b) >= 10) and ((blv - mlv) >=1) and ((blv / mlv) < 2):
#                     st = 'ТМ 18.5'
#                     game = []
#                     setsb = []
#                     setsm = []
#                     b1,m1 = kol_set_18_5_bolshe(set1)
#                     b2,m2 = kol_set_18_5_bolshe(set2)
#                     b3,m3 = kol_set_18_5_bolshe(set3)
#                     b4,m4 = kol_set_18_5_bolshe(set4)
#                     b5,m5 = kol_set_18_5_bolshe(set5)
#                     if (b1 < m1):
#                         setsm.append('1')
#                     else:
#                         setsb.append('1')
#                     if (b2 < m2):
#                         setsm.append('2')
#                     else:
#                         setsb.append('2')
#                     if (b3 < m3):
#                         setsm.append('3')
#                     else:
#                         setsb.append('3')
#                     if (b4 < m4):
#                         setsm.append('4')
#                     else:
#                         setsb.append('4')
#                     if (b5 < m5):
#                         setsm.append('5')
#                     else:
#                         setsb.append('5')

#                     game.append(id_ev)
#                     game.append(liga)
#                     game.append(date_ev_str)
#                     game.append(name_ht)
#                     game.append(name_at)
#                     game.append(b)
#                     game.append(m)
#                     game.append(st)
#                     game.append(blv)
#                     game.append(mlv)
#                     game.append(setsb)
#                     game.append(setsm)
#                     mass_game.append(game)
#                     # ms1 = get_kol_menshe(summ_set1)
#                     # print(ms1)
#                     # if ms1 >= 8:
#                     #     sets.append('1')
                    
#                     # ms2 = get_kol_menshe(summ_set2)
#                     # print(ms1)
#                     # if ms2 >= 8:
#                     #     sets.append('2')
                    
#                     # ms3 = get_kol_menshe(summ_set3)
#                     # print(ms3)
#                     # if ms3 >= 8:
#                     #     sets.append('3')
                    
#                     # ms4 = get_kol_menshe(summ_set4)
#                     # print(ms4)
#                     # if ms4 >= 7:
#                     #     sets.append('4')
                    
#                     # ms5 = get_kol_menshe(summ_set5)
#                     # print(ms5)
#                     # if ms5 >= 7:
#                     #     sets.append('5')
#                 # game.append(sets)
#                 # with open('game_spis.txt', 'a') as f:
#                 #     f.write(f'\n{id_ev}')          
#                 #     f.close()  
#                 else:
#                     pass
                        
#     print(mass_game)                            
#     s = sorted(mass_game, key=lambda student: student[2])
#     mass_game.clear()
#     print(s)  
    
#     for g in s:
#         # print(g[2],g[3],g[4]) 
#         with codecs.open('spisok.txt', 'a', 'utf-8') as file:
#             file.write(f'\n{g[0]}--{g[1]}--{g[2]}--{g[3]}--{g[4]}--{g[7]}') 
#             file.close()
#         # fsets = ''
#         # for g8 in g[8]:
#         #     fesets = f'{g8} '
#         #     fsets = fsets + fesets
                mess = f'\U0001F4C6 {date_ev_str} \n' \
                            f'\U0001F3D3 {liga}\n' \
                            f'\U0001F9D1 {name_ht} - {name_at} \n' \
                           \
                            f'\U0001F4B2 Последние: {bolshe} - {menshe} \n'\
                            \
                            \
                            f'----------------------------------------------------------\n'\
                            # f'\n' 
                # message = message + mess  
                        
                send_telegram(mess)
                send_channel(mess)
#         # print('send')            
#         print(mess)         
    
def get_last_vstrechi(mass_stat):
    # Создаем пустой массив
    lv_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in mass_stat.find_all('table', class_ = 'ev-mstat-tbl'):
        # Пробегаем циклом по тэгу <tr>
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'ev-mstat-sc'):
                # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                try:
                    td = ted.get_text()
                    # Парсим содержимое тега
                    td1 = td.split(' (')[1]
                    # Удаляем все знаки ' в строке
                    td2 = td1.replace(')', "")
                    # Удаляем все знаки , в строке
                    td3 = td2.replace(',', "")
                    # Добавляем полученный результат в подготовленный нами массив
                    lv_mass.append(td3)
                except:
                    pass
    # Возвращаем готовый массив 
    return(lv_mass)

def get_ochnye_vstrechi(mass_stat):
    # Создаем пустой массив
    ov_mass = []
    # Цикл переборки массива, переданного в функцию
    # Пробегаем циклом по тэгу <table>
    for body in mass_stat.find_all('table', class_ = ''):
        # Пробегаем циклом по тэгу <tr>
        for tr in body.find_all('tr', class_ = ''):
            # Пробегаем циклом по тэгу <td> в классе 'score'
            for ted in tr.find_all('td', class_ = 'score'):
                # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
                td = ted.get_text()
                # Парсим содержимое тега
                td1 = td.split(' (')[1]
                # Удаляем все знаки ' в строке
                td2 = td1.replace(')', "")
                # Удаляем все знаки , в строке
                td3 = td2.replace(',', "")
                # Добавляем полученный результат в подготовленный нами массив
                ov_mass.append(td3)
    # Возвращаем готовый массив 
    return(ov_mass)


    
# def parse(soup):
#     ov_mass = []
#     # Цикл переборки массива, переданного в функцию
#     # Пробегаем циклом по тэгу <table>
#     for body in soup.find_all('table', class_ = ''):
#         # print(body)
#         # Пробегаем циклом по тэгу <tr>
#         for tr1 in body.find_all('tr', class_ = 'line'):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
#             for ted in tr1.find_all('td', class_ = 'score'):
#                 try:
#                     # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                     td = ted.get_text()
#                     # Парсим содержимое тега
#                     td1 = td.split(' (')[1]
#                     # Удаляем все знаки ' в строке
#                     td2 = td1.replace(')', "")
#                     # Удаляем все знаки , в строке
#                     td3 = td2.replace(',', "")
#                     # Добавляем полученный результат в подготовленный нами массив
#                     ov_mass.append(td3)
#                 except:
#                     pass
#         for tr in body.find_all('tr', class_ = ''):
#             # Пробегаем циклом по тэгу <td> в классе 'score'
#             for ted in tr.find_all('td', class_ = 'score'):
#                 try:
#                     # Получаем нужный нам тэг <td> и получаем текст который находится внутри него
#                     td = ted.get_text()
#                     # Парсим содержимое тега
#                     td1 = td.split(' (')[1]
#                     # Удаляем все знаки ' в строке
#                     td2 = td1.replace(')', "")
#                     # Удаляем все знаки , в строке
#                     td3 = td2.replace(',', "")
#                     # Добавляем полученный результат в подготовленный нами массив
#                     ov_mass.append(td3)
#                 except:
#                     pass
#     return ov_mass

def kol_ochnyh_vstrech(ov_mass):
    # Создаем переменную и присваиваем ей 0
    i = 0
    # Цикл переборки полученного массива
    for vstrecha in ov_mass:
        # Прибавляем 1 к переменной при пробегании массива
        i = i + 1
    # Возвращаем полученный массив значений
    return(i)

def kol_set_18_5_bolshe(lv_mass):
    # Создаем пустой массив
    set_mass = []
    # Цикл переборки полученного массива
    for game in lv_mass:
        
        try:
            set = game.split(' ')[0]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[1]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[2]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[3]
            
            set_mass.append(set)
        except:
            pass
        try:
            set = game.split(' ')[4]
            
            set_mass.append(set)
        except:
            pass
        
    # print(set_mass)
    sum_point = summ_point_set_mass(set_mass)
    b = 0
    m = 0
    for sum_set_point in sum_point:
        if sum_set_point >= 19:
            b+=1
        if sum_set_point <= 18:
            m+=1
        
    # Возвращаем полученный массив значений
    return(b,m)


def summ_point_set_mass(set_mass):
    # Создаем пустой массив
    summ_set_mass = []
    # Цикл переборки полученного массива
    for si in (set_mass):
        
        # Обработка исключений счетчика сумм
        try:
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
            s1 = si.split(':')[0] 
            # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
            s2 = si.split(':')[1]    
            # Получаем сумму переменных    
            summ = int(s1) + int(s2)
            # Добавляем полученную сумму в массив
            summ_set_mass.append(summ)
        # Выполняется в случае возникновения исключения
        except:
            # Пропустить - ничего не выполнять
            pass
    # Возвращаем полученный массив значений
    return(summ_set_mass)

# # Функция формирования массива со счетом первых партий очных встреч
# def get_o_v_1set(ov_mass):
#     # Создаем пустой массив
#     ov_1set_mass = []
#     # Цикл переборки полученного массива
#     for set_1 in ov_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_1_1 = set_1.split(' ')[0]
#         # Добавляем полученное значение в массив
#         ov_1set_mass.append(set_1_1)
#     # Возвращаем полученный массив значений    
#     return(ov_1set_mass)
    
# # Функция формирования массива со счетом вторых партий очных встреч
# def get_o_v_2set(ov_mass):
#     # Создаем пустой массив
#     ov_2set_mass = []
#     # Цикл переборки полученного массива
#     for set_2 in ov_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_2_1 = set_2.split(' ')[1]
#         # Добавляем полученное значение в массив
#         ov_2set_mass.append(set_2_1)
#     # Возвращаем полученный массив значений
#     return(ov_2set_mass)

# # Функция формирования массива со счетом третьих партий очных встреч
# def get_o_v_3set(ov_mass):
#     # Создаем пустой массив
#     ov_3set_mass = []
#     # Цикл переборки полученного массива
#     for set_3 in ov_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_3_1 = set_3.split(' ')[2]
#         # Добавляем полученное значение в массив
#         ov_3set_mass.append(set_3_1)
#     # Возвращаем полученный массив значений
#     return(ov_3set_mass)

# # Функция формирования массива со счетом четвертых партий очных встреч
# def get_o_v_4set(ov_mass):
#     # Создаем пустой массив
#     ov_4set_mass = []
#     # Цикл переборки полученного массива
#     for set_4 in ov_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_4_1 = set_4.split(' ')[3]
#         # Добавляем полученное значение в массив
#         ov_4set_mass.append(set_4_1)
#     # Возвращаем полученный массив значений
#     return(ov_4set_mass)

# # Функция формирования массива со счетом пятых партий очных встреч
# def get_o_v_5set(ov_mass):
#     # Создаем пустой массив
#     ov_5set_mass = []
#     # Цикл переборки полученного массива
#     for set_5 in ov_mass:
#         try:# Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#             set_5_1 = set_5.split(' ')[4]
#             # Добавляем полученное значение в массив
#             ov_5set_mass.append(set_5_1)
#         except:
#             pass
#     # Возвращаем полученный массив значений
#     return(ov_5set_mass)

# # Функция получения количества партий с тоталом меньше 18.5 из переданного массива с суммами очков по партиям
# def get_kol_menshe(summ_point):
#     # Создаем переменную и присваиваем ей 0
#     i = 0
#     # Цикл переборки полученного массива
#     for bolshe in summ_point:
#         # Проверяем число полученное циклом
#         if int(bolshe) <= 18:
#             # Если условие выполняется прибавляем 1 к переменной
#             i+=1
#     # Возвращаем полученное количество
#     return (i)

# # Функция получения количества партий с тоталом больше 18.5 из переданного массива с суммами очков по партиям
# def get_kol_bolshe(summ_point):
#     # Создаем переменную и присваиваем ей 0
#     i = 0
#     # Цикл переборки полученного массива
#     for bolshe in summ_point:
#         # Проверяем число полученное циклом
#         if int(bolshe) >= 19:
#             # Если условие выполняется прибавляем 1 к переменной
#             i+=1
#             # Возвращаем полученное количество
#     return (i)


# # Функцтя формирования массива с суммами очков по партиям
# def summ_point_set_mass(set_mass):
#     # Создаем пустой массив
#     summ_set_mass = []
#     # Цикл переборки полученного массива
#     for si in (set_mass):
        
#         # Обработка исключений счетчика сумм
#         try:
#             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#             s1 = si.split(':')[0] 
#             # Парсим строку по заданному символу и присваиваем нужную часть строки переменной           
#             s2 = si.split(':')[1]    
#             # Получаем сумму переменных    
#             summ = int(s1) + int(s2)
#             # Добавляем полученную сумму в массив
#             summ_set_mass.append(summ)
#         # Выполняется в случае возникновения исключения
#         except:
#             # Пропустить - ничего не выполнять
#             pass
#     # Возвращаем полученный массив значений
#     return(summ_set_mass)

# def get_l_v_1set(lv_mass):
#     # Создаем пустой массив
#     ov_1set_mass = []
#     # Цикл переборки полученного массива
#     for set_1 in lv_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_1_1 = set_1.split(' ')[0]
#         # Добавляем полученное значение в массив
#         ov_1set_mass.append(set_1_1)
#     # Возвращаем полученный массив значений    
#     return(ov_1set_mass)
    
# # Функция формирования массива со счетом вторых партий очных встреч
# def get_l_v_2set(lv_mass):
#     # Создаем пустой массив
#     ov_2set_mass = []
#     # Цикл переборки полученного массива
#     for set_2 in lv_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_2_1 = set_2.split(' ')[0]
#         # Добавляем полученное значение в массив
#         ov_2set_mass.append(set_2_1)
#     # Возвращаем полученный массив значений
#     return(ov_2set_mass)

# # Функция формирования массива со счетом третьих партий очных встреч
# def get_l_v_3set(lv_mass):
#     # Создаем пустой массив
#     ov_3set_mass = []
#     # Цикл переборки полученного массива
#     for set_3 in lv_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_3_1 = set_3.split(' ')[2]
#         # Добавляем полученное значение в массив
#         ov_3set_mass.append(set_3_1)
#     # Возвращаем полученный массив значений
#     return(ov_3set_mass)

# # Функция формирования массива со счетом четвертых партий очных встреч
# def get_l_v_4set(lv_mass):
#     # Создаем пустой массив
#     ov_4set_mass = []
#     # Цикл переборки полученного массива
#     for set_4 in lv_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_4_1 = set_4.split(' ')[3]
#         # Добавляем полученное значение в массив
#         ov_4set_mass.append(set_4_1)
#     # Возвращаем полученный массив значений
#     return(ov_4set_mass)

# # Функция формирования массива со счетом пятых партий очных встреч
# def get_l_v_5set(lv_mass):
#     # Создаем пустой массив
#     ov_5set_mass = []
#     # Цикл переборки полученного массива
#     for set_5 in lv_mass:
#         # Парсим строку по заданному символу и присваиваем нужную часть строки переменной
#         set_5_1 = set_5.split(' ')[3]
#         # Добавляем полученное значение в массив
#         ov_5set_mass.append(set_5_1)
#     # Возвращаем полученный массив значений
#     return(ov_5set_mass)
# if __name__ == '__main__':
#     main()
bot.polling(none_stop=True)