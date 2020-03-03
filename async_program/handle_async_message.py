import asyncio
import aiohttp


async def handle_message(topic, uid, payload):
    """
    Async function
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
            "records" : [{
                "value" : {
                    "device" : uid,
                    "payload": payload,
                    "topic": topic
                    }
                }]
            }

    async with aiohttp.ClientSession() as session:
        async with  session.post(url, data=data) as response:
            data = await response.text()
        print (data)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([handle_message('mykafkatopic', '0e5d5851-f436-4dd3', {})]))