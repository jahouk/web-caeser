from flask import Flask, request, redirect
import cgi
from caeser import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="" method="POST">
        <label for="Rotate by">Rotate by:</label>
        <input type="text" name="rot" value="0" />
        <br />
         <textarea name="text">{0}</textarea> 
        <br />
        <input type="submit" value="Submit Query" />
      </form>
    </body>
</html>"""

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']
    output =  rotate_string(text, rot)
    return redirect("/?text=" + output)

@app.route("/")
def index():
    text = request.args.get('text')
    if text:
        text_element = cgi.escape(text, quote=True)
    else:
        text_element = ""
    
    return form.format(text_element)

app.run()