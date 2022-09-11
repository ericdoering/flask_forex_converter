from ast import Num
from crypt import methods
from curses import flash
from flask import Flask, render_template, get_flashed_messages, request, flash
from forex_python.converter import CurrencyRates

app = Flask(__name__)
app.secret_key = "currConvert717$"


@app.route("/", methods=['GET', 'POST'])
def convert_page():
    currA = request.args.get("from")
    currB = request.args.get("to")
    total = request.args.get("amount")


    valid_currency = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", 
    "SEK", "SGD", "HKD", "AUD", "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB",
    "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]


    invalid_currA = currA is not None and currA not in valid_currency
    invalid_currB = currB is not None and currB not in valid_currency


    if invalid_currA:
        flash('Please type in a valid currency for "Convert From"', "error")
    
    if invalid_currB:
        flash('Please type in a valid currency for "Convert To"', "error")

    if total is not None and not total.isnumeric():
        flash("Please type in a number value", "error")


    #For default rendering of the inital page before user inputs arguments
    if currA is None and currB is None and total is None:
        return render_template("convert_page.html")

    if invalid_currA is False and invalid_currB is False and total and total.isnumeric():
        total = int(total)
        converted = CurrencyRates().convert(currA, currB, total)
        return render_template("results_page.html", converted=converted)
    
    else: return render_template("convert_page.html", currA=currA, currB=currB, total=total)

    


