# using shared state object to prevent race conditions and circular dependencies on async modules.

import asyncio

class SharedState:
    def __init__(self):
        self.username = ""
        self.lock = asyncio.Lock()
        
    async def get_username(self):
        async with self.lock:
            return self.username


    async def set_username(self, new_value):
        async with self.lock:
            self.username = new_value
            print(f"Shared state username updated to {self.username}")



application_state = SharedState()

