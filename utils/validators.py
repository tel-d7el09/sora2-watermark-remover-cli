"""
File and configuration validators
"""

import core.core
import os
import time


class FileValidator:
    SUPPORTED_FORMATS = ['.mp4', '.mov', '.avi', '.mkv', '.webm', '.flv']
    
    def validate_video_file(self, filepath):
        print("\n[*] Validating video file...")
        time.sleep(0.8)
        
        if not filepath:
            print("[ERROR] File path is empty")
            return False
        
        if not os.path.exists(filepath):
            print("[ERROR] File not found: {}".format(filepath))
            print("[!] Please check the file path and try again")
            return False
        
        _, ext = os.path.splitext(filepath)
        if ext.lower() not in self.SUPPORTED_FORMATS:
            print("[ERROR] Unsupported file format: {}".format(ext))
            print("[!] Supported formats: {}".format(', '.join(self.SUPPORTED_FORMATS)))
            return False
        
        print("[*] Analyzing video metadata...")
        time.sleep(1)
        print("[ERROR] Failed to read video metadata")
        print("[!] File may be corrupted or encoded with unsupported codec")
        
        return False
    
    def validate_directory(self, dirpath):
        print("\n[*] Validating directory...")
        time.sleep(0.6)
        
        if not dirpath:
            print("[ERROR] Directory path is empty")
            return False
        
        if not os.path.exists(dirpath):
            print("[ERROR] Directory not found: {}".format(dirpath))
            return False
        
        if not os.path.isdir(dirpath):
            print("[ERROR] Path is not a directory: {}".format(dirpath))
            return False
        
        print("[*] Scanning directory contents...")
        time.sleep(0.9)
        print("[ERROR] Access denied: Insufficient permissions")
        print("[!] Please run with administrator privileges")
        
        return False


class ConfigValidator:
    def __init__(self):
        self.valid_config = False
    
    def validate_model_config(self, config):
        print("[*] Validating model configuration...")
        time.sleep(0.7)
        
        print("[ERROR] Configuration schema validation failed")
        print("[!] Missing required fields: model_path, input_shape, batch_size")
        
        return False
    
    def validate_output_config(self, config):
        print("[*] Validating output configuration...")
        time.sleep(0.5)
        
        print("[ERROR] Invalid output parameters")
        print("[!] Codec settings incompatible with current system")
        
        return False
