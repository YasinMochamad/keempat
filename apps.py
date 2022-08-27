from urllib import response
from flask import Flask,request
from flask_restful import Resource,Api
from flask_cors import CORS

app=Flask(__name__)
api=Api(app)
CORS(app)

identitas={}

class ContohResorce(Resource):
  def get(self):
    #response={"msg":"hallo dunia ini adalah restfull pertamaku"}
    return identitas

  def post(self):
    nama=request.form["nama"]
    umur=request.form["umur"]
    identitas["nama"]=nama
    identitas["umur"]=umur
    response={"msg":"sukses di masukkan bos"}
    return response



api.add_resource(ContohResorce,"/api",methods=["GET","POST"])


if __name__ == "__main__":
    app.run(debug=True,port=5001)


