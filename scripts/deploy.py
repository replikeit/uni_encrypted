from brownie import *
from .settings import IS_PUBLISH
import os


# GOERLI
def main():
    wallet = accounts.add(os.environ["PRIVATE_KEY"])
    UniEncrypted.deploy("0x0B1ba0af832d7C05fD64161E0Db78E85978E8082", 
            {"from": wallet}, publish_source=IS_PUBLISH)
