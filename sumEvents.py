import providers

def getProviders(id):
    return providers.getProvidersByUserId(id)

# python -c 'import sumEvents; sumEvents.sumDelivered(18)'
def sumDelivered(id):
    deliveries = []
    for provider in getProviders(id):
        deliveries.append(provider.delivered)
    return 'Deliveries: ' + str(sum(deliveries))

# python -c 'import sumEvents; sumEvents.sumOpens(18)'
def sumOpens(id):
    opens = []
    for provider in getProviders(id):
        opens.append(provider.opens)
    return 'Opens: ' + str(sum(opens))

def sumSpamReports(id):
    spam_reports = []
    for provider in getProviders(id):
        spam_reports.append(provider.spam_reports)
    return 'Spam Reports: ' + str(sum(spam_reports))
