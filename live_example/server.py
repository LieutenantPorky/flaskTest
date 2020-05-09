from flask import Flask, request

app = Flask(__name__)
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
        print(request.json)
        # user=request.json['user']
        # amount=request.json['amount']
        #
        # if user in users:
        #     users[user] += float(amount)
        #
        # print(user, amount)

    return "success"







if __name__ == "__main__":
    app.run(debug=True)
