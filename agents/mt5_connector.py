import MetaTrader5 as mt5

def connect_mt5():
    if not mt5.initialize():
        raise RuntimeError("MT5 initialize failed")
    account = mt5.account_info()
    if account is None:
        raise RuntimeError("MT5 account not found")
    return account

def shutdown_mt5():
    mt5.shutdown()
