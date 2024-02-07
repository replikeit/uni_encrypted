from brownie import *
from .settings import IS_PUBLISH
import os


# GOERLI
def main():
    wallet = accounts.add(os.environ["PRIVATE_KEY"])
    UniEncrypted.deploy("0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6", 
            {"from": wallet}, publish_source=IS_PUBLISH)
