
import asyncio

async def envoyer_message(nome, phone):
    print(f"Envoi du message à {nome} sur le numéro {phone}")
    await asyncio.sleep(2)  # Simule un délai d'envoi
    print(f"Message envoyé à {nome}")


async def main():
    await asyncio.gather(
        envoyer_message("Alice", "+123456789"),
        envoyer_message("Bob", "+987654321")
    )

asyncio.run(main())