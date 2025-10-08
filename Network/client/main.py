from client_manager import ClientGame
import asyncio

client = ClientGame()
asyncio.run(client.initialize())


while True:
    action = input("Enter action (0: wait, 1: up, 2: down, 3: left, 4: right, 5: pick, 6: drop): ")
    try:
        asyncio.run(client.execute_action(action))
    except Exception as e:
        print(f"Error executing action: {e}")
