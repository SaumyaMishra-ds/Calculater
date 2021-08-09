
from db1 import create_connection, execute_query
from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error


def insert_data(a, b, result):

    db = create_connection()
    # query = "insert into cal(First,Second,Addition,substraction,multiply,division) values({},{},{add},{sub},{mult},{div})".format(
    #     a, b, **result)
    # ctrl + /
    query = f"insert into cal(First,Second,Addition,substraction,multiply,division) values({a},{b},{result['add']},{result['sub']},{result['mult']}, {result['div']})"

    execute_query(db, query)
    # cur = db.cursor()

    # cur.execute(query)``

    # cur.close()
    # db.close()


def cal(a, b):
    data = {'add': int(a)+int(b), 'sub': int(a)-int(b),
            'mult': int(a)*int(b), 'div': int(a)/int(b)}
    return data


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    a = request.form.get('a')
    b = request.form.get('b')
    result = cal(a, b)

    insert_data(a, b, result)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
