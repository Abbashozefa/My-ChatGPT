from flask import Flask,render_template,request
import openai
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv('api_key')


openai.api_key=api_key

# prompt=input("Ask ChatGPT:")






app=Flask(__name__)


@app.route("/",methods=['POST','GET'])
def home():
    if request.method == 'POST':
        prompt=str(request.form['msg'])
        response =openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=2000)   
    
        return response['choices'][0]["text"]
    else:
        return render_template('index.html')

# @app.route("/get",methods=['POST','GET'])
# def webhook():
#     prompt=str(request.form['msg'])
#     response =openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=2000)
      
    
#     return response['choices'][0]["text"]
    
    
    





if __name__  == "__main__":
    app.run(host='0.0.0.0',port=3000)
