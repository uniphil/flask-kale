# -*- coding: utf-8 -*-
"""
    test_flask_kale
    ~~~~~~~~~~~~~~~

    lalala

    :copyright: uniphil 2013
    :license: dwtfyw with optional coffee stipulation (one large dark black)
"""


import unittest
from pymongo import MongoClient
from flask import Flask
import flask_kale


class test_flask_kale(unittest.TestCase):

    def test_basic(self):
        app = Flask('test')
        kale = flask_kale.Kale(app)
        @kale.dbgetter
        def get_database():
            connection = MongoClient()
            return connection.test
        class Fruit(kale.Model):
            _collection_name = 'fruit'
        apple = Fruit(name='my red apple')
        apple.save()
