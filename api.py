from flask import Flask
from flask_restful import Resource, Api, reqparse
from flaskext.mysql import MySQL

app = Flask(__name__)
api = Api(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "root's password"
app.config['MYSQL_DATABASE_DB'] = 'flasktest'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('username', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['username']
            _password = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_user', (_userEmail, _userName, _password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {
                    'StatusCode': '200',
                    'Message': 'User created'
                }
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

            # return {
            #     'email': _userEmail,
            #     'username': _userName,
            #     'password': _password
            # }
        except Exception as e:
            return {'error': str(e)}
        return {'status': 'success'}


api.add_resource(CreateUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)


