import Config as cfg
import ActivateAppWindow as window

# Getting the current screen resolution
current_screen_width, current_screen_height = cfg.pyag.size()

# Function to capture a screenshot
def capture_screenshot(save_path="capture1.png"):    
    # Starting point (x, y) percentage
    x = int(current_screen_width * 0)
    y = int(current_screen_height * 0)

    # Region width and height percentage
    region_width = int(current_screen_width * 0.85)
    region_height = int(current_screen_height * 0.17)

    # Capture the screenshot
    screenshot = cfg.pyag.screenshot(region=(x, y, region_width, region_height))

    # Save the screenshot to a file
    screenshot.save(save_path)
    print(f"Captura salva como {save_path}")
    
# Function to check if the screen resolution is correct    
def is_screen_resolution_correct():
    # Check if the screen resolution is correct
    if current_screen_width == cfg.SCREEN_WIDTH and current_screen_height == cfg.SCREEN_HEIGHT:
        print(f"Resolução da tela atual: {current_screen_width}x{current_screen_height}")
        return True
    else:
        return False

# Function to check if the application window is active 
# and capture the screenshot
def capture():
    if is_screen_resolution_correct():
        window.activate_window(cfg.WINDOW_ORDER)
        capture_screenshot()
    else:
        raise Exception(f"Resolução da tela incorreta. Mude para {cfg.SCREEN_WIDTH}x{cfg.SCREEN_HEIGHT}.")