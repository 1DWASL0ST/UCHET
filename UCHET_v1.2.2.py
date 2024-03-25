# ПЕРЕПИСАТЬ ПУТЬ ФАЙЛА
def output():
    import re
    import tkinter as tk
    window = tk.Tk()
    
    j = 0
    with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'r', encoding = 'utf-8') as a:
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 5:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
        print('дата наименование цена себестоимость вид оплаты')
        for i in range (len(TABLITSA)):
            for j in range(5):
                result = tk.Label(window, text = TABLITSA[i][j])
                result.grid(stick= 'we', row= i, column= j)
        #     print(*TABLITSA[i])
        # print(' ')
    window.mainloop()
def day_delete():
    with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'w') as a:
        a.close
def day_revenue():
    import re
    import tkinter as tk
    window = tk.Tk()
    j = 0
    revenue = 0
    perevod_revenue = 0
    cash_renevue = 0
    mts_revenue = 0
    with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'r', encoding= 'utf - 8') as a:
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 5:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
        for i in range(len(TABLITSA)):
            revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            if 'наличными' == TABLITSA[i][4] or 'наличные' == TABLITSA[i][4]:
                cash_renevue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            elif 'переводом' == TABLITSA[i][4] or 'перевод'== TABLITSA[i][4]:
                perevod_revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            elif 'мтс' == TABLITSA[i][4]:
                mts_revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
        l1 = tk.Label(window, text= 'Общая выручка:')
        l11 = tk.Label(window, text= revenue)
        l2 = tk.Label(window, text ='Выручка Наличными:')
        l21 = tk.Label(window, text= cash_renevue)
        l3 = tk.Label(window, text ='Выручка переводом:')
        l31 = tk.Label(window, text= perevod_revenue)
        l4 = tk.Label(window, text ='выручка на мтс:')
        l41 = tk.Label(window, text= mts_revenue)
        l1.grid(sticky='we',row= 0, column= 0)
        l2.grid(sticky='we',row= 1, column= 0)
        l3.grid(sticky='we',row= 2, column= 0)
        l4.grid(sticky='we',row= 3, column= 0)
        l11.grid(sticky='we',row= 0, column= 1)
        l21.grid(sticky='we',row= 1, column= 1)
        l31.grid(sticky='we',row= 2, column= 1)
        l41.grid(sticky='we',row= 3, column= 1)
        window.mainloop()
def insert1():
    import tkinter as tk
    window = tk.Tk()
    l1 = tk.Label(window, text ='введите дату')
    l1.grid(sticky= 'we', row= 0, column= 0)
    e1 = tk.Entry(window)
    e1.grid(sticky= 'we', row= 1, column= 0)
    
    l2 = tk.Label(window, text ='введите наименование товара')
    l2.grid(sticky= 'we', row= 2, column= 0)
    e2 = tk.Entry(window)
    e2.grid(sticky= 'we', row= 3, column= 0)
    
    l3 = tk.Label(window, text ='введите цену товара')
    l3.grid(sticky= 'we', row= 4, column= 0)
    e3 = tk.Entry(window)
    e3.grid(sticky= 'we', row= 5, column= 0)
    
    l4 = tk.Label(window, text ='введите себестоимость товара')
    l4.grid(sticky= 'we', row= 6, column= 0)
    e4 = tk.Entry(window)
    e4.grid(sticky= 'we', row= 7, column= 0)
    
    l5 = tk.Label(window, text ='введите тип оплаты')
    l5.grid(sticky= 'we', row= 8, column= 0)
    e5 = tk.Entry(window)
    e5.grid(sticky= 'we', row= 9, column= 0)
   
    
    b = tk.Button(window, text= 'Подтвердить')
    
    def insert(event):
        with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'a+', encoding= 'utf - 8') as a:
            date = e1.get()
            name = e2.get()
            cost = e3.get()
            cost_price = e4.get()
            transaction_type = e5.get()
            t_type = transaction_type.lower()
            a.write(date)
            a.write((';'))
            a.write(name)
            a.write((';'))
            a.write(cost)
            a.write((';'))
            a.write(cost_price)
            a.write((';'))
            a.write(t_type + (';') + '\n')
    b.bind('<Button-1>', insert)        
    b.grid(sticky= 'we', row= 10, column= 0)
    window.mainloop()
