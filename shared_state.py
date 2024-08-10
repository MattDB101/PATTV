# using shared state object to prevent race conditions and circular dependencies on async modules.

import asyncio

class SharedState:
    def __init__(self):
        self.username = ""
        self.streamkey = ""
        self.lock = asyncio.Lock()
        
    async def get_username(self):
        async with self.lock:
            return self.username
        
    async def get_streamkey(self):
        async with self.lock:
            return self.streamkey

    async def set_user(self, new_username, new_streamkey):
        async with self.lock:
            self.username = new_username
            self.streamkey = new_streamkey
            print(f"Shared state user updated to {self.username}")

            
application_state = SharedState()

