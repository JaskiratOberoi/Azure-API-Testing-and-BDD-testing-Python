from behave import *
import requests
import index


@given('we have a valid url')
def step_impl(context):
    assert index.url == 'https://management.azure.com/subscriptions?api-version=2016-06-01'


@when('data is gathered from the API')
def step_impl(context):
    assert index.response.json() == requests.get(url=index.url, headers=index.headers).json()


@then('we should receive response code 200')
def step_impl(context):
    assert index.response.status_code == 200


@then('the data received should be of an enabled subscription')
def step_impl(context):
    for i in range(0, len(index.Database)):
        assert index.Database[i]["state"] == "Enabled"

