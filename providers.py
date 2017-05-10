import requests
import pdb


# python -c 'import providers; providers.getProvidersByUserId(18)'

def getProvidersByUserId(id):
    resp = requests.get("http://localhost:3000/api/v1/providers/%s" % id)
    # pdb.set_trace()
    if resp.status_code != 200:
        raise ApiError('GET /providers/ {}'.format(resp.status_code))
    for provider in resp.json():
        print('{} {}'.format(provider['id'], provider['provider_name']))
