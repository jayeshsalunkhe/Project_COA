from flask import Flask,jsonify,request
from flask_cors import CORS
from vaibhav_assembler import assemblercode
from vaibhav_disassembler import disassemblercode

app = Flask(__name__)
CORS(app)
def assembleCode(text):
  return assemblercode(text,0)
def disassembleCode(text):
  return disassemblercode(text,0)

@app.route("/",methods=['GET'])
def home():
  print("home",request.data)
  response = jsonify({"home":"home"})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/assemble",methods=['POST'])
def assemble():
  print(request.get_json())
  response = jsonify( {'data':assembleCode(request.get_json()['data'])} )
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

@app.route("/disassemble",methods=['POST'])
def disassemble():
  print(request.get_json())
  response = jsonify( {'data':disassembleCode(request.get_json()['data'])} )
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

# @app.route("/about")
# def about():
#   return {"about":"about"}
if __name__ == "__main__":
  app.run(debug=True)