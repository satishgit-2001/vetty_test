import os
import sys
from flask import Flask, render_template

app = Flask(__name__)


#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route('/')
@app.route('/<string:fname>/')
@app.route('/<string:fname>/<int:sln>/<int:eln>')
def fileread(fname=None, sln=None, eln=None):
    if not fname:
        fname = 'file1.txt'
    filepath = os.path.join("Jrpythondev/",fname)
    try:
        with open(filepath,'r',  encoding="cp437", errors='ignore') as fh:
            lines = fh.readlines()
            if (sln and eln):
                lines = lines[sln:eln+1]
    except Exception as e:
        response = exception_handler(exception=e, error=500)
        return response

    return render_template('filecontent.html', lines=lines)


def exception_handler(exception, error):
    message = "{}  --  {}".format(error, f"{repr(exception)}")
    return render_template('PageNotFound.html', message=message)

if __name__ == '__main__':
    app.run()
