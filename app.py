from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculate_score():
    if request.method == 'POST':
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        score = random.randint(50, 100)

        result = {
            'name1': name1,
            'name2': name2,
            'score': score
        }

        # Print the result for debugging (Vercel logs)
        print(f"result : {result}")

        return render_template("index.html", data=result)
    else:
        return render_template("index.html", data={})

if __name__ == '__main__':
    app.run(debug=True)