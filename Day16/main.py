from flask import Flask
from flask_restful import Api , Resource
# from module.User import User

class PrintHelloWorld(Resource):
    def get(self):
        return {
            'message': 'Hello Wrold!'
        }, 200

class testAPI(Resource):
    def get(self):
        return {
            'message': 'Hello Wrold!'
        }, 200

users = []
class User (Resource):

    def get(self, name):
        find = [item for item in users if item['name'] == name]
        if len(find) == 0:
            return {
                'message': 'username not exist!'
            }, 403
        user = find[0]
        if not user:
            return {
                'message': 'username not exist!'
            }, 403
        return {
            'message': '',
            'user': user
        }

    def post(self, name):
        pass

    def put(self, name):
        pass

    def delete(self, name):
        pass

app = Flask(__name__)
api = Api(app)

api.add_resource(PrintHelloWorld, "/print_hello_world/")
api.add_resource(User, "/user/<string:name>")

if(__name__ == "__main__"):
  app.run(host='0.0.0.0', port=8080)








































# from flask import Flask, render_template, request , Response
# from random import choice
# import json

# web_site = Flask(__name__)

# number_list = [
# 	100, 101, 200, 201, 202, 204, 206, 207, 300, 301, 302, 303, 304, 305, 307, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
# 	416, 417, 418, 421, 422, 423, 424, 425, 426,
# 	429, 431, 444, 450, 451, 500, 502, 503, 504, 506, 507, 508, 509, 510, 511, 599
# ]

# @web_site.route('/')
# def index():
# 	return render_template('index.html')

# @web_site.route('/user/', defaults={'username': None})
# @web_site.route('/user/<username>')
# def generate_user(username):
# 	if not username:
# 		username = request.args.get('username')

# 	if not username:
# 		return 'Sorry error something, malformed request.'

# 	return render_template('personal_user.html', user=username)

# @web_site.route('/page')
# def random_page():
#   return render_template('page.html', code=choice(number_list))

# @web_site.route('/api')
# def indexapi():
#   t = {
#     "title":"welecome to python flask api example"
#   }
#   return Response(json.dumps(t), mimetype='application/json')

# web_site.run(host='0.0.0.0', port=8080)