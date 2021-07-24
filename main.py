from typing import Optional
import starlette.responses as _responses
from fastapi import FastAPI, File, UploadFile
import json
#import pandas as pd


with open('df_new0.json') as data_file:
    data0 = json.load(data_file)
with open('df_new1.json') as data_file:
    data1 = json.load(data_file)
with open('df_new2.json') as data_file:
    data2 = json.load(data_file)
with open('df_new3.json') as data_file:
    data3 = json.load(data_file)
with open('df_new4.json') as data_file:
    data4 = json.load(data_file)
with open('df_new5.json') as data_file:
    data5 = json.load(data_file)
with open('df_new6.json') as data_file:
    data6 = json.load(data_file)
with open('df_new7.json') as data_file:
    data7 = json.load(data_file)
with open('df_new8.json') as data_file:
    data8 = json.load(data_file)
with open('df_new9.json') as data_file:
    data9 = json.load(data_file)

app = FastAPI()

@app.get('/')
async def root():
    return _responses.RedirectResponse("/redoc")
@app.get("/data/data1")
def read_data():
        return data0
@app.get("/data/data2")
def read_data():
        return data1
    
@app.get("/data/data3")
def read_data():
        return data2
    
@app.get("/data/data4")
def read_data():
        return data3

@app.get("/data/data5")
def read_data():
        return data4

@app.get("/data/data6")
def read_data():
        return data5

    
@app.get("/data/data7")
def read_data():
        return data6

    
@app.get("/data/data8")
def read_data():
        return data7

@app.get("/data/data9")
def read_data():
        return data8
    
@app.get("/data/data10")
def read_data():
        return data9

# with open('data_test.json') as data_file:
#     data_1 = json.load(data_file)



# @app.get("/data/{data_id}")
# def read_data(data_id: int):
#     return {"data_id": data_id}
#     elif data == 2:
#         return {"data_id": data_id}
#     elif data == 3:
#         return {"data_id": data_id}