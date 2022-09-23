import psycopg2
from psycopg2 import OperationalError
from db_config import config


class DB:
    _instance = None

    def __init__(self, data: dict):
        self.con = self.connect(data)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return f'{self.con}'

    @staticmethod
    def connect(config: dict):
        connection = None
        try:
            connection = psycopg2.connect(
                database=config['db_name'],
                user=config['db_user'],
                password=config['db_password'],
                host=config['db_host'],
                port=config['db_port'],
            )
        except OperationalError as e:
            return e
        return connection

    def execute_query(self, query):
        self.con.autocommit = True
        cursor = self.con.cursor()
        try:
            cursor.execute(query)
        except OperationalError as e:
            return e

    def execute_select_query(self, query):
        cursor = self.con.cursor()
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            return res
        except OperationalError as e:
            return e


con = DB(config)
create_publisher = '''create table if not exists publishers(id serial primary key, publisher_name varchar(80) unique)'''
con.execute_query(create_publisher)
create_genre = '''create table if not exists genres(id serial primary key, genre_name varchar(80) unique)'''
con.execute_query(create_genre)
create_books = '''  create table if not exists books(id serial primary key, title varchar(80) unique,
                    genre_id int references genres,
                    publisher_id int references publishers,
                    publication_year int,
                    available_amount int)'''
con.execute_query(create_books)

insert_publishers = ''' insert into publishers(publisher_name) values ('ЭКСМО');
                        insert into publishers(publisher_name) values ('ДРОФА');
                        insert into publishers(publisher_name) values ('АСТ');'''
con.execute_query(insert_publishers)
insert_genres = '''     insert into genres(genre_name) values ('Роман');
                        insert into genres(genre_name) values ('Приключения');
                        insert into genres(genre_name) values ('Поэзия');'''
con.execute_query(insert_genres)
insert_genres = '''     insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                        values ('Мастер и Маргарита', 1, 2, 2014, 5);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Таинственный остров', 2, 2, 2015, 10);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Бородино', 3, 3, 2015, 12);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Дубровский', 1, 2, 2020, 7);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Вокруг света за 80 дней', 2, 2, 2019, 5);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Убийства по алфавиту', 1, 1, 2017, 9);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Затерянный мир', 2, 1, 2020, 3);
                        insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Герой нашего времени', 1, 3, 2017, 2);
                         insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Смерть поэта', 3, 3, 2020, 2);
                         insert into books(title, genre_id, publisher_id, publication_year, available_amount)
                         values ('Поэмы', 3, 3, 2019, 5);'''
con.execute_query(insert_genres)

select_everything = ''' select title as Name, genre_name as Genre, publisher_name as Publisher,
                        publication_year as Year, available_amount as Amount
                        from books b, genres g, publishers p
                        where b.genre_id = g.id
                        and b.publisher_id = p.id'''
print(con.execute_select_query(select_everything))

a, b = 3, 7
select_first = f'''  select title, genre_name, available_amount from books b, genres g where
                     b.genre_id = g.id and b.available_amount >= {a}
                     and b.available_amount <= {b}
                     '''
print(con.execute_select_query(select_first))

year = 2018
select_second = f'''select title, publisher_name, available_amount from books b, publishers p
                    where b.publisher_id = p.id
                    and b.publication_year > {year}
                    and position(' ' in b.title) = 0
                    '''
print(con.execute_select_query(select_second))

select_third = f''' select genre_name, count(*) from books b, genres g
                    where b.genre_id = g.id and b.publication_year > {year}
                    group by genre_name
                    '''
print(con.execute_select_query(select_third))