from myapplication import app

@app.route('/')
def index():
    return render