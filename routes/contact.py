from flask import Blueprint,request,jsonify
from utils.email import send_email

contact_bp=Blueprint("contact",__name__)

@contact_bp.route("/contact",methods=["POST"])
def contact():

 message=request.json["message"]

 send_email(message)

 return jsonify({"status":"sent"})