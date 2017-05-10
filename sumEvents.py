import providers

def sumDelivered(id):
    deliveries = []
    data = providers.getProvidersByUserId(id)
    for provider in data:
        deliveries.append(provider.delivered)
    print sum(deliveries)
