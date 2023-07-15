from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

@app.template_filter('format_time')
def format_time(dt):
    return "#" + dt.strftime('%H%M%S')

@app.template_filter('format_time_regular')
def format_time(dt):
    return dt.strftime('%H:%M:%S')

if __name__ == '__main__':
    app.run()
