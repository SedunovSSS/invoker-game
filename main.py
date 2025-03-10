import pygame
import time
import random
import json
import os
pygame.init()

WIDTH, HEIGHT = 860, 860
SLIDER_WIDTH, SLIDER_HEIGHT = 160, 10
SLIDER_X, SLIDER_Y = (WIDTH - SLIDER_WIDTH) - 20, 20
FPS = 666

sc = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

pygame.display.set_caption('Invoker Game')
icon = pygame.image.load(os.getcwd()+'/spells/invoker.png').convert_alpha()
pygame.display.set_icon(icon)


spells = {
    'qqq': {
        'fullname': 'Cold Snap',
        'image': pygame.image.load('spells/invoker_cold_snap.png').convert_alpha()
    },
    'qqw': {
        'fullname': 'Ghost Walk',
        'image': pygame.image.load('spells/invoker_ghost_walk.png').convert_alpha()
    },
    'eqq': {
        'fullname': 'Ice Wall',
        'image': pygame.image.load('spells/invoker_ice_wall.png').convert_alpha()
    },
    'www': {
        'fullname': 'E.M.P',
        'image': pygame.image.load('spells/invoker_emp.png').convert_alpha()
    },
    'qww': {
        'fullname': 'Tornado',
        'image': pygame.image.load('spells/invoker_tornado.png').convert_alpha()
    },
    'eww': {
        'fullname': 'Alacrity',
        'image': pygame.image.load('spells/invoker_alacrity.png').convert_alpha()
    },
    'eee': {
        'fullname': 'Sun Strike',
        'image': pygame.image.load('spells/invoker_sun_strike.png').convert_alpha()
    },
    'eeq': {
        'fullname': 'Forge Spirit',
        'image': pygame.image.load('spells/invoker_forge_spirit.png').convert_alpha()
    },
    'eew': {
        'fullname': 'Chaos Meteor',
        'image': pygame.image.load('spells/invoker_chaos_meteor.png').convert_alpha()
    },
    'eqw': {
        'fullname': 'Deafening Blast',
        'invoke': 'qwe',
        'image': pygame.image.load('spells/invoker_deafening_blast.png').convert_alpha()
    },
}

quas = pygame.image.load('spells/invoker_quas.png')
wex = pygame.image.load('spells/invoker_wex.png')
exort = pygame.image.load('spells/invoker_exort.png')
invoke = pygame.image.load('spells/invoker_invoke.png')

font = pygame.font.SysFont('Arial', 50, bold=True)
font1 = pygame.font.SysFont('Arial', 20, bold=True)

dragging = False
score = 0

try:
    f = open('settings.json', 'r')
    data = json.load(f)
    best_score = data['best_score']
    slider_value = data['slider_value']
except:
    best_score = 0
    slider_value = 0.25
time2makespell = max(1, int(slider_value*20))

running = True
lose = False
start = False

current_spheres = ''
current_spells = [None]*2


