from provider import *
import requests
import json

# python -c 'import providers; providers.getProviders()'
def getProviders():
    # resp = requests.get("https://api.simplymailstatistics.com/api/v1/providers/")
    resp = requests.get("http://localhost:3000/api/v1/providers")
    providers = []
    if resp.status_code != 200:
        raise ApiError('GET /providers {}'.format(resp.status_code))
    for provider in resp.json():
        providers.append(Provider(**provider))
    return providers

# python -c 'import providers; providers.getProvidersByUserId(18)'
def getProvidersByUserId(id):
    userProviders = []
    # resp = requests.get("https://api.simplymailstatistics.com/api/v1/providers/%s" % id)
    resp = requests.get("http://localhost:3000/api/v1/providers/%s" % id)
    if resp.status_code != 200:
        raise ApiError('GET /providers/:id {}'.format(resp.status_code))
    userProviders = [Provider(**provider) for provider in resp.json()]
    return userProviders

# python -c 'import providers; providers.getProvidersByUserId(18)'
def getProviderNames(id):
    resp = requests.get("http://api.simplymailstatistics.com/api/v1/providers-names/%s" % id)
    if resp.status_code != 200:
        raise ApiError('GET /providers-names/:id {}'.format(resp.status_code))
    for provider in resp.json():
        print('{}'.format(provider))
