from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
  response = jsonify({"home":"home"})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

# @app.route("/about")
# def about():
#   return {"about":"about"}
if __name__ == "__main__":
  app.run(debug=True)