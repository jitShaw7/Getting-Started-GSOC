import requests

def subscribe(userEmail, subscriptionList):
    url = 'https://lists.debian.org/cgi-bin/subscribe.pl'
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    #for mailList in subscriptionList:
    data = ''
    for option in subscriptionList:
        data = data + "subscribe=" + option + "&"
    data = data + "user_email=" + userEmail
    print(data)

    r = requests.post(url, data=data, headers = headers)
    errorMessage = 'Bad data in e-mail address'
    if(r.status_code == 200 and errorMessage not in r.text):
        print(r.content)
        return 1
    else:
        print(r.content)
        return 0


