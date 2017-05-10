from provider import *
import requests
import pdb
import json
# pdb.set_trace()

# python -c 'import providers; providers.getProviders()'
def getProviders():
    resp = requests.get("http://localhost:3000/api/v1/providers/")
    if resp.status_code != 200:
        raise ApiError('GET /providers {}'.format(resp.status_code))
    for provider in resp.json():
        p = Provider(**provider)
        print p

# python -c 'import providers; providers.getProvidersByUserId(18)'
def getProvidersByUserId(id):
    resp = requests.get("http://localhost:3000/api/v1/providers/%s" % id)
    if resp.status_code != 200:
        raise ApiError('GET /providers/:id {}'.format(resp.status_code))
    for provider in resp.json():
        print('{} {}'.format(provider['id'], provider['provider_name']))

# python -c 'import providers; providers.getProvidersByUserId(18)'
def getProviderNames(id):
    resp = requests.get("http://localhost:3000/api/v1/providers-names/%s" % id)
    if resp.status_code != 200:
        raise ApiError('GET /providers-names/:id {}'.format(resp.status_code))
    for provider in resp.json():
        print('{}'.format(provider))
