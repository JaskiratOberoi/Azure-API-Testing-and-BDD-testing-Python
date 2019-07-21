from flask import Flask, render_template, request
from index import response, Database, responseRG, ResourceG

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/subId-home/')
def subscription_id():
    return render_template('template.html')


@app.route('/subId-api/', methods=['GET', 'POST'])
def print_response():
    status = request.form['status']

    print(response)
    for i in range(0, len(Database)):
        if Database[i]["state"] == status:
            print("Display Name of Subscription : " + Database[i]["displayName"])
            print("Subscription ID of Account : " + Database[i]["subscriptionId"])
            print("State of the Subscription [Enabled/Disabled] : " + Database[i]["state"])
    return render_template('result.html', displayName=Database[0]["displayName"], subscriptionId=Database[0]["subscriptionId"], state=Database[i]["state"])


@app.route('/rg-api/')
def resource_group_response():
    print(responseRG)
    for i in range(0, len(ResourceG)):
        print("Resource Group Name : " + ResourceG[i]["name"])
        print("Resource Group Location : " + ResourceG[i]["location"] + "\n")

    return render_template('RG_result.html', rgName1=ResourceG[0]["name"], rgName2=ResourceG[1]["name"], rgName3=ResourceG[2]["name"],
                           rgLocation1=ResourceG[0]["location"], rgLocation2=ResourceG[1]["location"], rgLocation3=ResourceG[2]["location"])



if __name__ == '__main__':
    app.run(debug=True)
