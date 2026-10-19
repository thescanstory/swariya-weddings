#!/bin/bash
# Install macOS LaunchAgent for Swariya Autonomous SEO Optimizer
PLIST_PATH="$HOME/Library/LaunchAgents/com.swariya.seo.daemon.plist"
SCRIPT_PATH="/Users/mac/Documents/swariya-weddings-complete-project/scripts/autonomous_optimizer_daemon.py"
PYTHON_PATH="$(which python3)"
PROJECT_DIR="/Users/mac/Documents/swariya-weddings-complete-project"

cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.swariya.seo.daemon</string>
    <key>ProgramArguments</key>
    <array>
        <string>$PYTHON_PATH</string>
        <string>$SCRIPT_PATH</string>
    </array>
    <key>WorkingDirectory</key>
    <string>$PROJECT_DIR</string>
    <key>StartInterval</key>
    <integer>43200</integer>
    <key>StandardOutPath</key>
    <string>$PROJECT_DIR/reports/daemon_stdout.log</string>
    <key>StandardErrorPath</key>
    <string>$PROJECT_DIR/reports/daemon_stderr.log</string>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
EOF

launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"
echo "✅ Swariya Autonomous SEO Daemon installed and loaded successfully!"
echo "📍 Plist: $PLIST_PATH"
echo "🕒 Interval: Every 12 hours (automated background execution)"
