#from CursEngine import CursEngine
from CursEngine.Curse import Curse
from Module.CursEngine.__init__ import CursEngine
from time import sleep

def DVDShowcase():
    class MyEngine(CursEngine):
        def __init__(self):
            super().__init__(framepause=0.5,screen_size=(60,20))
        async def before_main(self):
            e=await self.new_entity('box',False,30,10,3,3,'rect',1)
            e.set_velocity(1,0.5)
            self.assign({'box':e})
            self.add_color_pair(1,'blue','black')
        async def main(self):
            en=self.get('box')
            if en.x>=self.screen_size[0] or en.x<=0:
                en.velocityX*=-1
            if en.y>=self.screen_size[1] or en.y<=0:
                en.velocityY*=-1
            self.assign({'box':en})
    MyEngine()  

def BounceShowcase():
    class MyEngine(CursEngine):
        def __init__(self):
            super().__init__(framepause=0.07)

        def adjust(self,en,en2):
            while en.isTouching(en2,-1):
                en.y-=1
        
        async def before_main(self):
            await self.new_entity('new',False,3,3, 2, 2, 'rect', 1)
            await self.new_entity('ground',False,1,15,58,3,'rect',2)
            await self.new_var('jumps',5)
            self.add_color_pair(1,'red','black')
            self.add_color_pair(2,'green', 'black')
            
            e=self.get('new')
            e.velocityY=0

        async def main(self):
            en=self.get('new')
            grn=self.get('ground')
            u=self.get('jumps')

            en.velocityY+=0.07

            if en.isTouching(grn,-1) and u>0:
                en.velocityY*=-0.8
                u-=1

            elif en.isTouching(grn,0) and u<=0:
                en.velocityY=0
                self.adjust(en,grn)
            
            self.assign({'new':en,'jumps':u})

    MyEngine()

async def wrapit_before(engine):
    await engine.new_entity('new',False,1,1,1,1,'rect')

async def wrapit_main(engine):
    myen=engine.get('new')
    myen.velocityX=1

#e=CursEngine(mode='wrap')
#e.wrap((wrapit_before,wrapit_main))

def main():
    m=Curse()
    menu=['DVD Showcase','Bouncing Square Showcase','Credits']
    menu_f=['break']*len(menu)
    menu_c=[1,2,4]
    m.add_color_pair(1,'blue','black')
    m.add_color_pair(2,'red','black')
    m.add_color_pair(3,'white','black')
    m.add_color_pair(4,'yellow','black')

    m.menu_board(menu,menu_c)
    mode=m.menu_board_input(cursor='3|-> $field <-',inputs=menu_f)
    m.refresh()
    m.clear()
    m.close()

    sleep(1)

    if mode=='DVD Showcase':
        DVDShowcase()
    elif mode=='Bouncing Square Showcase':
        BounceShowcase()
    else:
        print("this is cool - yash 2021")

