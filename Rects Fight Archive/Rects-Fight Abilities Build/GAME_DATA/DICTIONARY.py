# DICTIONARY
import MEDIA as m
import GLOBAL as g
import SPRITES as s
import random

# Sets up colors in a dictonary and returns a random color [For rainbow character]
def GET_RANDOM():
    i = random.randrange(0, 6)
    DICT = {
        0: g.BLUE,
        1: g.ORANGE,
        2: g.GREEN,
        3: g.PURPLE,
        4: g.RED,
        5: g.YELLOW,
        6: g.WHITE
    }
    return DICT[i]

def BIG_BULLET(groupa, groupb, pos, vel, img):
    print(vel)
    if not vel[0] == 0:
        if not vel[0] == -8:
            vel = (vel[0] - 4, 0)
        else:
            vel = (vel[0] + 4, 0)
    if not vel[1] == 0 and vel[0] == 0:
        if not vel[1] == -8:
            vel = (0, vel[1] - 4)
        else:
            vel = (0, vel[1] + 4)
    print(vel)
    BIGBULLET = s.BigBullet(pos, vel, img)
    groupa.add(BIGBULLET)
    groupb.add(BIGBULLET)

def TEMP_DEFAULT(groupa, groupb, pos, velocity, img):
    BULLET = s.Bullet(pos, velocity, img)
    groupa.add(BULLET)
    groupb.add(BULLET)
        
GAME_DICT = {
    # Player Media, Colors, And Locations
    'BLUE': {
        'COLOR': g.BLUE,
        'PLAYER_IMAGE': m.MEDIA['blue_face'],
        'BULLET_IMAGE': m.MEDIA['blue_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'ORANGE': {
        'COLOR': g.ORANGE,
        'PLAYER_IMAGE': m.MEDIA['orange_face'],
        'BULLET_IMAGE': m.MEDIA['orange_bullet'],
        'LOCAL': 220,
        'ABILITY': BIG_BULLET},
    'GREEN': {
        'COLOR': g.GREEN,
        'PLAYER_IMAGE': m.MEDIA['green_face'],
        'BULLET_IMAGE': m.MEDIA['green_bullet'],
        'LOCAL': 210,
        'ABILITY': TEMP_DEFAULT},
    'PURPLE': {
        'COLOR': g.PURPLE,
        'PLAYER_IMAGE': m.MEDIA['purple_face'],
        'BULLET_IMAGE': m.MEDIA['purple_bullet'],
        'LOCAL': 210,
        'ABILITY': TEMP_DEFAULT},
    'RED': {
        'COLOR': g.RED,
        'PLAYER_IMAGE': m.MEDIA['red_face'],
        'BULLET_IMAGE': m.MEDIA['red_bullet'],
        'LOCAL': 224,
        'ABILITY': TEMP_DEFAULT},
    'YELLOW': {
        'COLOR': g.YELLOW,
        'PLAYER_IMAGE': m.MEDIA['yellow_face'],
        'BULLET_IMAGE': m.MEDIA['yellow_bullet'],
        'LOCAL': 209,
        'ABILITY': TEMP_DEFAULT},
    'GREY': {
        'COLOR': g.GREY,
        'PLAYER_IMAGE': m.MEDIA['grey_face'],
        'BULLET_IMAGE': m.MEDIA['grey_bullet'],
        'LOCAL': 220,
        'ABILITY': TEMP_DEFAULT},
    'WHITE': {
        'COLOR': g.WHITE,
        'PLAYER_IMAGE': m.MEDIA['white_face'],
        'BULLET_IMAGE': m.MEDIA['white_bullet'],
        'LOCAL': 210,
        'ABILITY': TEMP_DEFAULT},
    'RAINBOW': {
        'COLOR': GET_RANDOM(),
        'PLAYER_IMAGE': m.MEDIA['rainbow_face'],
        'BULLET_IMAGE': m.MEDIA['rainbow_bullet'],
        'LOCAL': 190,
        'ABILITY': TEMP_DEFAULT},
    # HP Bars
    'HP': {
        0: m.MEDIA['hp_dead'],
        1: m.MEDIA['hp_low'],
        2: m.MEDIA['hp_decayed'],
        3: m.MEDIA['hp_full']},
    # Mode Values [Loaded In main game depending on g.MODE]
    'MODE': {
        'CLASSIC': {
            'TIMER': 30,
            'PLAYER_VELOCITY': 5,
            'BULLET_VELOCITY': 8,
            'HEALTH': 3,
            'SOUND': m.MEDIA['classic_sound'],
            'MUSIC': m.MEDIA['classic_music']},
        'CHAOS': {
            'TIMER': 10,
            'PLAYER_VELOCITY': 8,
            'BULLET_VELOCITY': 15,
            'HEALTH': 1,
            'SOUND': m.MEDIA['chaos_sound'], 
            'MUSIC': m.MEDIA['chaos_music']}
        },
    # Timer Values
    'TIMER': {
        True: [g.RED, g.FONTB],
        False: [g.WHITE, g.FONTNORMAL]},
}     
