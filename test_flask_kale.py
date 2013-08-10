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


class TestDB(object):
    """Get a database and make sure we clean up"""
    def __init__(self, db_name='test_flask_kale'):
        self.db_name = db_name

    def __enter__(self):
        self.cx = MongoClient()
        self.db = self.cx[self.db_name]
        return self.db

    def __exit__(self, type, value, traceback):
        self.cx.drop_database(self.db_name)


class test_flask_kale(unittest.TestCase):

    def test_basic(self):
        with TestDB() as db:
            app = Flask('test')
            kale = flask_kale.Kale(app)

            @kale.dbgetter
            def get_database():
                return db

            class Fruit(kale.Model):
                _collection_name = 'fruit'

            Fruit(name='apple').save()

    def test_init_app(self):
        with TestDB() as db:
            app = Flask('test')
            kale = flask_kale.Kale()
            kale.dbgetter(lambda: db)
            class Fruit(kale.Model): _collection_name = 'fruit'
            apple = Fruit(name='apple')
            kale.init_app(app)
            apple.save()

    def test_app_factory(self):
        with TestDB() as db:
            def make_app():
                return Flask('test')
            kale = flask_kale.Kale()
            kale.dbgetter(lambda: db)
            class Fruit(kale.Model): _collection_name = 'fruit'
            apple = Fruit(name='apple')
            app = make_app()
            kale.init_app(app)
            apple.save()

    def test_no_database(self):
        with TestDB() as db:
            kale = flask_kale.Kale(Flask('test'))
            class Fruit(kale.Model): _collection_name = 'fruit'
            apple = Fruit(name='apple')
            with self.assertRaises(NotImplementedError):
                apple.save()

    def test_kale_basics(self):
        """Not-comprehensive sanity check that kale still works like kale."""
        with TestDB() as db:
            kale = flask_kale.Kale(Flask('test'))
            kale.dbgetter(lambda: db)
            
            class Fruit(kale.Model):
                _collection_name = 'fruit'

            apple = Fruit(name='apple', colour='red')
            apple_ref = apple.save()
            loaded_apple = Fruit.collection.find_one(apple_ref)
            self.assertIs(loaded_apple, apple)
            apple.remove()
            loaded_nothing = Fruit.collection.find_one()
            self.assertIs(loaded_nothing, None)
