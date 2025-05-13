
# Requires: `playwright` and working script_18 + script_21 logic
# Crontab or Task Scheduler recommended for true hourly automation

import os
import subprocess
import time
from datetime import datetime

log_root = "patchlog"
os.makedirs(log_root, exist_ok=True)

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(log_root, "script_22_hourly_monitor_log.txt"), "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {msg}\n")

try:
    log("🚀 Hourly Netlify check started.")

    # Step 1: Crawl live errors
    log("Running script_18_netlify_error_crawler.py...")
    subprocess.run(["python", "script_18_netlify_error_crawler.py"], check=True)

    # Step 2: Re-map errors to source files
    log("Running script_19_match_live_errors_to_source.py...")
    subprocess.run(["python", "script_19_match_live_errors_to_source.py"], check=True)

    # Step 3: Auto-repair overlays and modules
    log("Running script_21_live_symbolic_patch_monitor.py...")
    subprocess.run(["python", "script_21_live_symbolic_patch_monitor.py"], check=True)

    log("✅ Hourly cycle complete.\n")

except subprocess.CalledProcessError as e:
    log(f"❌ Subprocess failed: {e}")
except Exception as e:
    log(f"❌ Unexpected error: {e}")