def week_insert():
    import re
    j = 0
    revenue = 0
    perevod_revenue = 0
    cash_renevue = 0
    mts_revenue = 0
    with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'r', encoding= 'utf - 8') as a:
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 5:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
        for i in range(len(TABLITSA)):
            revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            if 'наличными' == TABLITSA[i][4] or 'наличные' == TABLITSA[i][4]:
                cash_renevue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            elif 'переводом' == TABLITSA[i][4] or 'перевод'== TABLITSA[i][4]:
                perevod_revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
            elif 'мтс' == TABLITSA[i][4]:
                mts_revenue += float(TABLITSA[i][2]) - float(TABLITSA[i][3])
    with open(r'C:\Users\1dwasl0st\Desktop\week_sells.txt', 'a+', encoding= 'utf - 8') as b:
        rev = str(revenue)
        cash = str(cash_renevue)
        per = str(perevod_revenue)
        mts = str(mts_revenue)
        b.write(rev)
        b.write((';'))
        b.write(cash)
        b.write((';'))
        b.write(per)
        b.write((';'))
        b.write(mts + (';') + '\n')
def month_insert():
    with open(r'C:\Users\1dwasl0st\Desktop\week_sells.txt', 'r', encoding= 'utf - 8') as a:
        import re
        j = 0
        revenue = 0
        perevod_revenue = 0
        cash_renevue = 0
        mts_revenue = 0
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 4:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
        for i in range (len(TABLITSA)):
            revenue += float(TABLITSA[i][0])
            perevod_revenue += float(TABLITSA[i][1])
            cash_renevue += float(TABLITSA[i][2])
            mts_revenue += float(TABLITSA[i][3])
    with open(r'C:\Users\1dwasl0st\Desktop\month_sells.txt', 'a+', encoding= 'utf - 8') as b:
        rev = str(revenue)
        cash = str(cash_renevue)
        per = str(perevod_revenue)
        mts = str(mts_revenue)
        b.write(rev)
        b.write((';'))
        b.write(cash)
        b.write((';'))
        b.write(per)
        b.write((';'))
        b.write(mts + (';') + '\n')
def week_report():
    with open(r'C:\Users\1dwasl0st\Desktop\week_sells.txt', 'r', encoding= 'utf - 8') as a:
        import re
        import tkinter as tk
        window = tk.Tk()
        j = 0
        revenue = 0
        perevod_revenue = 0
        cash_renevue = 0
        mts_revenue = 0
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 4:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
        for i in range (len(TABLITSA)):
            revenue += float(TABLITSA[i][0])
            perevod_revenue += float(TABLITSA[i][1])
            cash_renevue += float(TABLITSA[i][2])
            mts_revenue += float(TABLITSA[i][3])
        l1 = tk.Label(window, text= 'Общая выручка:')
        l11 = tk.Label(window, text= revenue)
        l2 = tk.Label(window, text ='Наличными:')
        l21 = tk.Label(window, text= cash_renevue)
        l3 = tk.Label(window, text ='переводом:')
        l31 = tk.Label(window, text= perevod_revenue)
        l4 = tk.Label(window, text ='на мтс:')
        l41 = tk.Label(window, text= mts_revenue)
        l1.grid(sticky='we',row= 0, column= 0)
        l2.grid(sticky='we',row= 1, column= 0)
        l3.grid(sticky='we',row= 2, column= 0)
        l4.grid(sticky='we',row= 3, column= 0)
        l11.grid(sticky='we',row= 0, column= 1)
        l21.grid(sticky='we',row= 1, column= 1)
        l31.grid(sticky='we',row= 2, column= 1)
        l41.grid(sticky='we',row= 3, column= 1)
        window.mainloop()
