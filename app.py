from flask import Flask, render_template, request
from subprocess import Popen, PIPE

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/streamlit', methods=['POST'])
def run_streamlit():
    p = Popen(['streamlit', 'run', 'streamlit_app.py'], stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    return output

if __name__ == '__main__':
    app.run()
    