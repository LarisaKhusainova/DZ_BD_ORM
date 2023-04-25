
def delete_table(con):
    with con.cursor() as cur:
        cur.execute("""
            DROP TABLE if exists sale cascade;
            """)
        cur.execute("""
            DROP TABLE if exists stock cascade;
            """)
        cur.execute("""
            DROP TABLE if exists book cascade;
            """)
        cur.execute("""
            DROP TABLE if exists shop cascade;
            """)
        cur.execute("""
            DROP TABLE if exists publisher cascade;
            """)



def create_db(conn):
    with conn.cursor() as cur:
        # delete_table(conn)
        cur.execute("""
            create table if not exists publisher (
            id serial primary key,
            name varchar(50) not null);
            """)
        cur.execute("""
            create table if not exists shop (
            id serial primary key,
            name varchar(50) not null);
            """)
        cur.execute("""
            create table if not exists book(
            id serial primary key,
            id_publisher Integer not null references publisher(id) on delete cascade on update cascade,
            title varchar(40) not null);
            """)
        cur.execute("""
            create table if not exists stock(
            id serial primary key,
            id_book Integer not null references book(id) on delete cascade on update cascade,
            id_shop Integer not null references shop(id) on delete cascade on update cascade,
            count Integer);
            """)
        cur.execute("""
            create table if not exists sale(
            id serial primary key,
            price float not null,
            date_sale date not null,
            id_stock Integer not null references stock(id) on delete cascade on update cascade,
            count Integer);
            """)
        conn.commit()
    print("БД cоздана")


