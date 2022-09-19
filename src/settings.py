USE_DOCKER = False

if USE_DOCKER:
    postgresql = {
        'pguser': 'zxc',
        'pgpswd': 'zxc',
        'pghost': 'db',   
        'pgport': 5432,
        'pgdb': 'async_db'
    }
else:
    postgresql = {
        'pguser': 'zxc',
        'pgpswd': 'zxc',
        'pghost': 'localhost',   
        'pgport': 5432,
        'pgdb': 'async_db'
    }



headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33"
}

bot_token = '5367418874:AAF3q6zKABDCgZFR-P0cSFTnV_pL3cUMDEs'
chat_id = '-1001595046697'
chanel = 'https://t.me/storage_psql_dumps'