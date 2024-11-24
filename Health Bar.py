pg.draw.rect(screen,"red",(250,250,300,40))
pg.draw.rect(screen,"green",(250,250,300*ratio,40))
def init(self,x,y,w,h,max_hp):
    self.x=x
    self.y=y
    self.h=h
    self.hp=max_hp
    self.max_hp=max_hp
def draw(self,surface):
    ratio=self.hp/self.max_hp
health_bar=HealthBar(250,200,300,40,100)