# def add_client(conn, first_name, last_name, email, phone=None):
#     with conn.cursor() as cur:
#         if find_client(conn, email=email):  # Ищем клиента с таким имейлом
#             return "Данный email уже существует "  # Сообщаем пользователю, что клиент с таким имейлом уже есть
#
#         cur.execute("""
#             INSERT INTO clientTb (name,fam,email) VALUES (%s,%s,%s) RETURNING id;
#         """, (first_name,last_name,email))
#         conn.commit()
#         if phone:  # Проверяем передали ли телефон при добавлении контакта
#             client_id = cur.fetchone()  # получаем из запроса идентификационный номер и сохраняем в переменную
#             add_rez = add_phone(conn, client_id, phone)  # Вызываем функцию добавления номера телефона и рузультат сохраняем в переменную
#             if add_rez == 'Номер телефона уже зарегистрирован':  # Проверяем вернулось ли сообщение, которое равно тому, что сообщает о существовании номера
#                 conn.rollback()  # Отменяем создание клиента
#                 return "Добавление невозможно"  # Сообщаем что добавить невозможно
#         conn.commit()  # Делаем коммит у соединения
#         return "Добавление клиента произведено"  # Сообщаем что клиент добавлен
#
# def add_phone(conn, client_id: int, phone):
#     with conn.cursor() as curs:
#         if find_client(conn, phone=phone): #Ищем клиента с таким имейлом
#             return "Номер телефона уже зарегистрирован" #Соообщаем что такой номер есть
#         curs.execute(
#             """
#             SELECT clienttb.id from clienttb WHERE clienttb.id = %s;
#             """,
#             (client_id,) #Передаем id клиента
#         )
#         if not curs.fetchone(): #Проверяем вернулась ли пустая коллекция
#             return "Клиент с указанным ID не найден" #Соообщаем что такого клиента нет
#         curs.execute(
#             """
#             INSERT INTO teltb (id_cl, tel) VALUES (%s, %s);
#             """,
#             (client_id, phone)
#         )
#         conn.commit() #Подтверждаем изменения
#     return "Номер телефона добавлен" #Возвращаем сообщение об успехе
#
# def add_client_phone(conn, first_name, last_name, email, phone):
#     with conn.cursor() as cur:
#         cur.execute("""
#             INSERT INTO clientTb (name,fam,email) VALUES (%s,%s,%s) RETURNING id;
#         """, (first_name,last_name,email))
#         conn.commit()
#         client_id=cur.fetchone()
#         if phone is not None:
#             add_phone(conn, client_id, phone)
#
# def change_client(conn, client_id, first_name=None, last_name=None, email=None):
#         # pass
#         with conn.cursor() as cur:
#             cur.execute(
#                 """
#                 SELECT clienttb.name, clienttb.fam, clienttb.email,clienttb.id FROM clienttb
#                 WHERE clienttb.id = %s;
#                 """,
#                 (client_id,)  # Передаем id клиента
#             )
#             sel_rez = cur.fetchone()  # Получаем данные пользователя в виде кортежа из запроса и сохраняем в переменную
#             if not sel_rez:  # Если селект данные не вернул, то проваливаемся в блок
#                 return "Такого клиента не существует"  # Сообщаем, что такого пользователя нет
#             if first_name is None:  # Если имя пустое, то проваливаемся в блок
#                 first_name = sel_rez[0]  # Изменяем имя клиента на значение из кортежа, который вернулся из запроса
#             if last_name is None:  # Если фамилия пустая, то проваливаемся в блок
#                 last_name = sel_rez[1]  # Изменяем фамилию клиента на значение из кортежа, который вернулся из запроса
#             if email is None:  # Если почта пустая, то проваливаемся в блок
#                 email = sel_rez[2]  # Изменяем почту клиента на значение из кортежа, который вернулся из запроса
#             cur.execute(
#                 """
#                 UPDATE clienttb
#                 SET name = %s, fam = %s, email = %s
#                 WHERE id = %s;
#                 """,
#                 (first_name, last_name, email, client_id)
#             )
#             conn.commit()
#         return "Пользователь успешно изменен"
#
# def delete_phone(conn, client_id, phone=None):
#     with conn.cursor() as cur:
#         del_str="""
#             DELETE FROM teltb WHERE telTb.id_cl = %s AND teltb.tel = %s RETURNING id_cl, tel;
#             """
#         cur.execute(del_str, (client_id,phone))
#         if not cur.fetchone():  # Проверяем не пустая ли коллекция вернулась
#             return "Указанные для удаления данные не найдены"  # Возвращаем сообщение что такого номера нет
#         conn.commit()
#         return "Удаление телефона ", phone, "произведено успешно"  # Сообщаем об успешной операции
#
# def delete_client(conn, client_id):
#     with conn.cursor() as cur:
#         del_str1 = """
#             DELETE FROM clienttb WHERE clienttb.id = %s RETURNING id;
#             """
#         cur.execute(del_str1, (client_id,))
#         if not cur.fetchone():  # Проверяем не пустая ли коллекция вернулась
#             return "Указанные для удаления данные не найдены"  # Возвращаем сообщение что такого номера нет
#         conn.commit()
#         return "Удаление клиента с ID=",str(client_id), "произведено успешно"  # Сообщаем об успешной операции
#
# def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
#     print("Поиск для: ", first_name, last_name, email, phone)
#
#     with conn.cursor() as curs:
#         if first_name is None:  # Если имя не было передано
#             first_name = '%'  # Определяем новое значение, которое означает, что здесь может быть любая строка
#         if last_name is None:  # Если фамилия не была передана
#             last_name = '%'  # Определяем новое значение, которое означает, что здесь может быть любая строка
#         if email is None:  # Если почта не была передана
#             email = '%'  # Определяем новое значение, которое означает, что здесь может быть любая строка
#         param1 = [first_name, last_name, email]  # Создаем список из имени, фамилии и почты
#         new_str = ''  # Определяем переменную с пустой строкой. Далее эта строка будет вставляться в тело запоса.
#         if phone:  # Если телефон содержит значение
#             new_str = ' AND teltb.tel= %s::text'  # Присваиваем переменной, которую определили через строку выше,
#             # новое значение с условием поиска телефона.Вместо первых точек указываем столбец с номерами из таблицы номеров.
#         # else:
#         #     phone='%'
#             param1.append(phone)  # Добавляем в ранее созданный список телефон, который передали в функцию.
#         select_str = f"""
#                 SELECT
#                     clientTb.name, clientTb.fam, clientTb.email,
#                     CASE
#                         WHEN ARRAY_AGG(teltb.tel) = '{{Null}}' THEN ARRAY[]::TEXT[]
#                         ELSE ARRAY_AGG(teltb.tel)
#                     END phones
#                 FROM clientTb
#                 LEFT JOIN telTb ON clientTb.id = telTb.id_cl
#                 WHERE clientTb.name ILIKE %s AND clientTb.fam ILIKE %s AND clientTb.email ILIKE %s{new_str}
#                 GROUP BY clientTb.name,clientTb.fam, clientTb.email;
#                 """
#         curs.execute(select_str, param1)  # Передаем список или кортеж с значениями
#         qw = curs.fetchall()
#         print(qw)
#
#     return qw
#
