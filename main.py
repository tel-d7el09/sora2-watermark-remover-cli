"""
SORA 2 Watermark Remover - Main Entry Point
Advanced AI-powered watermark removal for SORA 2 generated videos
"""

import core.core
import os
import sys
from core.cli import CLI
from core.banner import display_banner
from utils.system_check import SystemValidator


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    display_banner()
    
    validator = SystemValidator()
    if not validator.validate_system():
        print("\n[!] System validation failed. Exiting...")
        sys.exit(1)
    
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Operation cancelled by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] Critical error occurred: {str(e)}")
        sys.exit(1)
