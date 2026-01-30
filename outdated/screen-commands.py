import os
def clear_screen():

    # 'nt' means Windows, 'posix' covers Mac and Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')