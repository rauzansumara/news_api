from api.crawler import news_crawler_tempo
from api.crawler import news_crawler_republika
from api.crawler import news_crawler_kompas
from api.crawler import news_crawler_liputan6
from api.crawler import news_crawler_viva
from operator import itemgetter

def unfiltered_paged(amount):
    news_ready = []

    viva = news_crawler_viva.data_json
    #lip6 = news_crawler_liputan6.data_json[:20]
    tempo = news_crawler_tempo.data_json
    republika = news_crawler_republika.data_json
    kompas = news_crawler_kompas.data_json
    '''
    for w,x,y,z in zip(lip6,tempo,republika,kompas):
        news_ready.append(w)
        news_ready.append(x)
        news_ready.append(y)
        news_ready.append(z)
    '''
    news_ready = viva+tempo+republika+kompas
    '''
    newlist = []
    for sublist in news_ready:
        for item in sublist:
            newlist.append(item)
    '''
    newlist = sorted(news_ready, key=itemgetter('date'), reverse=True)
    #newlist = sorted(news_ready, key=lambda x: Timestamp(x['date']))
    
    #newlist = sorted(news_ready['data'], key=itemgetter('date')) 

    amount = amount*20

    if amount < len(newlist):
        b = newlist[(0 if amount < 20 else amount):(amount+20 if amount >= 20 else amount+20)]
    else:
        b = False

    return b