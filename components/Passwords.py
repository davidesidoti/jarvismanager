#!/usr/bin/python
# -*- coding: utf-8 -*-

class Passwords:
    fake_pwd_db = {
        "social": {
            "instagram": {
                "url": "https://instagram.com/login",
                "user": "sidotidavide@gmail.com",
                "password": "InstaTest1234"
            },
            "tiktok": {
                "url": "https://tiktok.com/login",
                "user": "sidotidavide@gmail.com",
                "password": "TkTkTest1234"
            }
        },
        "games": {
            "riot": [
                {
                    "url": "https://riot.com/login",
                    "user": "sidotidavide@gmail.com",
                    "password": "ValoUnoTest1234"
                },
                {
                    "url": "https://riot.com/login",
                    "user": "d.sidoti@gmail.com",
                    "password": "ValoDueTest1234"
                }
            ],
            "steam": {
                "url": "https://steam.com/login",
                "user": "sidotidavide@gmail.com",
                "password": "SteamTest1234"
            }
        }
    }
    
    def __init__(self) -> None:
        pass
    
    def search_pwd(self, query: str):
        pass