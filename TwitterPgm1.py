from TwitterAPI import TwitterAPI
consumer_key = "QlZUBAbMB9suzDKI1PeVsX4Hk"
consumer_secret = "qbclbrBtJyP3v22JMZY2plyO2PzyMIJXIqbs1NUjVrFV4HOiO5"
access_token_key = "781110054284103681-DLx1WVyCzSLCzH0zLYK25cU0A7vLQow"
access_token_secret = "qN0EpBgFNKrpHYmhf47qhODi1vP6g8nVLs7OTAYlkJLq2"
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
#Get tweet by its id:
r = api.request('statuses/show/:%d' % 781118223047680000)
print(r.text)
#Stream tweets from New York City:
'''r = api.request('statuses/filter', {'locations':'-74,40,-73,41'})
for item in r:
        print(item)'''