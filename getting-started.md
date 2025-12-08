---
layout: default
title: "Environment Setup Guide"
parent: Home
nav_order: 1
---

Complete this setup before attending training.

## Required Software

### 1. Python 3.10+

**macOS:**

```bash
brew install python@3.10
```

**Windows:**
Download from <https://python.org/downloads/>

**Linux:**

```bash
sudo apt update && sudo apt install python3.10 python3.10-venv
```

**Verify:**

```bash
python3 --version
# Should show Python 3.10.x or higher
```

### 2. VS Code (Recommended IDE)

Download from <https://code.visualstudio.com/>

**Recommended Extensions:**

- Python (Microsoft)
- Pylance
- Python Debugger

### 3. Docker Desktop

Download from <https://docker.com/products/docker-desktop>

**Verify:**

```bash
docker --version
docker compose version
```

### 4. ngrok

**macOS:**

```bash
brew install ngrok
```

**Windows/Linux:**
Download from <https://ngrok.com/download>

**Setup:**

1. Create free account at <https://ngrok.com>
2. Get your authtoken from dashboard
3. Configure ngrok:

```bash
ngrok config add-authtoken YOUR_TOKEN
```

**Verify:**

```bash
ngrok version
```

### 5. Git

**macOS:**

```bash
brew install git
```

**Windows:**
Download from <https://git-scm.com/>

**Verify:**

```bash
git --version
```

## Required Accounts

### SignalWire Account

1. Go to <https://signalwire.com>
2. Click "Get Started Free"
3. Complete registration
4. Note your:
   - Space name (e.g., `yourname.signalwire.com`)
   - Project ID
   - API Token

### ngrok Account

1. Go to <https://ngrok.com>
2. Create free account
3. Configure authtoken (see above)
4. Optional: Set up static domain for consistent URLs

## Training Environment Setup

### Create Working Directory

```bash
mkdir -p ~/signalwire-training
cd ~/signalwire-training
```

### Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### Install SignalWire Agents SDK

**Required version:** >= 1.0.11

```bash
pip install "signalwire-agents>=1.0.11"
```

### Verify Installation

```bash
# Check SDK imports
python -c "from signalwire_agents import AgentBase; print('SDK OK')"

# Check CLI tools
swaig-test --help
sw-agent-init --help
```

### Create Environment File (Optional)

You can store configuration in a `.env` file. To use it, install python-dotenv:

```bash
pip install python-dotenv
```

Create `.env` in your working directory:

```bash
# SignalWire Credentials (for future use)
SIGNALWIRE_SPACE_NAME=your-space
SIGNALWIRE_PROJECT_ID=your-project-id
SIGNALWIRE_TOKEN=your-api-token

# Agent Authentication (SDK reads these automatically)
SWML_BASIC_AUTH_USER=signalwire
SWML_BASIC_AUTH_PASSWORD=your-secure-password
```

> **Note:** The `.env` file is not loaded automatically. You must call `load_dotenv()` at the start of your agent script. See Module 1.4 for details.

## Pre-Training Checklist

- [ ] Python 3.10+ installed and working
- [ ] VS Code installed with Python extension
- [ ] Docker Desktop installed and running
- [ ] ngrok installed and authenticated
- [ ] Git installed
- [ ] SignalWire account created
- [ ] API credentials saved in `.env`
- [ ] SDK installed and verified
- [ ] CLI tools working

## Troubleshooting

### Python not found

```bash
# Try python3 instead of python
python3 --version

# Or specify full path on Windows
py -3.10 --version
```

### pip install fails

```bash
# Upgrade pip first
pip install --upgrade pip

# Then install SDK
pip install signalwire-agents
```

### ngrok connection issues

```bash
# Verify authtoken is set
ngrok config check

# Test tunnel
ngrok http 5000
```

### Docker not starting

- Ensure virtualization is enabled in BIOS
- On Windows, ensure WSL2 is installed
- Restart Docker Desktop

## Getting Help

- AI Agents SDK Documentation: <https://developer.signalwire.com/sdks/agents-sdk>
- SDK Repository: <https://github.com/signalwire/signalwire-agents>
- Training Support: Contact your instructor
