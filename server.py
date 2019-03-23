# from flask import Flask, request, make_response, jsonify
# import json
# import requests

# app =Flask(__name__)

# @app.route('/',methods=['GET'])
# def respond():
#     name=request.args.get('name')
#     name={'Name':name}
#     return jsonify([name])
# @app.route('/webhook',methods=['POST'])
# def response():
#     name='ko'
#     name={'fulfillmentText':name}
#     return jsonify(name)
# if __name__ == '__main__':
# 	app.run()

from flask import Flask, request, make_response, jsonify
import json
import requests

app =Flask(__name__)

@app.route('/',methods=['GET'])
def respond():
    name=request.args.get('name')
    name={'Name':name}
    return jsonify([name])
@app.route('/webhook',methods=['POST'])
def response():
    req=request.get_json(silent=True,force=True)
    intent=req.get('queryResult').get('intent').get('displayName')
    if intent=='Default Welcome Intent':
        res={'fulfillmentText':'Hello'}
        return jsonify(res)
    elif intent=='number':
        num=req.get('queryResult').get('parameters').get('number')
        qtype=req.get('queryResult').get('parameters').get('type')
        num=int(num)
        url='http://numbersapi.com/'
        final_url=url+str(num)+'/'+qtype+'?json'
        res=requests.get(final_url)
        print(res)
        text= res.json()['text']
        
        return jsonify({'fulfillmentText':text})
    return jsonify({'fulfillmentText':'Po'})
if __name__ == '__main__':
	app.run()