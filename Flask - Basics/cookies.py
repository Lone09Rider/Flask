# from flask import Flask, render_template, redirect, request, url_for, make_response

# app = Flask(__name__)

# # CRETAE A COOKIE
# @app.route("/")
# def index():
#     cookie = make_response('Create Cookie')
#     cookie.set_cookie('name', "SRj", max_age=60)
#     return(cookie)

# # READ A COOKIE
# @app.route("/read")
# def read():
#     if request.cookies.get("name"):
#         cookie = make_response(f"Display Cookie : {request.cookies.get('name')}")
#     else:
#         cookie = make_response('Create Cookie')
#         cookie.set_cookie('name', "SRj", max_age=60*60)
#     return cookie

# # Delete Cookie
# @app.route('/delete')
# def delete():
#     cookie = make_response("Delete a Cookie")
#     cookie.set_cookie('name', "SRj", max_age=0)
#     return cookie

# if __name__ == "__main__":
#     app.run(debug=True)