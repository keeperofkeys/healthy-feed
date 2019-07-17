from django.conf import settings

def providers(request):
    return {
        'providers': [provider[0] for provider in settings.FEEDS]
    }
