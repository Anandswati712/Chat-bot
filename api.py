import requests, json

def news(input):
    link = requests.get(
    "https://newsapi.org/v2/everything?q=" + input +
    "&from=2023-01-01&sortBy=publishedAt&apiKey=41e0c9be6ba340a185222e9f02f6ef89")

    jsonREQ = json.loads(link.text)

    articles = jsonREQ['articles']

    for i in range(5):
        print(str(i) + ". " + articles[i]['title'])


def weather(input):
    location = requests.get("http://api.openweathermap.org/geo/1.0/direct?q="+input+"&limit=5&appid=48437ccd3178a1c967fd99d4c4a7eaec")
    jsonREQ = json.loads(location.text)

    latitude = jsonREQ[0]['lat']
    longitude = jsonREQ[0]['lon']

    link = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+str(latitude)+"&lon="+str(longitude)+"&appid=48437ccd3178a1c967fd99d4c4a7eaec")
    json_link = json.loads(link.text)

    print("Temperature : " ,json_link['main']['temp'] ,"F")



def jokes():
    link = requests.get("https://api.chucknorris.io/jokes/random")
    json_link = json.loads(link.text)

    print(json_link['value'])
