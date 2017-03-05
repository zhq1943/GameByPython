class Settings():
    """save all game settings"""
    def __init__(self):
        #alien settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        #bullet
        
        self.bullet_speed_factor = 1.5
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10
        self.bullet_distance = 30
        
        self.ship_space_times_self = 2
        self.alien_speed_factor = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3
        
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """initiallize game process faster game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.fleet_direction = 1
        self.alien_points = 50
        
    def increase_speed(self):
        """icrease speed"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
        #print(self.alien_points)       
        
