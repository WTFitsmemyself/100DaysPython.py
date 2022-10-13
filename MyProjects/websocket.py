from twelvedata import TDClient


def on_event(e):
    print(e)


td = TDClient(apikey="ce4a51735dd64fcd986ca573836a380a")
ws = td.websocket(symbols="APPL", on_event=on_event)
ws.connect()
ws.keep_alive()
