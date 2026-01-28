import MetaTrader5 as mt5

def place_order(symbol, order_type, lot, sl_points=200, tp_points=400):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        raise RuntimeError("Symbol not found")

    if not symbol_info.visible:
        mt5.symbol_select(symbol, True)

    price = mt5.symbol_info_tick(symbol).ask if order_type == "BUY" else mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY if order_type == "BUY" else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": price - sl_points * symbol_info.point if order_type == "BUY" else price + sl_points * symbol_info.point,
        "tp": price + tp_points * symbol_info.point if order_type == "BUY" else price - tp_points * symbol_info.point,
        "deviation": 20,
        "magic": 10001,
        "comment": "SHOPZOO_AI",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    return result
