import asyncio

async def processar_dado(dado: str) -> str:
    await asyncio.sleep(1)
    return dado.upper()