from flask import Flask, request

app = Flask(__name__)
app.debug = True

weekly_budgets = {"Bob":24}

@app.route("/getBudget", methods=["POST"])
def update():
    user = request.json["id"]
    if user in weekly_budgets:
        return str((weekly_budgets[request.json["id"]]))
    else:
        return "User not found"



# @app.route("/update/<int:id>/<int:newBudget>")
# def update(id, newBudget):
#     weekly_budgets[id] = newBudget
#     return("Hello user " + str(id) + ", we have updated your budget to: " + str(weekly_budgets[id]))
#
#
# @app.route("/test/<int:id>")
# def homepage(id):
#     return("Hello user " + str(id) + ", your budget for this week is: " + str(weekly_budgets[id]))


if __name__ == "__main__":
    app.run(debug=True)
