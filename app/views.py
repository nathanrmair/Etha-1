from app import app

import json

@app.route('/')
def homepage():
    return 'Hello world'

@app.route('/register',methods=['POST'])
def register():
    return json.dumps(
	    {
	        "status": "OK"
	    }
    )

@app.route('/passenger',methods=['POST'])
def passenger():
    return json.dumps(
	    {
	        "status": "OK"
	    }
    )

@app.route('/update',methods=['POST'])
def update():
    return json.dumps(
	    {
	        "status": "OK"
	    }
    )



