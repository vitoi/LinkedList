from typing import Any, Optional

rootlogger: Any = ...

def class_logger(cls): ...

class Identified(object):
    logging_name: str = ...
    def _should_log_debug(self) -> bool: ...
    def _should_log_info(self) -> bool: ...

class InstanceLogger(object):
    echo: Any
    logger: Any = ...
    def __init__(self, echo, name) -> None: ...
    def debug(self, msg, *args, **kwargs): ...
    def info(self, msg, *args, **kwargs): ...
    def warning(self, msg, *args, **kwargs): ...
    def warn(self, msg, *args, **kwargs): ...
    def error(self, msg, *args, **kwargs): ...
    def exception(self, msg, *args, **kwargs): ...
    def critical(self, msg, *args, **kwargs): ...
    def log(self, level, msg, *args, **kwargs): ...
    def isEnabledFor(self, level): ...
    def getEffectiveLevel(self): ...

def instance_logger(instance, echoflag: Optional[Any] = ...): ...

class echo_property(object):
    __doc__: str = ...
    def __get__(self, instance, owner): ...
    def __set__(self, instance, value): ...
