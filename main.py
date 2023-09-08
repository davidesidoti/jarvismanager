#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


class JarvisManager:
    def __init__(self) -> None:
        pass

    def get_token(self):
        req = requests.request("POST", "http://127.0.0.1:8000/token", headers={
                               "accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}, data={"username": "sidotidavide@gmail.com", "password": "Hash37883788&"})
        return req

    def searchPWD(self, token, query: str = ""):
        req = requests.get(
            url=f"http://127.0.0.1:8000/password/search/?query={query}",
            headers={
                "accept": "application/json"
                ,"Authorization": f"Bearer {token}"
            }
        )
        return req


if __name__ == "__main__":
    manager = JarvisManager()
    token = manager.get_token().json()["access_token"]
    # print(manager.searchPWD(token, "instagram").json())
    if manager.searchPWD(token).json() and isinstance(manager.searchPWD(token).json(), list):
        for pwd in manager.searchPWD(token).json():
            print("==========")
            for key, value in dict(pwd).items():
                print(f"{key}: {value}")
    else:
        raise ValueError("searchPWD() must return a list.")
