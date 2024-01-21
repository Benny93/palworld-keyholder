from pynput import keyboard
import pyautogui
import time

f_key_pressed = False

def on_press(key):
    global f_key_pressed
    if key == keyboard.Key.f10:
        f_key_pressed = not f_key_pressed
        if f_key_pressed:
            press_key('f')
            print("'F' key pressed and held down.")
        else:
            release_key('f')
            print("'F' key released.")
        time.sleep(0.3)  # Debounce to avoid rapid toggling

    elif key == keyboard.Key.esc:
        stop_script()

def press_key(key):
    pyautogui.keyDown(key)

def release_key(key):
    pyautogui.keyUp(key)

def stop_script():
    global f_key_pressed
    if f_key_pressed:
        release_key('f')
        print("'F' key released.")
    exit()

with keyboard.Listener(on_press=on_press) as listener:
    print("Press F10 to toggle the 'F' key. Press Esc to exit.")
    listener.join()
