import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

from ship import Ship
# from alien import Alien
import game_function as gf

from pygame.sprite import Group

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")
    
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 创建一个用于储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)   
    # 创建一个用于存储子弹的编组
    bullets = Group()    
    # 创建一个用于存储外星人的编组
    aliens = Group()
    # alien = Alien(ai_settings, screen)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # 开始游戏的主循环
    while True:
        
        # 监视键盘和鼠标事件
            gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
            
            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
