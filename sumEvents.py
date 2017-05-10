import providers

def getProviders(id):
    return providers.getProvidersByUserId(id)

# python -c 'import sumEvents; sumEvents.sumDelivered(18)'
def sumDelivered(id):
    deliveries = []
    for provider in getProviders(id):
        deliveries.append(provider.delivered)
    print 'Deliveries: ' + str(sum(deliveries))

# def sumOpens(id):
#     opens = []
