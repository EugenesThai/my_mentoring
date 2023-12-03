import time
import asyncio
import aiohttp

# Написать код было тяжело


async def ping_site(session, site):
    tic = time.perf_counter()
    try:
        async with session.get(site) as response:
            response.raise_for_status()
            # return response.elapsed.total_seconds()
            toc = time.perf_counter()
            return toc - tic
    except aiohttp.ClientResponseError as cre:
        print(f"Error for {site}: {cre.status} - {cre.message}")
        return None
    except Exception as e:
        print(f"Error for {site}: {str(e)}")
        return None


async def main():
    sites_to_ping = [
        "https://google.com",
        "https://github.com",
        "https://skdjxcsicifjcijfcif.mmmm",
        "https://baidu.com",
        "https://yandex.ru",
        "http://127.0.0.1:8000",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[ping_site(session, site) for site in sites_to_ping]
        )

    for site, result in zip(sites_to_ping, results):
        print(f"Ping for {site}: {result if result is not None else 'ERROR'} seconds")


asyncio.run(main())
