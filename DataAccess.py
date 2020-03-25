from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
client = MongoClient('mongodb+srv://admin:password#@cluster0-hyofa.mongodb.net/test?retryWrites=true&w=majority')

class dao():

    def getClient(self):
        return MongoClient('mongodb+srv://admin:password#@cluster0-hyofa.mongodb.net/test?retryWrites=true&w=majority')

    def getCollection(self, database, collection):
        return dao().getClient().get_database(database).get_collection(collection)

    def getSection(self, database, collection):
        return dao().serializeResult(dao().getClient().get_database(database).get_collection(collection).find())

    def postNews(self, article):
        try:
            dao().getCollection('WellNessOne', 'WellNessNews').insert({'date': datetime.datetime.today(), 'article': article})
        except:
            print('Data access exception')

    def editArticle(self, _id, article):
        try:
            dao().getCollection('WellNessOne', 'WellNessNews').update_one({"_id": ObjectId(_id)},{"$set": {"article": article}})
        except:
            print('Data access exception')

    def serializeResult(self, daoResult):
        result = []
        for x in daoResult:
            obj = {}
            for y in x:
                if y == '_id':
                    obj['_id'] = str(x[y])
                else:
                    obj[y] = x[y]
            result.append(obj)
        return result


