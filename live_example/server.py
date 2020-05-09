from flask import Flask, request, render_template

app = Flask(__name__, static_folder="./static", static_url_path='/static')
app.debug = True

users = {
"Bob":0,
"Bill":0
}

@app.route("/viewAll")
def viewBudgets():
    result = ""
    for key in users:
        result = result + key + ": " + str(users[key]) + "\n"
    return result

# print(viewBudgets())

@app.route("/updateBudget", methods=['GET','POST'])
def updateBudget():

    if request.method == 'POST':
        print(request.form)
        user=request.form['user']
        amount=request.form['amount']

        if user in users:
            users[user] += float(amount)

        print(user, amount)

    return render_template("form.html")








if __name__ == "__main__":
    app.run(debug=True)
