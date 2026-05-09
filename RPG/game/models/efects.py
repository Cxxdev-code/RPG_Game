from colorama import Fore, Style
import os

class Efects:
    def __init__(self):
        pass
    
    
    def clear_screen(self,):
        os.system('cls' if os.name == 'nt' else 'clear')

    
    def print_success(self,message):
        print(f"{Fore.GREEN}{message}{Style.RESET_ALL}")

    
    def print_error(self,message):
        print(f"{Fore.RED}{message}{Style.RESET_ALL}")

    
    def print_info(self,message):
        print(f"{Fore.CYAN}{message}{Style.RESET_ALL}")

    
    def print_warning(self,message):
        print(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

    
    def print_battle(self,message):
        print(f"{Fore.MAGENTA}{message}{Style.RESET_ALL}")
