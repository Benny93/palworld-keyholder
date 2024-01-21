from pynput import keyboard
import pyautogui
import time
import sys

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

def on_release(key):
    if key == keyboard.Key.esc:
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
    sys.exit()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        print("Press F10 to toggle the 'F' key. Press Ctrl+C to exit.")
        listener.join()
    except KeyboardInterrupt:
        stop_script()
