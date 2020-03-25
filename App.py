from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import datetime
from DataAccess import dao
app = Flask(__name__)
CORS(app, allow_headers='Content-Type')
app.config["DEBUG"] = True
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getSection', methods=['POST'])
@cross_origin()
def getSection():
    print('hi, this was reached')
    req = request.get_json()
    result = dao().getSection(req['Database'], req['Collection'])
    return jsonify({'result': result})

@app.route('/postNews', methods=['POST'])
@cross_origin()
def postNews():
    req = request.get_json()
    dao().postNews(req['article'])
    # collection = dao().getCollection('WellNessOne','WellNessNews')
    # collection.insert({'date': datetime.datetime.today(), 'article': req['article']})
    return jsonify('this worked')

@app.route('/editArticle', methods=['POST'])
@cross_origin()
def editArticle():
    req = request.get_json()
    dao().editArticle(req['_id'], req['article'])
app.run()