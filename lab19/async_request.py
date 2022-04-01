import asyncio
import aiohttp

async def do_request():
	async with aiohttp.request('GET', 'https://google.com') as response:
		html = await response.read()
		print(html)


# init event loop:
loop = asyncio.get_event_loop()

# run tasks in event loop:
loop.run_until_complete(do_request())


