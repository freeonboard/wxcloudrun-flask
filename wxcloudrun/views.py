from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')
        step = request.form.get('step')
        api_url = 'https://apis.jxcxin.cn/api/mi'
        params = {'user': user, 'password': password, 'step': step}
        response = requests.get(api_url, params=params)
        result = response.text
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(0.0.0.0)
