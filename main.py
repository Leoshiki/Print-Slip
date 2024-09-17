import Config as cfg
import CaptureInfo as capinfo
import ActivateAppWindow as window
import AutoGui as autogui

print("INICIANDO PROGRAMA")

########################### MODULE 1 ###########################
# Ensuring the main application is running and active
def activate_main_window():
    try:
        # Activate the application window
        window.activate_window(cfg.WINDOW_MAIN)
    except Exception as e:
        print(f"Erro: {e}")
        cfg.sys.exit(1)

    # Waiting for the application window to be activated
    cfg.time.sleep(1)
    print(f"\n1: JANELA {cfg.WINDOW_MAIN} ATIVADA COM SUCESSO")
################################################################


########################### MODULE 2 ###########################
# Preparing the order window for capturing
# Function to prepare the order window for capturing
def prepare_order_window():
    # Activate the order window
    try:
        window.activate_window(cfg.WINDOW_ORDER)
    except Exception as e:
        print(f"Erro: {e}")
        cfg.sys.exit(1)

    print(f"\n2: JANELA {cfg.WINDOW_ORDER} ATIVADA COM SUCESSO")

    # Checking if the missing products window is open and closing it
    if window.is_window_open(cfg.WINDOW_MISSINGPRODUCT):
        window.bring_window_to_foreground(cfg.WINDOW_MISSINGPRODUCT)
        autogui.press_esc_key()
        # Activate the order window again to maximize it
        try:
            window.activate_window(cfg.WINDOW_ORDER)
        except Exception as e:
            print(f"Erro: {e}")
            cfg.sys.exit(1)
    print(f"\n2: JANELA {cfg.WINDOW_MISSINGPRODUCT} FECHADA")

    # Maximizing the order window
    autogui.maximize_window()
    cfg.time.sleep(0.5)
################################################################


########################### MODULE 3 ###########################
# Capturing the first item
def capture_order_window():
    try:
        capinfo.capture()
    except Exception as e:
        print(f"Erro: {e}")
        cfg.sys.exit(1)

    # Waiting and closing the order window
    cfg.time.sleep(1)
    print("\n3: CAPTURA REALIZADA") 
    autogui.press_esc_key()
################################################################


########################### MODULE 4 ###########################
# Transforming the saved capture into text


################################################################


# Main function to run the program
try:
    activate_main_window()
    prepare_order_window()
    capture_order_window()
except Exception as e:
    print(f"Erro fatal: {e}")
    cfg.sys.exit(1)

print("\nCONCLUÍDO")