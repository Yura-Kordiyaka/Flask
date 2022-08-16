from app import app
from models import *
from sqlalchemy import select
import json


def convert_all(list):
    l = []
    for i in list:
        l.append(i.serialize)
    return l


