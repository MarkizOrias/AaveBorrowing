from scripts.aave_borrow import (
    get_asset_price,
    get_lending_pool,
    approve_erc20,
    get_account,
)
from brownie import config, network


def test_get_asset_price():
    # Arrange / Act
    dai_usd_price = get_asset_price(
        config["networks"][network.show_active()]["dai_usd_price_feed"]
    )
    eth_usd_price = get_asset_price(
        config["networks"][network.show_active()]["eth_usd_price_feed"]
    )
    asset_price = dai_usd_price / eth_usd_price
    # Assert
    assert asset_price > 0


def test_get_lending_pool():
    # Arrange / Act
    lending_pool = get_lending_pool()
    # Assert
    assert lending_pool is not None


def test_approve_erc20():
    # Arrange
    account = get_account()
    lending_pool = get_lending_pool()
    amount = 1000000000000000000  # 1
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    # Act
    tx = approve_erc20(amount, lending_pool.address, erc20_address, account)
    # Assert
    assert tx is not True
