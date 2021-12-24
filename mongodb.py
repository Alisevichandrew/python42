#Frame_work_mongoDB
from flask_pymongo import PyMongo # импорт Flask и Flask-PyMongo в наше приложение
import flask
app = flask.Flask(__name__) # создадим объект приложения Flask
mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db") # связь приложения с экземпляром MongoDB
db = mongodb_client.db
app.config["MONGO_URI"] = "mongodb://localhost:27017/todo_db" #Строка URI также может быть назначена ключу в MONGO_URIapp.config
mongodb_client = PyMongo(app)
db = mongodb_client.db
@app.route("/add_one") #Таким образом, чтобы вставить новую сущность, мы сделаем что-то вроде
def add_one():
    db.todos.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")
# Мы также можем добавить несколько записей одновременно с помощью метода. 
# Метод берет список словарей и добавляет их в коллекцию:db.colection.insert_many()insert_many()
@app.route("/add_many")
def add_many():
    db.todos.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return flask.jsonify(message="success")

# Если мы хотим вставить в наш список только допустимые и уникальные записи, нам придется установить параметр метода, 
# а затем поймать исключение:orderedinsert_many()falseBulkWriteError
from pymongo.errors import BulkWriteError

@app.route("/add_many")
def add_many():
    try:
        todo_many = db.todos.insert_many([
            {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
            {'_id': 8, 'title': "todo title two", 'body': "todo body two"},
            {'_id': 2, 'title': "todo title three", 'body': "todo body three"},
            {'_id': 9, 'title': "todo title four", 'body': "todo body four"},
            {'_id': 10, 'title': "todo title five", 'body': "todo body five"},
            {'_id': 5, 'title': "todo title six", 'body': "todo body six"},
        ], ordered=False)
    except BulkWriteError as e:
        return flask.jsonify(message="duplicates encountered and ignored",
                             details=e.details,
                             inserted=e.details['nInserted'],
                             duplicates=[x['op'] for x in e.details['writeErrors']])

    return flask.jsonify(message="success", insertedIds=todo_many.inserted_ids)
    


