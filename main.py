#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

class JarvisManager:
    def __init__(self) -> None:
        pass
    
    def get_token(self):
        req = requests.request("POST", "http://127.0.0.1:8000/token", headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}, data={"username": "hash", "password": "secret"})
        return req
    
    def searchPWD(self):
        req = requests.request("GET", "http://127.0.0.1:8000/password/search/?query=riot", headers={"accept": "application/json"})
        return req

if __name__ == "__main__":
    manager = JarvisManager()
    print(manager.get_token().text)
    print(manager.searchPWD().text)