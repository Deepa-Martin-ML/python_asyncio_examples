import asyncio
import aiohttp
import random

async def fetch_url(url):
    print(f'Fetch Url {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f'Fetch Url {url}: After Response')
            return await response.text()
        
async def process_reponse(url,response):
    print(f"Process URL: {url}")
    sum_num = 0
    loop_count = random.randrange(1,10)
    print(f'Process URL: loop count  {loop_count}')
    for count in range(loop_count):
        randnums = random.randrange(1,10)
        sum_num = sum_num + randnums 
        print(randnums, end='')
    print(f'Process URL: Computed sum {sum_num}')        

    return sum_num
        
async def main():
    urls = [
        'https://example.com',
        'https://openai.com',
        'https://github.com'
    ]

    tasks = [fetch_url(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    tasks1 = [process_reponse(url,response) for url, response in zip(urls, responses)]
    sums = await asyncio.gather(*tasks1)

    for url, sum in zip(urls, sums):
        print('Printing sum after gathering the results')
        print(f"URL: {url}, Sum: {sum}")

if __name__ == '__main__':
    asyncio.run(main())