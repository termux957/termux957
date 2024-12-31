from flask import Flask, render_template, request  # This should be at the top of the file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        balance = float(request.form["balance"])
        interest_rate = float(request.form["interest_rate"])
        monthly_payment = float(request.form["monthly_payment"])

        # Calculate debt payoff
        interest_rate = interest_rate / 100 / 12  # Monthly interest rate
        months = 0
        while balance > 0:
            balance = balance + balance * interest_rate - monthly_payment
            months += 1
            if balance < 0:
                break
        years = months // 12
        remaining_months = months % 12
        total_paid = monthly_payment * months

        return render_template(
            "result.html",
            years=years,
            remaining_months=remaining_months,
            total_paid=total_paid,
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # This should be on its own line
