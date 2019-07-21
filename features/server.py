from flask import Flask, render_template, request
from index import response, Database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template.html')


@app.route('/my-link/', methods=['GET', 'POST'])
def print_response():
    status = request.form['status']

    print(response)
    # state = input("Enter State of Subscription : ")
    for i in range(0, len(Database)):
        if Database[i]["state"] == status:
            print("Display Name of Subscription : " + Database[i]["displayName"])
            print("Subscription ID of Account : " + Database[i]["subscriptionId"])
            print("State of the Subscription [Enabled/Disabled] : " + Database[i]["state"])
    return render_template('result.html', displayName=Database[0]["displayName"], subscriptionId=Database[0]["subscriptionId"], state=Database[i]["state"])


if __name__ == '__main__':
    app.run(debug=True)
