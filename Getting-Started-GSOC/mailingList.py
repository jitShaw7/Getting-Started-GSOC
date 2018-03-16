import requests

def subscribe(userEmail, subscriptionList):
    url = 'https://lists.debian.org/cgi-bin/subscribe.pl'
    
    data = {'user_email': userEmail,
            'list': subscriptionList,
            'action': 'subscribe'}

    r = requests.post(url, data)
    errorMessage = 'Bad data in e-mail address'
    if(r.status_code == 200 and errorMessage not in r.text):
        print(r.text)
        return 1
    else:
        print(r.text)
        return 0