def month_report1():
    import tkinter as tk
    window = tk.Tk()
    l0 = tk.Label(window, text='Введите прочие расходы')
    l0.grid(sticky='w', row= 0, column=0)
    l01 = tk.Label(window, text='Введите зарплату сотрудникам')
    l01.grid(sticky='w', row= 2, column=0)
    e0 = tk.Entry(window)
    e0.grid(sticky='w', row= 1, column=0)
    e01 = tk.Entry(window)
    e01.grid(sticky='w', row= 3, column=0)
    b = tk.Button(window, text= 'Подтвердить')
    def month_report(event):
        with open(r'C:\Users\1dwasl0st\Desktop\month_sells.txt', 'r', encoding= 'utf - 8') as a:
            import re
            taxes = float(e0.get())
            sallary = float(e01.get())
            j = 0
            revenue = 0
            perevod_revenue = 0
            cash_renevue = 0
            mts_revenue = 0
            STROKA = []
            TABLITSA = []
            data = a.read()
            DATA = re.split(';|\n', data)
            I = len(DATA)
            for i in range (I):
                if DATA[i] != '':
                    STROKA.append(DATA[i])
                    j += 1
                    if j == 4:
                        TABLITSA += [STROKA]
                        STROKA = []
                        j = 0
            for i in range (len(TABLITSA)):
                revenue += float(TABLITSA[i][0])
                perevod_revenue += float(TABLITSA[i][1])
                cash_renevue += float(TABLITSA[i][2])
                mts_revenue += float(TABLITSA[i][3])
        l1 = tk.Label(window, text= 'Общая выручка:')
        l11 = tk.Label(window, text= revenue)
        l2 = tk.Label(window, text ='Наличными:')
        l21 = tk.Label(window, text= cash_renevue)
        l3 = tk.Label(window, text ='переводом:')
        l31 = tk.Label(window, text= perevod_revenue)
        l4 = tk.Label(window, text ='на мтс:')
        l41 = tk.Label(window, text= mts_revenue)
        l5 = tk.Label(window, text='чистая прибыль:')
        l51 = tk.Label(window, text=((revenue - taxes) - sallary))
        l1.grid(sticky='we',row= 0, column= 1)
        l2.grid(sticky='we',row= 1, column= 1)
        l3.grid(sticky='we',row= 2, column= 1)
        l4.grid(sticky='we',row= 3, column= 1)
        l5.grid(sticky='we',row= 4, column= 1)
        l11.grid(sticky='we',row= 0, column= 2)
        l21.grid(sticky='we',row= 1, column= 2)
        l31.grid(sticky='we',row= 2, column= 2)
        l41.grid(sticky='we',row= 3, column= 2)
        l51.grid(sticky='we',row= 4, column= 2)
    b.bind('<Button-1>', month_report)
    b.grid(sticky= 'we',row= 4, column= 0)
    window.mainloop()
def week_delete():
    with open(r'C:\Users\1dwasl0st\Desktop\week_sells.txt', 'w') as a:
        a.close
def month_delete():
    with open(r'C:\Users\1dwasl0st\Desktop\month_sells.txt', 'w') as a:
        a.close
def manual():
    import tkinter as tk
    import io
    window = tk.Tk()

    with io.open(r'C:\Users\1dwasl0st\Desktop\manual.txt', 'r',  encoding='utf-8' ) as a:
        text = a.read()
        result = text.split('\n')
    for i in range (len(result)):
        l = tk.Label(window, text= result[i])
        l.grid(sticky= 'w', row= i, column= 0)
    window.mainloop()
def all_days_insert():
    with open(r'C:\Users\1dwasl0st\Desktop\day_sells.txt', 'r', encoding= 'utf - 8') as a:
        import re
        j = 0
        STROKA = []
        TABLITSA = []
        data = a.read()
        DATA = re.split(';|\n', data)
        I = len(DATA)
        for i in range (I):
            if DATA[i] != '':
                STROKA.append(DATA[i])
                j += 1
                if j == 5:
                    TABLITSA += [STROKA]
                    STROKA = []
                    j = 0
                    k = -1
                    for h in range(1):
                        k += 1
                        with open(r'C:\Users\1dwasl0st\Desktop\all_day_sells.txt', 'a+', encoding= 'utf - 8') as b:
                            date = (TABLITSA[k][0])
                            name = (TABLITSA[k][1])
                            cost = TABLITSA[k][2]
                            cost_price = (TABLITSA[k][3])
                            transaction_type = (TABLITSA[k][4])
                            dat = str(date)
                            nam = str(name)
                            cos = str(cost)
                            cp = str(cost_price)
                            tt = str(transaction_type)
                            b.write(dat)
                            b.write((';'))
                            b.write(nam)
                            b.write((';'))
                            b.write(cos)
                            b.write((';'))
                            b.write((cp))
                            b.write((';'))
                            b.write(tt + (';') + '\n')
