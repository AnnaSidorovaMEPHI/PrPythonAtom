from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get_classifier_result/<version>", methods=['GET', 'POST'])
def return_classifier_result(version):
    #TODO прочитать из полученного запроса json-контент
    #В случае, если version==1, то должен вернуться json с версией и полем predict из входящего jsonа {"version":1, "predict":<predict_value>}
    #В случае, если version==0, то должен вернуться json с версией и полем old_predict из входящего jsonа {"version":0, "predict":<old_predict_value>}

    if request.method == 'POST':
        inputjson = request.json
        if version == '1':
            return jsonify({'version':1,'predict':inputjson['predict']})
        if version == '0':
            return jsonify({'version':0,'predict':inputjson['old_predict']})

@app.route("/")
def hello():
    #TODO должна возвращатьс инструкция по работе с сервером
    return "Введите json-контент. Сервер вернет json-контент с версией и полем predict/old_predict из входящего jsonа"

if __name__ == "__main__":
    app.run()
