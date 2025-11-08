import asyncio

class Status:
    """A Status represents whether some operation is complete.

    >>> s = Status()
    >>> s.is_done()
    False
    >>> s.done()
    >>> s.is_done()
    True
    """
    def __init__(self):
        self._done = False

    def is_done(self) -> bool:
        return self._done

    def done(self):
        self._done = True

import sys

async def get_user_input(status: Status) -> str:
    # Read one line of user input
    # Using "await" means that we're giving up control
    # and letting other coroutines run while we wait for
    # user input.
    result = await asyncio.to_thread(sys.stdin.readline) # 等待用户输入
    status.done() # Update status
    return result.strip() # 返回输入的字符串

