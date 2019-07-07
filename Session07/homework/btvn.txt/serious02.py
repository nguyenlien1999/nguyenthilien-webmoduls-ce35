from flask import Flask,render_template
app= Flask(__name__)
users={
    
    "lien":         {
			"name": "Nguyen Thi Lien",
			"age":  19
       },
    "huy" :         {
			"name" : "Nguyen Quang Huy",
			"age" : 29
       },
    "tuananh": {
			"name" : "Nguyen Tuan Anh",
			"age" : 29
       }
}
@app.route('/user/<username>')
def info(username):
    if username in users:
        user = users[username]
        return render_template('user.html', USER = user)
    else:
        return 'User not found'



if __name__=="__main__":
    app.run(debug=True)