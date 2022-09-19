import asyncio
import aiohttp
import os
import time
print('hello')
from settings import USE_DOCKER, headers
print('hello again')

# if USE_DOCKER:
#         print('[INFO] Waitong for postgresql start... sleeping 5s')
#         time.sleep(5)


from alt_database import clear_db
from pull_content import get_page_data
from page_quantity import get_pages_quantity, max_url



async def load_site_data():
    clear_db()
    pages = get_pages_quantity(max_url, headers)
    async with aiohttp.ClientSession() as session:
        tasks = []

        for page in range(1, pages+1):
                task = asyncio.create_task(get_page_data(session, tasks, page_id=page))            
                tasks.append(task)
                await asyncio.sleep(4)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
        asyncio.run(load_site_data())
        os.system('pg_dump async_db | gzip > dump.async_db.gz')
        if USE_DOCKER:
                print('[INFO] Done!')
                print('[INFO] You can dump data by runing \n'
                '"docker exec postgres_db pg_dump -U zxc -F t async_db | gzip > docker_async_db.gz"')