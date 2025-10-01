import aiohttp
import asyncio

async def recuperer_donnees(url):
    
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    session = aiohttp.ClientSession()
    
    response = await session.get(url)   
    
    if response.status == 200:
        data = await response.json()
        print(data)
    
    elif response.status == 404:
        print("Erreur HTTP: {response.status}")
    
    await response.release()
    await session.close()

asyncio.run(recuperer_donnees("https://jsonplaceholder.typicode.com/todos/1"))

    