from configs import config_reader as config

if config.INPUT_TYPE.lower() == 'cmd':
    from view.cmd_ import CmdView as View
else:
    from view.input_ import InputView as View
