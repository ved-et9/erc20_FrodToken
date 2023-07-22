from brownie import  FrodToken
from scripts.helpful_scripts import get_account
from web3 import Web3


intial_supply = Web3.toWei(10000,"ether")

def main():
    account=get_account()
    frod_Token = FrodToken.deploy(intial_supply,{"from":account})
    print(frod_Token.name())