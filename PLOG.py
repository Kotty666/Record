#!/usr/bin/python3
import logging, logging.handlers, re, inspect
from systemd.journal import JournalHandler

class logger:

    def __init__(self,msg, level='INFO') -> None:
        stack = inspect.stack()
        self.the_class = stack[1][0].f_locals["self"].__class__.__name__
        self.the_method = stack[1][0].f_code.co_name
        self._initLogger()
        self.logger(msg,level)

    def _initLogger(self):
        logging.getLogger(__name__)
        journalHandler = JournalHandler()

        logging.basicConfig(format='%(asctime)s.%(msecs)03d - %(levelname)s - %(message)s | {cl} > {me}'.format(cl=self.the_class,me=self.the_method),
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO,
            handlers=[
                journalHandler,
        ])

    def logger(self, msg, level='INFO'):
        if re.match(level, 'debug', re.IGNORECASE):
            int_level = 10
        elif re.match(level, 'info', re.IGNORECASE):
            int_level = 20
        elif re.match(level, 'warning', re.IGNORECASE):
            int_level = 30
        elif re.match(level, 'error', re.IGNORECASE):
            int_level = 40
        elif re.match(level, 'critical', re.IGNORECASE):
            int_level = 50
        else:
            int_level = 0

        logging.log(int_level, msg)
        return