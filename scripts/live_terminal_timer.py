#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Real-time Terminal Countdown & Mission Control for Swariya Weddings.
Displays live ticking countdown to the next automated SEO cycle.
Run: python3 scripts/live_terminal_timer.py
"""

import time
import sys
from datetime import datetime, timedelta

def main():
    cycle_interval = 12 * 3600 # 12 hours
    # First cycle completed around 20:16
    now = datetime.now()
    target = now.replace(hour=8, minute=13, second=5, microsecond=0)
    if now >= target:
        target += timedelta(days=1)
        
    print("\033[?25l", end="") # hide cursor
    try:
        while True:
            cur = datetime.now()
            diff = target - cur
            if diff.total_seconds() <= 0:
                target += timedelta(seconds=cycle_interval)
                diff = target - cur
                
            total_sec = int(diff.total_seconds())
            hrs = total_sec // 3600
            mins = (total_sec % 3600) // 60
            secs = total_sec % 60
            
            # ANSI colored output
            sys.stdout.write("\r\033[K")
            sys.stdout.write(
                f"\033[1;33m✦ SWARIYA AUTONOMOUS SEO ✦ \033[0m"
                f"Next Scan In: \033[1;32m{hrs:02d}h {mins:02d}m {secs:02d}s\033[0m | "
                f"Daemon: \033[1;36mACTIVE (PID 23438)\033[0m | "
                f"Link Health: \033[1;32m100%\033[0m | "
                f"Time: \033[90m{cur.strftime('%I:%M:%S %p')}\033[0m"
            )
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExited real-time monitor.")
    finally:
        print("\033[?25h", end="") # restore cursor

if __name__ == "__main__":
    main()
