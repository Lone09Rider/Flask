# from flask import request, Flask, session, render_template, url_for, make_response, redirect

# app = Flask(__name__)

# app.config['SECRET_KEY'] = "SRj"

# # CREATE A SESSION
# @app.route('/')
# def base():
#     if 'hits' in session:
#         session['hits'] = session.get('hits') + 1
#     else:
#         session['hits'] = 1
#     return f"Total time site visited: {session.get('hits')}"

# # DELETE A SESSION
# @app.route('/delete')
# def delete():
#     session.pop('hits', None)
#     return "Session Deleted"

# if __name__ == "__main__":
#     app.run(debug=True)