from flask import Flask, request
from main import ladder

app = Flask("Ladder")

@app.route("/ladder", methods=["GET"])
def get_ladder():
    return ladder()
app.run()
