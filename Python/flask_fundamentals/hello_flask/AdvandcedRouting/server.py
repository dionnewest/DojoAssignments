from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>')
def show_user_profile(username):
	# print var
	print id
	return render_template("user.html",var = username)

# @app.route('/route/with/<vararg>')
# def handler_functions(vararg):
# 	print vararg
app.run(debug=True)