class book:
    """Книга"""
    def __init__(self, id, name, year, author, bibl_id):
        self.id = id
        self.name = name
        self.year = year
        self.author = author
        self.bibl_id = bibl_id

class bibl:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class boobib:
    """
    'Книги находящиейся в библиотеке' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, bibl_id, book_id):
        self.bibl_id = bibl_id
        self.book_id = book_id

#Библиотеки
bibls = [
    bibl(1, 'Российская государственная библиотека'),
    bibl(2, 'Государственная публичная историческая библиотека России'),
    bibl(3, 'Политехническая библиотека'),
    bibl(4, 'Российская государственная библиотека искусств'),
    bibl(5, 'Российская государственная библиотека для молодёжи')
]

#Книги
books = [
    book(1, 'Крутой маршрут. Хроника времен культа личности', 2017, 'Евгения Гинзбург', 2),
    book(2, 'Люди, которые всегда со мной', 2019, 'Наринэ Абгарян', 5),
    book(3, 'Лето в пионерском галстуке', 2021, 'Катерина Сильванова, Елена Малисова', 4),
    book(4, 'Симон', 2020, 'Наринэ Абгарян', 1),
    book(5, '"Несвятые святые" и другие рассказы (сборник)', 2018, 'Архимандрит Тихон', 5),
    book(6, 'Манюня', 2021, 'Наринэ Абгарян', 5),
    book(7, 'Зулейха открывает глаза', 2020, 'Гузель Яхина', 2),
    book(8, 'Дарители. Короли будущего', 2016, 'Екатерина Соболь', 3),
    book(9, 'Дом, в котором...', 2015, 'Мариам Петросян', 1),
    book(10, 'Азазель', 2019, 'Борис Акунин', 1)
]

boo_bib = [
    boobib(1,9),
    boobib(1,10),
    boobib(2,7),
    boobib(2,1),
    boobib(5,2),
    boobib(3,8),
    boobib(4,3),
    boobib(5,5),
    boobib(5,6),
    boobib(1,4),
    boobib(1,6),
    boobib(5,3),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(bk.name, bk.year, bk.author, bb.name) 
        for bb in bibls 
        for bk in books 
        if bk.bibl_id==bb.id]
    
    print('Задание Е1')

    res_e1 = []
    # Перебираем все библиотеки
    for bb in bibls:
        if 'библиотека' in bb.name:
            bb_books = list(filter(lambda i: i[3]==bb.name, one_to_many))
            res_e1.append(bb_books)
    print(res_e1)
    
    print('\nЗадание Е2')
    
    res_e2 = []
    res = []
    for bb in bibls:
        sum = 0
        res.clear()
        res.append(bb.name)
        for bk in books:
            if (bb.id == bk.bibl_id):
                sum = sum + 1
        res.append(sum)
        res_e2.append(list(res))
    print(res_e2)   
        
    print('\nЗадание Е3')
    
    res_e3 = []
    for bk in books:
        res.clear()
        if (bk.name[0] == 'Д'):
            res = [bk.name, bb.name]
            res_e3.append(list(res))
    print(res_e3)        


if __name__ == '__main__':
    main()