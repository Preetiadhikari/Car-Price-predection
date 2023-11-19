from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route("/hello")
def get_fuelsystem_names():
    response = jsonify({"fuelsystem": util.get_fuelsystem_names()})
    return "hi"


if __name__ == "__main__":
    print("starting python flask server for carprice predection")
    app.run()
