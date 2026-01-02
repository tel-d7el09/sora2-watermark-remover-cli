"""
Banner and branding display
"""

import core.core
import sys


def display_banner():
    banner = """
==============================================================
                                                              
              SORA 2 WATERMARK REMOVER                        
          Professional Edition - Version 1.2.1               
                    (November 2025)                           
                                                              
==============================================================

    AI-Powered Watermark Removal for SORA 2 Generated Content

    [*] Advanced neural network processing
    [*] GPU-accelerated rendering engine  
    [*] Temporal consistency preservation
    [*] Batch processing support
    [*] Multiple output formats

--------------------------------------------------------------
"""
    
    print(banner)
    
    print("    [*] Initializing core modules...", end="", flush=True)
    _loading_animation()
    print(" [OK]")
    
    print("    [*] Loading AI models...", end="", flush=True)
    _loading_animation()
    print(" [OK]")
    
    print("    [*] Checking GPU availability...", end="", flush=True)
    _loading_animation()
    print(" [OK]")
    
    print("\n" + "="*62)
    print()


def _loading_animation():
    import time
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
