import providers

def getProviders(id):
    return providers.getProvidersByUserId(id)

# python -c 'import sumEvents; sumEvents.sumDelivered(18)'
def sumDelivered(data):
    deliveries = []
    for provider in data:
        deliveries.append(provider.delivered)
    return 'Deliveries: ' + str(sum(deliveries))

# python -c 'import sumEvents; sumEvents.sumOpens(18)'
def sumOpens(data):
    opens = []
    for provider in data:
        opens.append(provider.opens)
    return 'Opens: ' + str(sum(opens))

# python -c 'import sumEvents; sumEvents.sumSpamReports(18)'
def sumSpamReports(data):
    spam_reports = []
    for provider in data:
        spam_reports.append(provider.spam_reports)
    return 'Spam Reports: ' + str(sum(spam_reports))

# python -c 'import sumEvents; sumEvents.returnEvents(18)'
def returnEvents(id):
    data = getProviders(id)
    print sumDelivered(data)
    print sumOpens(data)
    print sumSpamReports(data)
