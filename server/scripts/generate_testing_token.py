#!/usr/bin/env python
import django, uuid, sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dva.settings")
django.setup()
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

if __name__ == '__main__':
    u = User.objects.create_user("test_token_user", email="test@test.com", password=str(uuid.uuid1()))
    try:
        token, _ = Token.objects.get_or_create(user=u)
    except:
        token = Token.objects.get(user=u)
    with open('creds.json', 'w') as creds:
        creds.write(json.dumps({'token': token.key}))
    print token.key
