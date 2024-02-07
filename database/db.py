import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("imangali Database connected successfully")
        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        try:
          self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        except sqlite3.OperationalError:
           pass
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name)
            )
        self.connection.commit()

    def sql_insert_ban_user(self, tg_id):
         self.cursor.execute(
              sql_queries.INSERT_BAN_USER_QUERY,
              (None, tg_id, 1,)
         )
         self.connection.commit()

    def sql_select_ban_users(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'count': row[2],
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_count(self, tg_id):
         self.cursor.execute(
              sql_queries.UPDATE_BAN_USER_QUERY,
              (tg_id,)
         )
         self.connection.commit()
    def sql_insert_profile(self, tg_id, nickname, bio, age, sign, gender, year, photo):
         self.cursor.execute(
              sql_queries.INSERT_PROFILE_QUERY,
              (None, tg_id, nickname, bio, age, sign, gender, year, photo,)
         )
         self.connection.commit()
    def sql_select_profile(self, tg_id):
         self.cursor.row_factory = lambda cursor, row: {
             'id': row[0],
             'telegram_id': row[1],
             'nickname': row[2],
             'bio': row[3],
             'age': row[4],
             'sign': row[5],
             'gender': row[6],
             'year': row[7],
             'photo': row[8],
         }
         return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
         ).fetchone()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_insert_dislike(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker,)
        )
        self.connection.commit()
    def sql_select_all_profiles(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'sign': row[5],
            'gender': row[6],
            'year': row[7],
            'photo': row[8],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_QUERY,
            (owner, owner,)
        ).fetchall()

    def sql_select_all_dis_profiles(self, owner):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'sign': row[5],
            'gender': row[6],
            'year': row[7],
            'photo': row[8],
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_DIS_PROFILE_QUERY,
            (owner, owner,)
        ).fetchall()