from flask import Flask, render_template,redirect
app= Flask(__name__)
all_food=[
        {
        "title":"gà",
        "description":"bổ",
        "link":"https://image.giaoducthoidai.vn/Uploaded/tranghn/2019-05-15/kfc-2-ENDJ.jpg?width=500",
        "food_type":"food"
        },
        {
        "title":"nước cam",
        "description":"vitamin A",
        "link":"https://photo-1-baomoi.zadn.vn/w1000_r1/18/03/23/144/25384434/1_30467.jpg",
        "food_type":"drink"
        },
        {
        "title":"chÁO",
        "description":"k bổ",
        "link":"http://www.monngon.tv/uploads/images/images/cach-lam-chao-thit-bam.jpg",
        "food_type":"food"
        },
    ]

@app.route("/foods")
def all_food_fu():
  
       
    return render_template("all_food.html",FOOD = all_food)
    

@app.route("/foods/detail/<int:index>")
def food_detail(index):
   food_detail= (all_food[index])
   return render_template("food_detail.html",FOOD_DETAIL= food_detail)

@app.route("/foods/delete/<int:index>")
def delete_food(index):
    del all_food[index]
    return redirect('/foods')

@app.route("/tho")
def index():
    return render_template('poem.html')

if __name__=="__main__":
    app.run(debug=True)