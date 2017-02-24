import sys ,pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
     """响应按键和鼠标事件"""
     if event.key == pygame.K_RIGHT:
         #move rght
         ship.moving_right = True
     elif event.key == pygame.K_LEFT:
         ship.moving_left = True
     elif event.key == pygame.K_UP:
         ship.moving_up = True
     elif event.key == pygame.K_DOWN:
         ship.moving_down = True 
     elif event.key == pygame.K_SPACE:
         if len(bullets) < ai_settings.bullets_allowed:
             new_bullet = Bullet(ai_settings,screen,ship)
             bullets.add(new_bullet)   
def check_keyup_events(event,ai_settings,screen,ship,bullets):
     if event.key == pygame.K_RIGHT:
         ship.moving_right = False
     elif event.key == pygame.K_LEFT:
         ship.moving_left = False
     elif event.key == pygame.K_UP:
         ship.moving_up = False
     elif event.key == pygame.K_DOWN:
         ship.moving_down = False  
                
def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)       
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
                       
def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    
    pygame.display.flip()
   
def update_bullets(bullets):
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