while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN and not start and not lose:
            if i.key == pygame.K_RETURN:
                choised_spell = random.choice(list(spells.keys()))
                endtime = time.time() + time2makespell + 1
                start = True
        elif i.type == pygame.KEYDOWN and not lose:
            if i.key == pygame.K_q:
                current_spheres += 'q'
            if i.key == pygame.K_w:
                current_spheres += 'w'
            if i.key == pygame.K_e:
                current_spheres += 'e'
            if len(current_spheres) > 3:
                current_spheres = current_spheres[-3:]
            if i.key == pygame.K_r:
                if len(current_spheres) == 3:
                    s = ''.join(list(sorted(list(current_spheres))))
                    if s not in current_spells:
                        current_spells[1] = current_spells[0]
                        current_spells[0] = s
                    if s == choised_spell:
                        time_diff = endtime - time.time()
                        score += int((1000*time_diff/(time2makespell)**2))
                        if score >= best_score:
                            best_score = score
                            json.dump({'best_score': best_score, 'slider_value': slider_value}, open('settings.json', 'w'), indent=4)
                        new_choised_spell = random.choice(list(spells.keys()))
                        while new_choised_spell == choised_spell or new_choised_spell in current_spells:
                            new_choised_spell = random.choice(list(spells.keys()))
                        choised_spell = new_choised_spell
                        endtime = time.time() + time2makespell + 1

        elif i.type == pygame.KEYDOWN and lose:
            if i.key == pygame.K_RETURN:
                current_spheres = ''
                current_spells = [None]*2
                score = 0
                new_choised_spell = random.choice(list(spells.keys()))
                while new_choised_spell == choised_spell or new_choised_spell in current_spells:
                    new_choised_spell = random.choice(list(spells.keys()))
                choised_spell = new_choised_spell
                lose = False
                endtime = time.time() + time2makespell + 1

        elif i.type == pygame.MOUSEBUTTONDOWN and not lose and start:
            mx, my = pygame.mouse.get_pos()
            if HEIGHT-16-128 <= my <= HEIGHT-16 and 16 <= mx <= 128+16:
                current_spheres += 'q'

            if HEIGHT-16-128 <= my <= HEIGHT-16 and 154 <= mx <= 128+154:
                current_spheres += 'w'

            if HEIGHT-16-128 <= my <= HEIGHT-16 and 292 <= mx <= 128+292:
                current_spheres += 'e'

            if HEIGHT-16-128 <= my <= HEIGHT-16 and 706 <= mx <= 128+706:
                if len(current_spheres) == 3:
                    s = ''.join(list(sorted(list(current_spheres))))
                    if s not in current_spells:
                        current_spells[1] = current_spells[0]
                        current_spells[0] = s
                    if s == choised_spell:
                        time_diff = endtime - time.time()
                        score += int((1000*time_diff/(time2makespell)**2))
                        if score >= best_score:
                            best_score = score
                            json.dump({'best_score': best_score, 'slider_value': slider_value}, open('settings.json', 'w'), indent=4)
                        new_choised_spell = random.choice(list(spells.keys()))
                        while new_choised_spell == choised_spell or new_choised_spell in current_spells:
                            new_choised_spell = random.choice(list(spells.keys()))
                        choised_spell = new_choised_spell
                        endtime = time.time() + time2makespell + 1

            if len(current_spheres) > 3:
                current_spheres = current_spheres[-3:]

        elif i.type == pygame.MOUSEBUTTONDOWN and (lose or (not start)):
            if i.button == 1:
                mouse_x, mouse_y = i.pos
                if SLIDER_X <= mouse_x <= SLIDER_X + SLIDER_WIDTH and SLIDER_Y <= mouse_y <= SLIDER_Y + SLIDER_HEIGHT:
                    dragging = True
                    slider_value = (mouse_x - SLIDER_X) / SLIDER_WIDTH
                    slider_value = max(0, min(slider_value, 1))
                    time2makespell = max(1, int(slider_value*20))
                    json.dump({'best_score': best_score, 'slider_value': slider_value}, open('settings.json', 'w'), indent=4)

        elif i.type == pygame.MOUSEBUTTONUP and (lose or (not start)):
            if i.button == 1:
                dragging = False

        elif i.type == pygame.MOUSEMOTION and (lose or (not start)):
            if dragging:
                mouse_x, _ = i.pos
                slider_value = (mouse_x - SLIDER_X) / SLIDER_WIDTH
                slider_value = max(0, min(slider_value, 1))
                time2makespell = max(1, int(slider_value*20))
                json.dump({'best_score': best_score, 'slider_value': slider_value}, open('settings.json', 'w'), indent=4)

    sc.fill('black')
    sc.blit(quas, (16, HEIGHT-16-128))
    sc.blit(wex, (154, HEIGHT-16-128))
    sc.blit(exort, (292, HEIGHT-16-128))

    if start:
        sc.blit(spells[choised_spell]['image'], (366, HEIGHT//4-64))
        font_render = font.render(spells[choised_spell]['fullname'], True, (0, 255, 255))
        sc.blit(font_render, ((WIDTH-font.size(spells[choised_spell]['fullname'])[0])//2, HEIGHT//4+64))

    font_render2 = font1.render(f'Score: {score}', True, (0, 255, 255))
    font_render3 = font1.render(f'Best Score: {best_score}', True, (0, 255, 255))

    sc.blit(font_render2, (10, 10))
    sc.blit(font_render3, (10, 30))

    if not lose:
        if not start:
            font_render1 = font.render('Press Enter to start', True, (0, 255, 255))
            sc.blit(font_render1, ((WIDTH-font.size('Press Enter to start')[0])/2, HEIGHT//4+320))
        else:
            time_diff = endtime - time.time()
            if time_diff <= 1:
                lose = True
            else:
                time_str = f'Time remaining: {int(time_diff)}'
                font_render1 = font.render(time_str, True, (0, 255, 255))
                sc.blit(font_render1, ((WIDTH-font.size(time_str)[0])/2, HEIGHT//4+320))
    else:
        font_render1 = font.render('You Lose! Press Enter to play', True, (255, 24, 0))
        sc.blit(font_render1, ((WIDTH-font.size('You Lose! Press Enter to play')[0])/2, HEIGHT//4+320))

    if lose or (not start):
        font_render4 = font1.render(f'Time 2 make spell: {time2makespell}s', True, (0, 255, 255))
        sc.blit(font_render4, (480, SLIDER_Y-8))
        pygame.draw.rect(sc, (200, 200, 200), (SLIDER_X, SLIDER_Y, SLIDER_WIDTH, SLIDER_HEIGHT))
        pygame.draw.rect(sc, (0, 255, 255), (SLIDER_X + slider_value * SLIDER_WIDTH - 10, SLIDER_Y - 5, 20, SLIDER_HEIGHT + 10))

    for i in range(len(current_spheres)):
        if current_spheres[i] == 'q':
            sc.blit(quas, (228+138*i, HEIGHT//2-64))
        if current_spheres[i] == 'w':
            sc.blit(wex, (228+138*i, HEIGHT//2-64))
        if current_spheres[i] == 'e':
            sc.blit(exort, (228+138*i, HEIGHT//2-64))

    for i in range(2):
        if current_spells[i]:
            sc.blit(spells[current_spells[i]]['image'], (430+138*i, HEIGHT-16-128))
        else:
            pygame.draw.rect(sc, (128, 128, 128), (430+138*i, HEIGHT-128-16, 128, 128), 5, border_radius=5)

    sc.blit(invoke, (706, HEIGHT-16-128))
    pygame.display.flip()
    clock.tick(FPS)

