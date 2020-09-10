import os
import sys
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Home page'


@app.route('/serve_file')
def fileread():
    fname = request.args.get('filename', type=str)
    sln = request.args.get('startline', type=int)
    eln = request.args.get('endline', type=int)

    if not fname:
        fname = 'file1.txt'
    filepath = os.path.join("Jrpythondev/",fname)
    encode = "utf-8"
    if fname == 'file4.txt' or fname == 'file2.txt':
        encode = "utf-16"
    
    try:
        with open(filepath,'r',  encoding=encode, errors='ignore') as fh:
            lines = fh.readlines()
            linecount = len(lines)
            if (sln and eln):
                if (sln >= linecount or eln >= linecount):
                    raise ValueError("Invalid arguments, start line number, end line number should be within line count") 
                if(sln <= eln):
                    lines = lines[sln:eln+1]
                else:
                   raise ValueError("Invalid arguments, start line number should be less than end line number")
    except Exception as e:
        response = exception_handler(exception=e, error=500)
        return response

    context = {"lines":lines, "filename":fname}
    return render_template('filecontent.html', context=context)


def exception_handler(exception, error):
    message = dict()
    message['msg'] = "{}".format(f"{repr(exception)}")
    message['error'] = "{}".format(error)
    return render_template('PageNotFound.html', message=message)

if __name__ == '__main__':
    app.run()