def close():
    all_days_insert()
    week_insert()
    month_insert()
    day_delete()      
def search1():
    import re
    import tkinter as tk
    window = tk.Tk()
    
    e = tk.Entry(window)
    b = tk.Button(window, text = 'Найти')
    l = tk.Label(window)
   
    
    def search(event):
        import tkinter as tk   
        with open(r'C:\Users\1dwasl0st\Desktop\all_day_sells.txt', 'r') as a:
            print('Введите дату и/или наименование товара')
            
            searching = e.get()
            Searching = searching.split(' ')
            STROKA = []
            TABLITSA = []
            data = a.read()
            DATA = re.split(';|\n', data)
            I = len(DATA)
            j = 0
            for i in range (I):
                if DATA[i] != '':
                    STROKA.append(DATA[i])
                    j += 1
                    if j == 5:
                        TABLITSA += [STROKA]
                        STROKA = []
                        j = 0
            TABLITSA = TABLITSA[::-1]
        
            availability = False
            print('Результаты поиска: \n ')
            if len(Searching) > 2:
                availability = True
                l["text"] = 'Ошибка: Введено что то кроме даты и наименования'
            if Searching[0] == '':
                availability = True
                l["text"] ='Ошибка: Введён пустой запрос'
            if len(Searching) == 1 and Searching[0] != '' :
                for i in range(len(TABLITSA)):
                    b = TABLITSA[i][0]
                    c = TABLITSA[i][1]
                    if Searching[0] == b or Searching[0] == c :
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
                    elif Searching[0] in b or Searching[0] in c :
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
            if len(Searching) == 2:
                for i in range(len(TABLITSA)):
                    b = TABLITSA[i][0]
                    c = TABLITSA[i][1]
                    if Searching[0] == b and Searching[1] == c:
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
                    elif Searching[0] == c and Searching[1] == b:
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
                    elif Searching[0] in c and Searching[1] == b:
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
                    elif Searching[0] == b and Searching[1] in c:
                        availability = True
                        for j in range(5):
                            
                            result = tk.Label(window, text = TABLITSA[i][j])
                            result.grid(stick= 'we', row= (i + 2), column= j)
            if availability == False:
                l["text"] ='Нет результатов : Проверьте правильность введённых данных'
                
    b.bind('<Button-1>', search)
    l.grid(column= 0, row = 2)
    e.grid(column= 0, row = 0)
    b.grid(column= 0, row = 1)
             
    window.mainloop()
def main():
    import tkinter
    tk = tkinter.Tk()
    tk.title('Учёт')
    tk.geometry('1280x540')
        
    b1 = tkinter.Button(tk, text='Нажмите чтобы внести информацию о продаже', command = insert1)
    b2 = tkinter.Button(tk, text='Нажмите чтобы вывести список продаж', command = output)
    b3 = tkinter.Button(tk, text='Нажмите чтобы вывести отчет за смену', command = day_revenue)
    b4 = tkinter.Button(tk, text='Нажмите чтобы завершить смену', command = close)
    b5 = tkinter.Button(tk, text='Нажмите чтобы вывести недельный отчет', command = week_report)
    b6 = tkinter.Button(tk, text='Нажмите чтобы вывести месячный отчет', command = month_report1)
    b7 = tkinter.Button(tk, text='Нажмите чтобы начать новую неделю', command = week_delete)
    b8 = tkinter.Button(tk, text='Нажмите чтобы начать новый месяц', command = month_delete)
    b10 = tkinter.Button(tk, text='Нажмите чтобы найти продажу по дате и наименованию', command = search1)
    b9 = tkinter.Button(tk, text='Нажмите чтобы просмотреть ИНСТРУКЦИЮ', command = manual)

    b1.grid(stick= 'we',column= 0)
    b2.grid(stick= 'we',column= 0)
    b3.grid(stick= 'we',column= 0)
    b4.grid(stick= 'we',column= 0)
    b5.grid(stick= 'we',column= 0)
    b6.grid(stick= 'we',column= 0)
    b7.grid(stick= 'we',column= 0)
    b8.grid(stick= 'we',column= 0)
    b10.grid(stick= 'we',column= 0)
    b9.grid(stick= 'we',column= 0)
    tk.mainloop()
main()