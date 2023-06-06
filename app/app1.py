from flask import Flask, request, render_template
import requests
import json

# app = Flask(__name__)
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')

@app.route('/',methods=['POST', 'GET'] )
def extract():
  # if request.method == "POST":
    text=str(request.form.get('text'))
    # text = "Malaria" #get user input and store it in this one
    payload = json.dumps({"sender": "Rasa","message": text})
    headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
    response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
    response=response.json()
    resp=[]
    for i in range(len(response)):
      try:
        resp.append(response[i]['text'])
      except:
        continue
    result=resp
    # l = []
    # l.append(text)
    # l.append(result[0])
    # return l
    if len(result)>0:
      return render_template('index.html', result=result[0],text=text)
    else:
      return render_template('index.html', result="Enter a query...",text=text)      
  # else:
  #   text = "None"
  #   return render_template('index.html', result="Enter a query",text=text)


if __name__ == '__main__':
    app.run(port=8000,debug=True)
