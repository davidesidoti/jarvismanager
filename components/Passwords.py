#!/usr/bin/python
# -*- coding: utf-8 -*-

from pymysql import connect, cursors
from passlib.context import CryptContext
from utilities.DBConnections import DBManager


class Passwords:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    db = DBManager()

    def __init__(self) -> None:
        pass

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def search_pwd(self, query: str):
        pwds = None

        try:
            if not query or query == "":
                pwds = self.db.query("SELECT * FROM passwords")
            else:
                pwds = self.db.query(
                    "SELECT * FROM `passwords` WHERE `name` LIKE '%{0}%' OR `url` LIKE '%{0}%' OR `user` LIKE '%{0}%'".format(query))
        except Exception as e:
            raise e

        return pwds
