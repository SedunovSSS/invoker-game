import pygame
import time
import random
import json
pygame.init()

spells = {
    'qqq': {
        'fullname': 'Cold Snap',
        'image': pygame.image.load('spells/invoker_cold_snap.png')
    },
    'qqw': {
        'fullname': 'Ghost Walk',
        'image': pygame.image.load('spells/invoker_ghost_walk.png')
    },
    'eqq': {
        'fullname': 'Ice Wall',
        'image': pygame.image.load('spells/invoker_ice_wall.png')
    },
    'www': {
        'fullname': 'E.M.P',
        'image': pygame.image.load('spells/invoker_emp.png')
    },
    'qww': {
        'fullname': 'Tornado',
        'image': pygame.image.load('spells/invoker_tornado.png')
    },
    'eww': {
        'fullname': 'Alacrity',
        'image': pygame.image.load('spells/invoker_alacrity.png')
    },
    'eee': {
        'fullname': 'Sun Strike',
        'image': pygame.image.load('spells/invoker_sun_strike.png')
    },
    'eeq': {
        'fullname': 'Forge Spirit',
        'image': pygame.image.load('spells/invoker_forge_spirit.png')
    },
    'eew': {
        'fullname': 'Chaos Meteor',
        'image': pygame.image.load('spells/invoker_chaos_meteor.png')
    },
    'eqw': {
        'fullname': 'Deafening Blast',
        'invoke': 'qwe',
        'image': pygame.image.load('spells/invoker_deafening_blast.png')
    },
}

quas = pygame.image.load('spells/invoker_quas.png')
wex = pygame.image.load('spells/invoker_wex.png')
exort = pygame.image.load('spells/invoker_exort.png')
invoke = pygame.image.load('spells/invoker_invoke.png')

font = pygame.font.SysFont('Arial', 50, bold=True)
font1 = pygame.font.SysFont('Arial', 20, bold=True)

WIDTH, HEIGHT = 860, 860
FPS = 666

score = 0
best_score = json.load(open('best.json', 'r'))['best_score']

sc = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
pygame.display.set_caption('Invoker Game')
pygame.display.set_icon(pygame.image.load('spells/invoker.png'))

running = True
lose = False

current_spheres = ''
current_spells = [None]*2

choised_spell = random.choice(list(spells.keys()))
endtime = time.time() + 6

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
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
                        score += 100*int(time_diff)
                        if score >= best_score:
                            best_score = score
                            json.dump({'best_score': best_score}, open('best.json', 'w'), indent=4)
                        new_choised_spell = random.choice(list(spells.keys()))
                        while new_choised_spell == choised_spell:
                            new_choised_spell = random.choice(list(spells.keys()))
                        choised_spell = new_choised_spell
                        endtime = time.time() + 6
        elif i.type == pygame.KEYDOWN and lose:
            if i.key == pygame.K_RETURN:
                current_spheres = ''
                current_spells = [None]*2
                score = 0
                new_choised_spell = random.choice(list(spells.keys()))
                while new_choised_spell == choised_spell:
                    new_choised_spell = random.choice(list(spells.keys()))
                choised_spell = new_choised_spell
                lose = False
                endtime = time.time() + 6

        elif i.type == pygame.MOUSEBUTTONDOWN and not lose:
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
                        score += 100*int(time_diff)
                        if score >= best_score:
                            best_score = score
                            json.dump({'best_score': best_score}, open('best.json', 'w'), indent=4)
                        new_choised_spell = random.choice(list(spells.keys()))
                        while new_choised_spell == choised_spell:
                            new_choised_spell = random.choice(list(spells.keys()))
                        choised_spell = new_choised_spell
                        endtime = time.time() + 6

            if len(current_spheres) > 3:
                current_spheres = current_spheres[-3:]

    sc.fill('black')
    sc.blit(quas, (16, HEIGHT-16-128))
    sc.blit(wex, (154, HEIGHT-16-128))
    sc.blit(exort, (292, HEIGHT-16-128))

    sc.blit(spells[choised_spell]['image'], (356, HEIGHT//4-64))
    font_render = font.render(spells[choised_spell]['fullname'], True, (255, 255, 255))
    sc.blit(font_render, ((WIDTH-font.size(spells[choised_spell]['fullname'])[0])/2, HEIGHT//4+64))

    font_render2 = font1.render(f'Score: {score}', True, (255, 255, 255))
    font_render3 = font1.render(f'Best Score: {best_score}', True, (255, 255, 255))

    sc.blit(font_render2, (10, 10))
    sc.blit(font_render3, (10, 50))

    if not lose:
        time_diff = endtime - time.time()
        if int(time_diff) <= 0:
            lose = True
        time_str = f'Time remaining: {int(time_diff)}'
        font_render1 = font.render(time_str, True, (255, 255, 255))
        sc.blit(font_render1, ((WIDTH-font.size(time_str)[0])/2, HEIGHT//4+320))
    else:
        font_render1 = font.render('You Lose!', True, (255, 255, 255))
        sc.blit(font_render1, ((WIDTH-font.size('You Lose!')[0])/2, HEIGHT//4+320))

    for i in range(len(current_spheres)):
        if current_spheres[i] == 'q':
            sc.blit(quas, (218+138*i, HEIGHT//2-64))
        if current_spheres[i] == 'w':
            sc.blit(wex, (218+138*i, HEIGHT//2-64))
        if current_spheres[i] == 'e':
            sc.blit(exort, (218+138*i, HEIGHT//2-64))

    for i in range(2):
        if current_spells[i]:
            sc.blit(spells[current_spells[i]]['image'], (430+138*i, HEIGHT-16-128))
        else:
            pygame.draw.rect(sc, (128, 128, 128), (430+138*i, HEIGHT-128-16, 128, 128), 5, border_radius=5)

    sc.blit(invoke, (706, HEIGHT-16-128))
    pygame.display.flip()
    clock.tick(FPS)
