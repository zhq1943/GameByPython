import sys,pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
def run_game():
    #初始化游戏并创建一个屏幕
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(ai_settings,screen)
    
    bullets = Group()
    #set back color
    bg_color = ai_settings.bg_color
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        #print(len(bullets))
        
        gf.update_screen(ai_settings,screen,ship,bullets)
        
        
            
run_game()
