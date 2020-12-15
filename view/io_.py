from configs import config_reader as config
from view.telnet_ import TelnetServer


class IO:
    if config.INPUT_MODE.lower() == 'telnet':
        s = TelnetServer()
        data_input_ = s.conn.receive_input
        print_ = s.conn.send_withnl
        log_ = print
        telnet_server_shutdown = s.shutdown

    else:
        data_input_ = input
        print_ = print
        log_ = print
