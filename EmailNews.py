from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='94454bdacf3247a2957f23c8de7f597f')

# Top Tech headlines
tech_headlines = newsapi.get_top_headlines(sources='mashable,techcrunch.com')

# Top Irish headlines    

#  Top World headlines



# all_articles = newsapi.get_everything(q='bitcoin',
#                                      sources='bbc-news,the-verge',
#                                       domains= 'bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)
#  sources = newsapi.get_sources()

#news = json.loads(top_headlines)

for items in tech_headlines:
    #print(items)
    if(items == 'articles'):
        for articles in tech_headlines[items]:
            print(articles)
    #for x in tech_headlines[items]:
        #print(tech_headlines[x][items])
        
        
#print(json.dumps(tech_headlines, indent = 4))
#print(top_headlines["articles"])






