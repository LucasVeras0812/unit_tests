import pytest
from async_utils import processar_dado

@pytest.mark.asyncio
async def test_processar_dado():
    resultado = await processar_dado("ntt data")
    assert resultado == "NTT DATA"
    
