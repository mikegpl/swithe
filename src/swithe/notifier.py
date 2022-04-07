from contextlib import ContextDecorator


class notify_on_finish(ContextDecorator):
    def __enter__(self):
    	print('Starting')
        return self

    def __exit__(self, *exc):
        print("And I'm notifying right now")
        print(f"This exception might not exist: {exc}")
        return False
