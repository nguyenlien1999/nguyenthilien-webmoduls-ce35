from flask import Flask
app= Flask(__name__)

@app.route('/bmi/<float:weight>/<float:height>')
def BMI(weight,height):
    bmi = weight/(height/100)*2
    if bmi<16:
        return str(bmi) +'Severely underweight'
    elif 16<= bmi<18.5: 
        return str(bmi)+ 'Underweight'
    elif 18.5 <=bmi and bmi < 25: 
        return str(bmi)+ 'Normal'
    elif  25 <= bmi and bmi < 30: 
        return str(bmi)+ 'Overweight'
    else:
        return str(bmi)+ 'Obese'


if __name__=="__main__":
    app.run(debug=True)