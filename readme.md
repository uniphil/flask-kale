Flask-kale
==========


[![Build Status](https://travis-ci.org/uniphil/flask-kale.png)](https://travis-ci.org/uniphil/flask-kale)


```python
>>> from pymongo import MongoClient
>>> from flask import Flask
>>> from flask.ext.kale import Kale
>>> connection = MongoClient()
>>> app = Flask(__name__)
>>> kale = Kale(app)
>>> @kale.dbgetter
... def get_db():
...     return connection.test
... 
>>> class Unicycle(kale.Model):
...     _collection_name = 'unicycles'
... 
>>> my_road = Unicycle(brand='Kris Holm', size=36, cranks=100, handlebar=True)
>>> my_road.save()
ObjectId('5205b271b50a1a04c7ec52b4')
>>> my_beater = Unicycle(brand='Bedford', size=24, cranks=150)
>>> my_beater.save()
ObjectId('5205b29bb50a1a04c7ec52b5')
>>> my_dream = Unicycle(brand='Custom', size=54, cranks=125, v_frame=True)
>>> my_dream.save()
ObjectId('5205b2edb50a1a04c7ec52b6')
>>> for uni in Unicycle.collection.find({'size': {'$gte': 36}}):
...     print '{} {}, crank ratio {:.2g}'.format(uni.brand, uni.size, (uni.size / 2.0 * 25.4 / uni.cranks))
... 
Kris Holm 36, crank ratio 4.6
Custom 54, crank ratio 5.5
```

```python
>>> from flask import Flask
>>> from flask.ext.pymongo import  PyMongo
>>> from flask.ext.kale import Kale
>>> 
>>> app = Flask(__name__)
>>> 
>>> mongo = PyMongo()
>>> 
>>> kale = Kale()
>>> 
>>> @kale.dbgetter
... def get_mongodb():
...     return mongo.db
... 
>>> 
>>> class User(kale.Model):
...     _collection_name = 'users'
...     def get_id(self):
...             return str(self._id)
... 
>>> 
>>> mongo.init_app(app)
>>> kale.init_app(app)
>>> 
>>> with app.test_request_context():
...     phil = User()
...     phil.name = 'Phil'
...     phil.username = 'uniphil'
...     phil.password = 'lalala'
...     phil.save()
... 
ObjectId('5205b89db50a1a07a1d8b088')

```
