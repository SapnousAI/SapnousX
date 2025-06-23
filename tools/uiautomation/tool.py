try:
    import pyautogui
    uiauto_available = True
except ImportError:
    uiauto_available = False

def move_mouse(x, y):
    if not uiauto_available:
        return 'pyautogui not installed.'
    pyautogui.moveTo(x, y)
    return f'Mouse moved to ({x},{y})'

def click_mouse():
    if not uiauto_available:
        return 'pyautogui not installed.'
    pyautogui.click()
    return 'Mouse clicked.'
