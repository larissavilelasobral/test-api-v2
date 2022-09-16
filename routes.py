from flask import Flask, request
from main import ladder

app = Flask("Ladder")

def __init__(self, ):
    @app.route("/ladder", methods=["GET"])
    def get_ladder():
        return ladder()

app.run()



