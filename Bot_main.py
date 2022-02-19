import pyautogui
import keyboard
import time
from termcolor import colored




def click_event(x, y):
    
    pyautogui.click(x, y)
    time.sleep(0)


def draw_card():
    
    if pyautogui.pixelMatchesColor(1530, 1001, (179, 167, 135)):
        print(colored('[LOG]', 'yellow'), colored('Draw Card', 'blue'))
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)


def botao_azul():

    if pyautogui.pixelMatchesColor(1480, 439, (80, 147, 147)):
        print(colored('[LOG]', 'yellow'), colored('Player Phase', 'blue'))
        time.sleep(0.5)
        click_event(1480, 439)
        print(colored('[LOG]', 'yellow'), colored('skipping phase', 'blue'))
        time.sleep(0.5)
        click_event(1506, 780)
        print(colored('[LOG]', 'yellow'), colored('skipped phase...', 'blue')) 
        if pyautogui.pixelMatchesColor(965, 507, (62, 92, 127)):
            botao_azul()
           
        else:
            time.sleep(1)
          

def discart_card():
    
    if pyautogui.pixelMatchesColor(1391, 604, (59, 159, 247)):
        print(colored('[LOG]', 'yellow'), colored('Card To Discard', 'blue'))
        time.sleep(0.5)
        click_event(588, 838)
        print(colored('[LOG]', 'yellow'), colored('Selecting card', 'blue'))
        time.sleep(0.5)
        click_event(968, 1020)
        print(colored('[LOG]', 'yellow'), colored('discarded card', 'blue'))

def botao_vermelho():
    
    if pyautogui.pixelMatchesColor(1510, 439, (151, 22, 17)):
        print(colored('[LOG]', 'yellow'), colored('Enemy turn', 'red'))
        print(colored('[LOG]', 'yellow'), colored('Wait...', 'red'))
        time.sleep(5)
    else:
        botao_azul()


def screen_defeat():
    
    if pyautogui.pixelMatchesColor(1418, 791, (223, 12, 62)):
        print(colored('[LOG]', 'yellow'), colored('Defeat screen', 'magenta'))
        time.sleep(2)
        click_event(964, 971)
    else:
        botao_azul()


def screen_duelpass():
    
    if pyautogui.pixelMatchesColor(668, 268, (191, 193, 191)):
        print(colored('[LOG]', 'yellow'), colored('skipping Duel Pass', 'magenta'))
        time.sleep(2)
        click_event(1590, 993)
        time.sleep(3)
        pyautogui.moveTo(100, 100)
        pyautogui.click(button='right')
        time.sleep(1)
        click_event(1703, 976)


def screen_duelresults():
    
    if pyautogui.pixelMatchesColor(42, 61, (48, 48, 48)):
        print(colored('[LOG]', 'yellow'), colored('skipping Duel Results', 'magenta'))
        time.sleep(2)
        pyautogui.moveTo(100, 100)
        pyautogui.click(button='right')
        time.sleep(1)
        click_event(1703, 976)
        time.sleep(4)
        pyautogui.moveTo(1900, 10)
        pyautogui.click(button='right')

def screen_XYZEvent():
    
    if pyautogui.pixelMatchesColor(1685, 518, (26, 32, 5)):
        print(colored('[LOG]', 'yellow'), colored('Receiving Rewards', 'magenta'))
        time.sleep(2)
        pyautogui.moveTo(1900, 10)
        pyautogui.click(button='right')


def button_duel():
    
    if pyautogui.pixelMatchesColor(1288, 854, (203, 253, 0)):
        print(colored('[LOG]', 'yellow'), colored('Clicking Start Another Duel', 'magenta'))
        time.sleep(2)
        click_event(1590, 517)
        time.sleep(1)
        click_event(1480, 870)



def window_nocard():
    
    if pyautogui.pixelMatchesColor(1356, 374, (59, 159, 247)):
        print(colored('[LOG]', 'yellow'), colored('Window no cards to apply effects', 'magenta'))
        time.sleep(1)
        click_event(964, 589)
    else:
        botao_azul()

def window_enemy_card():
    
    if pyautogui.pixelMatchesColor(645, 774, (163, 26, 26)):
        print(colored('[LOG]', 'yellow'), colored('Any enemy card to selected', 'magenta'))
        time.sleep(1)
        click_event(671, 840) #Select card
        time.sleep(1)
        click_event(962, 1011) #Ok Button
    else:
        botao_azul()


def card_01():
    
    if pyautogui.pixelMatchesColor(1284, 605, (59, 159, 247)):
        print(colored('[LOG]', 'yellow'),('[CARD EFFECT]', 'green'), colored('Hand destruction', 'cyan'))
        time.sleep(1)
        click_event(669, 805)
        time.sleep(2)
        click_event(274, 805)
        time.sleep(2)
        click_event(963, 1015)
        time.sleep(2)
    else:
        botao_azul()


def card_02():
    
    if pyautogui.pixelMatchesColor(752, 787, (171, 171, 171)):
        print(colored('[LOG]', 'yellow'),('[CARD EFFECT]', 'green'), colored('Toon page flip', 'cyan'))
        time.sleep(1)
        click_event(813, 870)
        time.sleep(2)
        click_event(966, 1024)
    else:
        botao_azul()


def coin():
    
    if pyautogui.pixelMatchesColor(624, 823, (203, 253, 0)):
        print(colored('[LOG]', 'yellow'), colored('Coin Win, going first', 'magenta'))
        time.sleep(1)
        click_event(767, 839)
    else:
        botao_azul()

while keyboard.is_pressed('q') == False:

    draw_card()
    botao_azul()
    discart_card()
    botao_vermelho()
    screen_defeat()
    screen_duelpass()
    screen_duelresults
    screen_XYZEvent
    button_duel()
    window_nocard
    window_enemy_card()
    card_01()
    card_02()
    coin()