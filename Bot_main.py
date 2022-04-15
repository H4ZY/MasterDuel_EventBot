from typing import Counter
import pyautogui
import keyboard
import time
from termcolor import colored
from datetime import datetime



now = datetime.now()

current_time = now.strftime("%H:%M:%S")



def click_event(x, y):
    
    pyautogui.click(x, y)
    time.sleep(0)


def draw_card():
    
    if pyautogui.pixelMatchesColor(1530, 1001, (179, 167, 135)):
        #print(colored('[LOG]', 'yellow'), colored('Draw Card', 'blue'))
        print((current_time), ('[LOG] Draw Card'))
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)
        time.sleep(0.5)
        click_event(1900, 480)
        click_event(1900, 480)


def player_button():

    if pyautogui.pixelMatchesColor(1480, 439, (80, 147, 147)):
        #print(colored('[LOG]', 'yellow'), colored('Player Phase', 'blue'))
        print((current_time), ('[LOG] Player Phase'))

        time.sleep(0.5)
        click_event(1480, 439)
        #print(colored('[LOG]', 'yellow'), colored('skipping phase', 'blue'))
        print((current_time), ('[LOG] skipping phase'))
        time.sleep(0.5)
        click_event(1506, 780)
        #print(colored('[LOG]', 'yellow'), colored('skipped phase...', 'blue')) 
        print((current_time), ('[LOG] skipped phase...'))
        if pyautogui.pixelMatchesColor(965, 507, (62, 92, 127)):
            player_button()
           
        else:
            time.sleep(1)
          

def discart_card():
    
    if pyautogui.pixelMatchesColor(1391, 604, (59, 159, 247)):
        #print(colored('[LOG]', 'yellow'), colored('Card To Discard', 'blue'))
        print((current_time), ('[LOG] Card To Discard...'))
        time.sleep(0.5)
        click_event(588, 838)
        #print(colored('[LOG]', 'yellow'), colored('Selecting card', 'blue'))
        print((current_time), ('[LOG] Selecting card...'))
        time.sleep(0.5)
        click_event(968, 1020)
        #print(colored('[LOG]', 'yellow'), colored('discarded card', 'blue'))
        print((current_time), ('[LOG] Discarded card...'))

def enemy_button():
    
    if pyautogui.pixelMatchesColor(1510, 439, (151, 22, 17)):
    
        #print(colored('[LOG]', 'yellow'), colored('Enemy turn', 'red'))
        print((current_time), ('[LOG] Enemy turn'))


        #print(colored('[LOG]', 'yellow'), colored('Wait...', 'red'))
        print((current_time), ('[LOG] Wait...'))
        time.sleep(5)
    else:
        player_button()



def screen_defeat():
    
    if pyautogui.pixelMatchesColor(1418, 791, (223, 12, 62)):
        #print(colored('[LOG]', 'yellow'), colored('Defeat screen', 'magenta'))
        print((current_time), ('[LOG] Defeat screen'))
        time.sleep(2)
        click_event(964, 971)

        #counter = 0
       # while True:
           # counter += 1
           # print("TESTE COUNT", counter)
           # break
    else:
        player_button()


def screen_duelpass():
    
    if pyautogui.pixelMatchesColor(668, 268, (191, 193, 191)):
        #print(colored('[LOG]', 'yellow'), colored('skipping Duel Pass', 'magenta'))
        print((current_time), ('[LOG] skipping Duel Pass'))
        time.sleep(2)
        click_event(1590, 993)
        time.sleep(3)
        pyautogui.moveTo(100, 100)
        pyautogui.click(button='right')
        time.sleep(1)
        click_event(1703, 976)


def screen_duelresults():
    
    if pyautogui.pixelMatchesColor(42, 61, (48, 48, 48)):
        #print(colored('[LOG]', 'yellow'), colored('skipping Duel Results', 'magenta'))
        print((current_time), ('[LOG] skipping Duel Results'))       
        time.sleep(5)
        click_event(938, 639)  
        time.sleep(2)
        click_event(1703, 976)
        time.sleep(4)
        click_event(807, 629)  
        time.sleep(2)
        pyautogui.moveTo(1900, 10)
        pyautogui.click(button='right')

        #807, 629 203, 253, 0

def wincondition():
    
    if pyautogui.pixelMatchesColor(502, 479, (0, 79, 143)):
        print((current_time), ('[LOG] skipping Win Condition'))
        time.sleep(1)
        click_event(971, 652)
    else:
        button_duel()    

def button_duel():
    
    if pyautogui.pixelMatchesColor(1288, 854, (203, 253, 0)):
        #print(colored('[LOG]', 'yellow'), colored('Start Another Duel', 'magenta'))
        print((current_time), ('[LOG] Start Another Duel'))
        time.sleep(2)
        click_event(964, 788 )
        time.sleep(2)
        click_event(1590, 517)
        time.sleep(1)
        click_event(1480, 870)



def window_nocard():
    
    if pyautogui.pixelMatchesColor(1356, 374, (59, 159, 247)):
        #print(colored('[LOG]', 'yellow'), colored('Window no cards to apply effects', 'magenta'))
        print((current_time), ('[LOG] Window no cards to apply effects'))
        time.sleep(1)
        click_event(964, 589)
    else:
        player_button()

def window_enemy_card():
    
    if pyautogui.pixelMatchesColor(645, 774, (163, 26, 26)):
        #print(colored('[LOG]', 'yellow'), colored('Any enemy card to selected', 'magenta'))
        print((current_time), ('[LOG] Any enemy card to selected'))
        time.sleep(1)
        click_event(671, 840) #Select card
        time.sleep(1)
        click_event(962, 1011) #Ok Button
    else:
        player_button()


def card_01():
    
    if pyautogui.pixelMatchesColor(1284, 605, (59, 159, 247)):
        #print(colored('[LOG]', 'yellow'),colored('[CARD EFFECT]', 'green'), colored('Hand destruction', 'cyan'))
        print((current_time), ('[LOG] [CARD EFFECT] Hand destruction')) 
        time.sleep(1)
        click_event(669, 805)
        time.sleep(2)
        click_event(274, 805)
        time.sleep(2)
        click_event(963, 1015)
        time.sleep(2)
    else:
        player_button()


def card_02():
    
    if pyautogui.pixelMatchesColor(752, 787, (171, 171, 171)):
        #print(colored('[LOG]', 'yellow'),colored('[CARD EFFECT]', 'green'), colored('Toon page flip', 'cyan'))
        print((current_time), ('[LOG] [CARD EFFECT] Toon page flip'))
        time.sleep(1)
        click_event(813, 870)
        time.sleep(2)
        click_event(966, 1024)
    else:
        player_button()


def coin():
    
    if pyautogui.pixelMatchesColor(624, 823, (203, 253, 0)):
        #print(colored('[LOG]', 'yellow'), colored('Coin game Win, going first', 'magenta'))
        print((current_time), ('[LOG] Coin game Win, going first'))
        time.sleep(1)
        click_event(767, 839)
    else:
        player_button()

def errorserver():
    
    if pyautogui.pixelMatchesColor(928, 423, (237, 0, 74)):
        print((current_time), ('[LOG] Error Server'))
        time.sleep(1)
        click_event(971, 652)
    else:
        button_duel()



while keyboard.is_pressed('q') == False:

    draw_card()
    player_button()
    discart_card()
    enemy_button()
    screen_defeat()
    screen_duelpass()
    screen_duelresults
    button_duel()
    window_nocard
    window_enemy_card()
    card_01()
    card_02()
    coin()
    errorserver()
    wincondition()
