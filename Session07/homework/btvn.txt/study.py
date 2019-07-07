from flask import Flask, render_template, redirect
app= Flask(__name__)
# Study
# Exercise 1: profile

@app.route("/about-me")
def profile():

    return render_template('profile.html',SCHOOL= school)

@app.route("/about-me/school")
def school():
    return redirect ('http://techkids.vn')




if __name__=="__main__":
    app.run(debug=True)