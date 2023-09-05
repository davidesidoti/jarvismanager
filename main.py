#!/usr/bin/python
# -*- coding: utf-8 -*-

from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.route("/")
def root():
    return {"response": "Test"}
