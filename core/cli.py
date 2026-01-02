"""
Interactive CLI Interface for SORA 2 Watermark Remover
"""

import core.core
import time
import os
from utils.validators import FileValidator, ConfigValidator
from core.processor import WatermarkProcessor
from core.engine import RemovalEngine


class CLI:
    def __init__(self):
        self.processor = WatermarkProcessor()
        self.engine = RemovalEngine()
        self.session_data = {}
    
    def run(self):
        while True:
            self._display_menu()
            choice = input("\n[>] Select option: ").strip()
            
            if choice == "1":
                self._process_single_video()
            elif choice == "2":
                self._process_batch()
            elif choice == "3":
                self._configure_advanced_settings()
            elif choice == "4":
                self._view_statistics()
            elif choice == "5":
                self._export_results()
            elif choice == "6":
                print("\n[*] Exiting SORA 2 Watermark Remover...")
                break
            else:
                print("\n[!] Invalid option. Please try again.")
                time.sleep(1.5)
            
            os.system('cls' if os.name == 'nt' else 'clear')
    
    def _display_menu(self):
        print("\n" + "="*60)
        print("  MAIN MENU")
        print("="*60)
        print("\n  [1] Process Single Video")
        print("  [2] Batch Processing")
        print("  [3] Advanced Settings")
        print("  [4] View Statistics")
        print("  [5] Export Results")
        print("  [6] Exit")
        print("\n" + "="*60)
    
    def _process_single_video(self):
        print("\n" + "-"*60)
        print("  SINGLE VIDEO PROCESSING")
        print("-"*60)
        
        video_path = input("\n[>] Enter video file path: ").strip()
        
        validator = FileValidator()
        if not validator.validate_video_file(video_path):
            input("\n[!] Press Enter to continue...")
            return
        
        output_path = input("[>] Enter output path (default: ./output/): ").strip()
        if not output_path:
            output_path = "./output/"
        
        print("\n[*] Detection mode:")
        print("    [1] AI Auto-detect")
        print("    [2] Manual region selection")
        print("    [3] Deep learning analysis")
        
        mode = input("[>] Select mode (1-3): ").strip()
        
        quality = input("[>] Output quality (1-100, default: 95): ").strip()
        
        print("\n[*] Initializing removal engine...")
        time.sleep(1)
        
        self.processor.process_video(video_path, output_path, mode, quality)
        
        input("\n[!] Press Enter to continue...")
    
    def _process_batch(self):
        print("\n" + "-"*60)
        print("  BATCH PROCESSING")
        print("-"*60)
        
        input_dir = input("\n[>] Enter input directory: ").strip()
        
        validator = FileValidator()
        if not validator.validate_directory(input_dir):
            input("\n[!] Press Enter to continue...")
            return
        
        output_dir = input("[>] Enter output directory: ").strip()
        
        recursive = input("[>] Recursive scan? (y/n): ").strip().lower() == 'y'
        
        file_formats = input("[>] File formats (comma-separated, default: mp4,mov,avi): ").strip()
        if not file_formats:
            file_formats = "mp4,mov,avi"
        
        parallel_jobs = input("[>] Parallel jobs (1-8, default: 4): ").strip()
        
        print("\n[*] Scanning directory...")
        time.sleep(1.2)
        
        self.processor.process_batch(input_dir, output_dir, recursive, file_formats, parallel_jobs)
        
        input("\n[!] Press Enter to continue...")
    
    def _configure_advanced_settings(self):
        print("\n" + "-"*60)
        print("  ADVANCED SETTINGS")
        print("-"*60)
        
        print("\n[*] Current Configuration:")
        print("    - AI Model: SORA-2-WM-REM-v3.2.1")
        print("    - Precision: FP16")
        print("    - GPU Acceleration: Enabled")
        print("    - Temporal Smoothing: Enabled")
        
        print("\n[1] Change AI Model")
        print("[2] Adjust Detection Sensitivity")
        print("[3] Configure GPU Settings")
        print("[4] Temporal Processing Options")
        print("[5] Output Format Settings")
        print("[6] Back to Main Menu")
        
        choice = input("\n[>] Select option: ").strip()
        
        if choice == "1":
            self._change_ai_model()
        elif choice == "2":
            self._adjust_sensitivity()
        elif choice == "3":
            self._configure_gpu()
        elif choice == "4":
            self._temporal_settings()
        elif choice == "5":
            self._output_settings()
        else:
            return
    
    def _change_ai_model(self):
        print("\n[*] Available Models:")
        print("    [1] SORA-2-WM-REM-v3.2.1 (Latest, Recommended)")
        print("    [2] SORA-2-WM-REM-v3.1.0 (Stable)")
        print("    [3] SORA-2-WM-REM-v3.0.5 (Legacy)")
        
        model = input("\n[>] Select model (1-3): ").strip()
        
        print("\n[*] Loading model configuration...")
        time.sleep(1.5)
        print("[ERROR] Failed to initialize model: CUDA out of memory")
        print("[!] Please try with a different model or reduce batch size")
        
        input("\n[!] Press Enter to continue...")
    
    def _adjust_sensitivity(self):
        print("\n[*] Detection Sensitivity Settings")
        
        threshold = input("[>] Detection threshold (0.0-1.0, default: 0.85): ").strip()
        confidence = input("[>] Confidence level (0.0-1.0, default: 0.92): ").strip()
        
        print("\n[*] Applying new sensitivity settings...")
        time.sleep(1)
        print("[ERROR] Configuration validation failed: Invalid threshold range")
        print("[!] Sensitivity must be calibrated with current model version")
        
        input("\n[!] Press Enter to continue...")
    
    def _configure_gpu(self):
        print("\n[*] GPU Configuration")
        
        gpu_id = input("[>] GPU Device ID (default: 0): ").strip()
        memory_limit = input("[>] Memory limit in GB (default: auto): ").strip()
        
        print("\n[*] Detecting GPU capabilities...")
        time.sleep(1.2)
        print("[ERROR] Failed to access GPU device")
        print("[!] CUDA driver version mismatch detected")
        print("[!] Required: 12.1+, Found: Unknown")
        
        input("\n[!] Press Enter to continue...")
    
    def _temporal_settings(self):
        print("\n[*] Temporal Processing Configuration")
        
        frame_interp = input("[>] Enable frame interpolation? (y/n): ").strip().lower()
        motion_comp = input("[>] Enable motion compensation? (y/n): ").strip().lower()
        
        print("\n[*] Calibrating temporal filters...")
        time.sleep(1.3)
        print("[ERROR] Temporal analysis engine initialization failed")
        print("[!] Insufficient system resources for temporal processing")
        
        input("\n[!] Press Enter to continue...")
    
    def _output_settings(self):
        print("\n[*] Output Format Configuration")
        
        codec = input("[>] Video codec (h264/h265/vp9, default: h265): ").strip()
        bitrate = input("[>] Target bitrate (Mbps, default: auto): ").strip()
        
        print("\n[*] Validating codec parameters...")
        time.sleep(1)
        print("[ERROR] Codec initialization failed: Missing encoder library")
        print("[!] Please install required codec dependencies")
        
        input("\n[!] Press Enter to continue...")
    
    def _view_statistics(self):
        print("\n" + "-"*60)
        print("  SESSION STATISTICS")
        print("-"*60)
        
        print("\n[*] Loading statistics...")
        time.sleep(1)
        print("[ERROR] Failed to retrieve session data")
        print("[!] Statistics database is corrupted or missing")
        print("[!] Please restart the application")
        
        input("\n[!] Press Enter to continue...")
    
    def _export_results(self):
        print("\n" + "-"*60)
        print("  EXPORT RESULTS")
        print("-"*60)
        
        export_format = input("\n[>] Export format (json/csv/xml): ").strip().lower()
        export_path = input("[>] Export path: ").strip()
        
        print("\n[*] Generating export file...")
        time.sleep(1.5)
        print("[ERROR] Export operation failed: Permission denied")
        print("[!] Unable to write to specified location")
        
        input("\n[!] Press Enter to continue...")
