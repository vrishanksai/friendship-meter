from flask import Flask, render_template, request
import random
import json
import os


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def calculate_score():
    
    if request.method == 'POST':
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        
        score = random.randint(50, 100)
        print(score)
        
        result = {
            'name1': name1,
            'name2': name2,
            'score': score
        }
        
        print(f"result : {result}")

        # Store result in JSON file
        json_file_path = 'friendship_data.json'
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r+') as file:
                data = json.load(file)
                data.append(result)
                file.seek(0)
                json.dump(data, file, indent=4)
        else:
            with open(json_file_path, 'w') as file:
                json.dump([result], file, indent=4)

        return render_template("index.html", data=result)
    else:
        return render_template("index.html", data={})

if __name__ == '__main__':
    app.run(debug=True)