from api.crawler import news_crawler_tempo
from api.crawler import news_crawler_republika
from api.crawler import news_crawler_kompas
from api.crawler import news_crawler_liputan6
from api.crawler import news_crawler_viva
from operator import itemgetter
from sklearn.externals import joblib

def filter(data):
    loaded_model = joblib.load('model/lsvcmodel.pkl')

    predicted = loaded_model.predict(data)
    return predicted

def filtered():
    news_ready = []

    viva = news_crawler_viva.data_json
    #lip6 = news_crawler_liputan6.data_json[:20]
    tempo = news_crawler_tempo.data_json
    republika = news_crawler_republika.data_json
    kompas = news_crawler_kompas.data_json

    news_ready = tempo+republika+kompas+viva

    t = []
    for i in news_ready:
        t.append(i['title'])

    predicted = filter(t)

    news = []
    for x in zip(news_ready, predicted):
        if x[1] == 1:
            news.append(x[0])

    newlist = sorted(news, key=itemgetter('date'), reverse=True)

    return newlist