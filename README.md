# System Health Monitor

A small Python script that records CPU, RAM, and disk usage to a log file and warns when CPU or disk usage gets high. It's a learning project, so it's intentionally simple.

## Status

**Completed:**
- Reads CPU, RAM, and disk usage with `psutil`
- Prints one timestamped line per run
- Appends each reading to `logs/health.log` without overwriting earlier entries
- Writes a `WARNING` line when CPU is above 80% or disk is above 90%

## Requirements

- Linux, or Windows with WSL2 (tested on Debian under WSL)
- Python 3 with venv support (`sudo apt install -y python3-venv`)

## Setup

```bash
cd ~/System-Health-Monitor
python3 -m venv venv
source venv/bin/activate
pip install psutil
```

## Usage

```bash
source venv/bin/activate
python health.py
```

Each run prints a line like this and appends the same line to `logs/health.log`: