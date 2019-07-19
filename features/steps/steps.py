from behave import *
import requests
import index


@given('we have a valid url')
def step_impl(context):
    assert index.url == 'https://management.azure.com/subscriptions?api-version=2016-06-01'


@when('data is gathered from the API')
def step_impl(context):
    if index.response.json() == requests.get(url=index.url, headers=index.headers).json():
        pass


@then('we should receive response code 200')
def step_impl(context):
    assert index.response.status_code == 200

