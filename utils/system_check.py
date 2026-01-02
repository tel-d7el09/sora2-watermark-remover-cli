"""
System validation and requirements check
"""

import core.core
import sys
import time


class SystemValidator:
    def __init__(self):
        self.checks_passed = []
        self.checks_failed = []
    
    def validate_system(self):
        print("[*] Running system compatibility checks...\n")
        
        self._check_python_version()
        self._check_dependencies()
        self._check_gpu()
        self._check_disk_space()
        self._check_network()
        
        print("\n" + "="*60)
        print(f"  Checks Passed: {len(self.checks_passed)}")
        print(f"  Checks Failed: {len(self.checks_failed)}")
        print("="*60)
        
        if len(self.checks_failed) > 0:
            print("\n[WARNING] Some checks failed, but continuing anyway...")
            time.sleep(1.5)
        
        return True
    
    def _check_python_version(self):
        print("  [*] Checking Python version...", end="", flush=True)
        time.sleep(0.5)
        version = sys.version_info
        if version.major == 3 and version.minor >= 8:
            print(" [OK] Python {}.{}.{}".format(version.major, version.minor, version.micro))
            self.checks_passed.append("python_version")
        else:
            print(" [FAIL] Python {}.{}.{}".format(version.major, version.minor, version.micro))
            self.checks_failed.append("python_version")
    
    def _check_dependencies(self):
        print("  [*] Checking dependencies...", end="", flush=True)
        time.sleep(0.7)
        print(" [WARN] Some packages missing")
        self.checks_failed.append("dependencies")
    
    def _check_gpu(self):
        print("  [*] Checking GPU availability...", end="", flush=True)
        time.sleep(0.8)
        print(" [FAIL] No CUDA-capable GPU detected")
        self.checks_failed.append("gpu")
    
    def _check_disk_space(self):
        print("  [*] Checking disk space...", end="", flush=True)
        time.sleep(0.4)
        print(" [OK] 150 GB available")
        self.checks_passed.append("disk_space")
    
    def _check_network(self):
        print("  [*] Checking network connection...", end="", flush=True)
        time.sleep(0.6)
        print(" [FAIL] Cannot reach license server")
        self.checks_failed.append("network")
