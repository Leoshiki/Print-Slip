import Config as cfg

 # Function to press Esc key
def press_esc_key():
    cfg.pyag.press("esc")
    print("Janela fechada com Esc.")
    
# Function to maximize the window
def maximize_window():
    cfg.pyag.hotkey("win", "up")
    print("Janela maximizada.")