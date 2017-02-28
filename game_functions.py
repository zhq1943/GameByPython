import sys ,pygame
from bullet import Bullet
from alien import Alien

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
         #ship.on_fire = True
         fire_bullet(ai_settings,screen,ship,bullets)
     elif event.key == pygame.K_q:
         sys.exit()    
         
def check_keyup_events(event,ai_settings,screen,ship,bullets):
     if event.key == pygame.K_RIGHT:
         ship.moving_right = False
     elif event.key == pygame.K_LEFT:
         ship.moving_left = False
     elif event.key == pygame.K_UP:
         ship.moving_up = False
     elif event.key == pygame.K_DOWN:
         ship.moving_down = False 
     #elif event.key == pygame.K_SPACE:
         #ship.on_fire = False     
                
def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)       
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
                       
def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
            
    ship.blitme()
    aliens.draw(screen)
    
    pygame.display.flip()
   
def update_bullets(ai_settings, screen, ship,bullets,aliens):
    """刷新子弹"""
    bullets.update()
    
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    #检测碰撞
    check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)        
           
            
def fire_bullet(ai_settings,screen,ship,bullets):
    """创建子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
            
        
def get_number_aliens_x(ai_settings,alien_width):
    """计算外星人列数"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x  
    
def get_number_rows(ai_settings,ship_height,alien_height):
    """计算外星人行数"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows  
      
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """create alien"""    
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width  
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien) 
        
def create_fleet(ai_settings, screen,ship,aliens):
    """创建外星人方正"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_aliens_y = get_number_rows(ai_settings, ship.rect.height*ai_settings.ship_space_times_self, alien.rect.height)
    for row_number in range(number_aliens_y): 
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
           
def update_aliens(ai_settings,aliens):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
def check_fleet_edges(ai_settings, aliens):
    """有外星人 到达边缘 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
            
def change_fleet_direction(ai_settings, aliens):
    """改变外星人移动的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1    
    
def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
    #check if bullets hit alien
    #重叠检测，返回字典 key bullet val alien
    #param 3 delete bullet
    #param 4 delete alien
    collision = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    #外星人为空，重新生成子弹和外星人
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)     
          
