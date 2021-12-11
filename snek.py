from Module.CursEngine.__init__ import CursEngine

def snek():
    class SnekEngine(CursEngine):
        def __init__(self):
            super().__init__(framepause=0.1)

        async def before_main(self):
            r=await self.new_ductile_entity('snake',False,2,2,2,1)
            r.extend(2)

        async def main(self):
            pass

    SnekEngine()