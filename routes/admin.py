from flask import Blueprint,jsonify

admin_bp=Blueprint("admin",__name__)

@admin_bp.route("/admin/messages")

def messages():

 return jsonify([
  {"message":"Test message"}
 ])