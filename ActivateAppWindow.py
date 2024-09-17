import Config as cfg

# Function to check if the main application process is running
def is_main_process_running():
    for proc in cfg.psutil.process_iter(['pid', 'name']):
        try:
            if cfg.PROCESS_MAIN.lower() in proc.info['name'].lower():
                print(f"O processo \"{cfg.PROCESS_MAIN}\" está rodando em segundo plano.")
                return True
        except (cfg.psutil.NoSuchProcess, cfg.psutil.AccessDenied, cfg.psutil.ZombieProcess):
            pass
    return False

# Function to check if the window with the specified title is open
def is_window_open(window_title):
    windows = cfg.pygw.getWindowsWithTitle(window_title)
    if windows:
        print(f"Janela \"{window_title}\" encontrada.")
        return True
    return False

# Function to bring the application window to the foreground
def bring_window_to_foreground(window_title):
    windows = cfg.pygw.getWindowsWithTitle(window_title)
    if windows:
        window = windows[0]
        if not window.isActive:
            if window.isMinimized:
                print(f"Restaurando janela minimizada \"{window_title}\".")
                window.restore()
            window.activate()
            print(f"Trazendo \"{window_title}\" para a frente.")
        else:
            print(f"A janela \"{window_title}\" já está ativa.")
    else:
        raise Exception(f"Não foi possível ativar a janela \"{window_title}\". Abra o aplicativo e tente novamente.")

# Main function to ensure the app is running and active
def activate_window(WINDOW):
    if is_main_process_running() and is_window_open(WINDOW):
        bring_window_to_foreground(WINDOW)
    else:
        raise Exception(f"\"{cfg.PROCESS_MAIN}\" não está rodando ou a janela \"{WINDOW}\" não está aberta.")