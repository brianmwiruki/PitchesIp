from flask import render_template
@app.route('/')
def index():
    title = "4Real"
return render_template(title = title)