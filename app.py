from flask import Flask, render_template, request, url_for

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



# hello
@app.route("/submit", methods=['POST'])
def submit():
    simple_interest=''
    if request.method== 'POST' and 'Principal' in request.form and 'Rate' in request.form and 'Time' in request.form: 
        Principal=float(request.form.get('Principal'))
        Rate=float(request.form.get('Rate'))
        Time=float(request.form.get('Time'))
        simple_interest= round((Principal*Time*Rate*0.01),2)     
    else:
        pass
    return render_template("index.html", Principal=Principal, Rate=Rate, Time=Time,simple_interest = simple_interest)



@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/calc", methods=['POST'])
def calc():
    compound_interest=''
    Amount=''
    if request.method== 'POST' and 'Principal1' in request.form and 'InterestRate' in request.form and 'NoTimes' in request.form and 'Time1' in request.form: 
        Principal1=float(request.form.get('Principal1'))
        InterestRate=float(request.form.get('InterestRate'))
        Time1=float(request.form.get('Time1'))
        NoTimes=int(request.form.get('NoTimes'))
        Amount=round((Principal1*(1+(InterestRate*0.01)/NoTimes)**(Time1*NoTimes)), 2)
        compound_interest=round((Amount-Principal1), 2)
    else:
        pass
    return render_template("home.html", Principal1=Principal1, InterestRate=InterestRate,Time1=Time1, NoTimes=NoTimes, Amount=Amount, compound_interest = compound_interest)

    




if __name__=='__main__':
    app.run(debug = True)
