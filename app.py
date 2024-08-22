import random
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods = ["POST","GET"])
def form_submit_ui():

    your_name           = request.values.get("your_name")
    your_friend_name    = request.values.get("your_friend_name")
    friendship_meter = random.randint(20, 100)

    result_dict = {
        "your_name" : your_name,
        "your_friend_name" : your_friend_name,
        "friendship_meter" : friendship_meter
    }

    return render_template(
        'index.html',
        result = result_dict
    )


    
if __name__ == '__main__':
    


    app.run(host="0.0.0.0", debug = True, port = 8000)