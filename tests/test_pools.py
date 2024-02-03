from brownie import *
import pytest
from scripts.encoder import generate_random_input


@pytest.fixture(scope="module")
def kit():
    return accounts.at('0x6B44ba0a126a2A1a8aa6cD1AdeeD002e141Bcd44', force=True)


@pytest.fixture(scope="module")
def uni_encrypted_contract(kit):
    weth = Contract.from_explorer("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")
    uni_enc = UniEncrypted.deploy("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2", {"from":accounts[0]})
    weth.approve(uni_enc.address, "1 ether", {"from": kit})
    return uni_enc


def test_usdc_weth(uni_encrypted_contract, kit):
    usdc = Contract.from_explorer("0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48")
    balance_before = usdc.balanceOf(kit)
    uni_encrypted_contract.encodedSwap(generate_random_input("0x763d3b7296e7C9718AD5B058aC2692A19E5b3638", 0.1), {"from": kit})
    assert balance_before < usdc.balanceOf(kit)
