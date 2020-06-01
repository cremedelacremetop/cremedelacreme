import pymongo
import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mining']
coll = db['app']

query = {}

cursor = coll.find(query)
counter = 0
try:
    for doc in cursor:
        id_mongo = doc['_id']

        retrieved_date_start = doc['retrieved_date_start'] if 'retrieved_date_start' in doc else None
        num_week = None

        category = doc['category'] if 'category' in doc else None
        clean_category = None

        genre = doc['genre'] if 'genre' in doc else None
        unified_genre = None

        retrieved_date_end = doc['retrieved_date_end'] if 'retrieved_date_end' in doc else None
        last_update = doc['last_update'] if 'last_update' in doc else None
        last_update_days = None

        num_installs = doc['num_installs'] if 'num_installs' in doc else None
        fixed_num_installs = None

        android_version = doc['android_version'] if 'android_version' in doc else None
        macro_android_version = None

        price = doc['price'] if 'price' in doc else None
        price_usd = None

        whats_new = doc['whats_new'] if 'whats_new' in doc else None
        has_whats_new = None

        dev_address = doc['dev_address'] if 'dev_address' in doc else None
        clean_dev_address = None

        country = doc['country'] if 'country' in doc else None

        if retrieved_date_start :

            if retrieved_date_start <= datetime.datetime(2017,11,6):
                num_week = 1
            elif retrieved_date_start <= datetime.datetime(2017,11,13):
                num_week = 2
            elif retrieved_date_start <= datetime.datetime(2017,11,20):
                num_week = 3
            elif retrieved_date_start <= datetime.datetime(2017,11,27):
                num_week = 4
            elif retrieved_date_start <= datetime.datetime(2017,12,4):
                num_week = 5
            elif retrieved_date_start <= datetime.datetime(2017,12,11):
                num_week = 6
            elif retrieved_date_start <= datetime.datetime(2017,12,18):
                num_week = 7
            elif retrieved_date_start <= datetime.datetime(2017,12,25):
                num_week = 8
            elif retrieved_date_start <= datetime.datetime(2018,1,1):
                num_week = 9
            elif retrieved_date_start <= datetime.datetime(2018,1,8):
                num_week = 10
            elif retrieved_date_start <= datetime.datetime(2018,1,15):
                num_week = 11
            elif retrieved_date_start <= datetime.datetime(2018,1,22):
                num_week = 12
            elif retrieved_date_start <= datetime.datetime(2018,1,29):
                num_week = 13
            elif retrieved_date_start <= datetime.datetime(2018,2,5):
                num_week = 14
            elif retrieved_date_start <= datetime.datetime(2018,2,12):
                num_week = 15
            elif retrieved_date_start <= datetime.datetime(2018,2,19):
                num_week = 16
            elif retrieved_date_start <= datetime.datetime(2018,2,26):
                num_week = 17
            elif retrieved_date_start <= datetime.datetime(2018,3,5):
                num_week = 18
            elif retrieved_date_start <= datetime.datetime(2018,3,12):
                num_week = 19
            elif retrieved_date_start <= datetime.datetime(2018,3,19):
                num_week = 20
            elif retrieved_date_start <= datetime.datetime(2018,3,26):
                num_week = 21
            elif retrieved_date_start <= datetime.datetime(2018,4,2):
                num_week = 22
            elif retrieved_date_start <= datetime.datetime(2018,4,9):
                num_week = 23
            elif retrieved_date_start <= datetime.datetime(2018,4,15):
                num_week = 24
            elif retrieved_date_start <= datetime.datetime(2018,4,23):
                num_week = 25
            elif retrieved_date_start <= datetime.datetime(2018,4,30):
                num_week = 26
            elif retrieved_date_start <= datetime.datetime(2018,5,7):
                num_week = 27
            elif retrieved_date_start <= datetime.datetime(2018,5,14):
                num_week = 28
            elif retrieved_date_start <= datetime.datetime(2018,5,21):
                num_week = 29
            elif retrieved_date_start <= datetime.datetime(2018,5,28):
                num_week = 30

        if category:
            clean_category = category.replace('_topFree', '').replace('_topSelling', '')

        if genre:
            unified_genre = '_and_'.join(genre).lower().replace(' ','')

        if retrieved_date_end and last_update:
            last_update_days = (retrieved_date_end-last_update).days 

        if num_installs:
            if '10,000 - 50,000' in num_installs:
                fixed_num_installs = '10,000+'
            elif '50,000 - 100,000' in num_installs:
                fixed_num_installs = '50,000+'
            elif '100,000 - 500,000' in num_installs:
                fixed_num_installs = '100,000+'
            elif '500 - 1,000' in num_installs:
                fixed_num_installs = '500+'
            elif '5,000 - 10,000' in num_installs:
                fixed_num_installs = '5,000+'
            elif '50 - 100' in num_installs:
                fixed_num_installs = '50+'
            elif '100 - 500' in num_installs:
                fixed_num_installs = '100+'
            elif '1,000 - 5,000' in num_installs:
                fixed_num_installs = '1,000+'
            elif '10,000,000 - 50,000,000' in num_installs:
                fixed_num_installs = '10,000,000+'
            elif '1,000,000 - 5,000,000' in num_installs:
                fixed_num_installs = '1,000,000+'
            elif '5,000,000 - 10,000,000' in num_installs:
                fixed_num_installs = '5,000,000+'
            elif '500,000 - 1,000,000' in num_installs:
                fixed_num_installs = '500,000+'
            elif '50,000,000 - 100,000,000' in num_installs:
                fixed_num_installs = '50,000,000+'
            elif '5 - 10' in num_installs:
                fixed_num_installs = '5+'
            elif '100,000,000 - 500,000,000' in num_installs:
                fixed_num_installs = '100,000,000+'
            elif '10 - 50' in num_installs:
                fixed_num_installs = '10+'
            elif '1 - 5' in num_installs:
                fixed_num_installs = '1+'
            elif '1,000,000,000 - 5,000,000,000' in num_installs:
                fixed_num_installs = '1,000,000,000+'
            elif '500,000,000 - 1,000,000,000' in num_installs:
                fixed_num_installs = '500,000,000+'
            else:
                fixed_num_installs = num_installs


        if android_version:
            android_version = android_version.strip()
            if android_version in ['1.1 and up', '1.0 and up', '1.0 - 6.0']:
                macro_android_version = 'Unnamed and up'
            elif android_version in ['1.5 and up']:
                macro_android_version = 'Cupcake and up'
            elif android_version in ['1.6 and up']:
                macro_android_version = 'Donut and up'
            elif android_version in ['2.1 and up', '2.1 - 6.0', '2.0.1 and up', '2.0 and up', '2.0 - 4.3']:
                macro_android_version = 'Eclair and up'
            elif android_version in ['2.2 and up']:
                macro_android_version = 'Froyo and up'
            elif android_version in ['2.3.3 and up', '2.3.3 - 6.0', '2.3 and up', '2.3 - 8.0', '2.3 - 7.0']:
                macro_android_version = 'Gingerbread and up'
            elif android_version in ['3.2 and up', '3.1 and up', '3.0 and up', '3.0 - 8.0', '3.0 - 7.1.1']:
                macro_android_version = 'Honeycomb and up'
            elif android_version in ['4.0.3 and up', '4.0.3 - 7.1.1', '4.0.3 - 6.0', '4.0 and up', '4.0 - 8.0', '4.0 - 7.1.1']:
                macro_android_version = 'Ice Cream Sandwich and up'
            elif android_version in ['4.3 and up', '4.3 - 8.0', '4.3 - 7.1.1', '4.2 and up', '4.2 - 8.0', '4.2 - 7.1.1', '4.1 and up', '4.1 - 8.0', '4.1 - 7.1.1']:
                macro_android_version = 'Jelly Bean and up'
            elif android_version in ['4.4W and up', '4.4 and up', '4.4 - 8.0', '4.4 - 7.1.1', '4.4']:
                macro_android_version = 'KitKat and up'
            elif android_version in ['5.1 and up', '5.1 - 7.1.1', '5.0 and up', '5.0 - 8.0', '5.0 - 7.1.1', '5.0 - 6.0']:
                macro_android_version = 'Lollipop and up'
            elif android_version in ['6.0 and up']:
                macro_android_version = 'Marshmallow and up'
            elif android_version in ['7.1 and up', '7.0 and up', '7.0']:
                macro_android_version = 'Nougat and up'
            elif android_version in ['8.0 and up']:
                macro_android_version = 'Oreo and up'
            elif android_version in ['Varies with device']:
                macro_android_version = 'Varies with device'

        if price and country:
            if country == 'co':
                price_usd = price/2881.97
            elif country == 'br':
                price_usd = price/3.35
            elif country == 'de':
                price_usd = price/0.83
            else:
                price_usd = price

        if len(whats_new) > 0:
            has_whats_new = True
        else:
            has_whats_new = False

        if dev_address:
            clean_dev_address = dev_address.replace('<div class="content physical-address">','').replace('</div>', '')

        print('---------------')

        newvalues = { 
            '$set': { 
                    'num_week': num_week,
                    'clean_category': clean_category,
                    'unified_genre': unified_genre,
                    'last_update_days': last_update_days,
                    'fixed_num_installs': fixed_num_installs,
                    'macro_android_version': macro_android_version,
                    'price_usd': round(price_usd,4) if price_usd else price_usd,
                    'has_whats_new': has_whats_new,
                    'clean_dev_address': clean_dev_address
                }
            }
        coll.update_one({'_id': id_mongo}, newvalues)
        counter = counter + 1
        print(counter)

finally:
    client.close()