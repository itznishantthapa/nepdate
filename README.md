# Nepali Date CLI

A simple command-line tool to display Nepali dates with beautiful boxed output and Nepali numerals (देवनागरी अंक).

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### 🍎 macOS Installation

#### Option 1: Using pipx (For Homebrew-managed Python)
If you have Python installed via [Homebrew](https://brew.sh/) and get "externally-managed-environment" errors, use pipx:

```bash
# Install pipx if you don't have it
brew install pipx

# Install the package
pipx install nepali-date-cli
```

#### Option 2: Using pip3 (Standard Installation)
For most macOS systems, try this first:

```bash
# Install using pip3
pip3 install nepali-date-cli

# If you encounter permission issues, use --user flag
pip3 install --user nepali-date-cli
```

#### Option 3: Using Virtual Environment (Recommended)
This is the safest method that avoids system conflicts:
```bash
# Create a virtual environment
python3 -m venv nepali-date-env

# Activate the virtual environment
source nepali-date-env/bin/activate

# Install the package
pip install nepali-date-cli

# The 'miti' command is now available in this environment
miti

# To deactivate later (optional)
deactivate
```

#### Option 4: Using Homebrew Python (Alternative)
```bash
# Install Python via Homebrew if not already done
brew install python

# Try installing directly
pip3 install nepali-date-cli
```

#### Option 5: Override System Protection (Last Resort)
Only use this if other methods don't work:

```bash
# This bypasses the safety check - use with caution
pip3 install --break-system-packages nepali-date-cli
```

### 🪟 Windows Installation

#### Option 1: Using Command Prompt
```cmd
# Install the package
pip install nepali-date-cli
```

#### Option 2: Using PowerShell
```powershell
# Install the package
pip install nepali-date-cli

# If you encounter execution policy issues, try:
python -m pip install nepali-date-cli
```

#### Option 3: Using Virtual Environment
```cmd
# Create a virtual environment
python -m venv nepali-date-env

# Activate the virtual environment
nepali-date-env\Scripts\activate

# Install the package
pip install nepali-date-cli

# To deactivate later (optional)
deactivate
```

### 🔄 Upgrading to Latest Version

#### macOS:
```bash
# If using pipx (for Homebrew-managed Python)
pipx upgrade nepali-date-cli

# If using pip3 (standard installation)
pip3 install --upgrade nepali-date-cli

# If using virtual environment
source nepali-date-env/bin/activate
pip install --upgrade nepali-date-cli

# If using system install with override (last resort)
pip3 install --upgrade --break-system-packages nepali-date-cli
```

#### Windows:
```cmd
pip install --upgrade nepali-date-cli
```

### ⚠️ Troubleshooting

#### Common Issues and Solutions:

**macOS - "externally-managed-environment" Error:**
```
error: externally-managed-environment
× This environment is externally managed
```

This error occurs when Python is managed by Homebrew. **Solutions (in order of preference):**

1. **Use pipx (Specifically for Homebrew-managed Python):**
   ```bash
   brew install pipx
   pipx install nepali-date-cli
   ```

2. **Use Virtual Environment:**
   ```bash
   python3 -m venv nepali-date-env
   source nepali-date-env/bin/activate
   pip install nepali-date-cli
   ```

3. **Force install (Not recommended):**
   ```bash
   pip3 install --break-system-packages nepali-date-cli
   ```

**Other macOS Issues:**
- If you get "command not found: pip3", install Python via Homebrew: `brew install python`
- Try `pip3 install nepali-date-cli` first - it works on many systems
- For M1/M2 Macs, ensure you're using the correct Python architecture

**Windows:**
- If "pip is not recognized", add Python to your PATH or use: `python -m pip install nepali-date-cli`
- If you get permission errors, run Command Prompt as Administrator
- Ensure Python and pip are properly installed from [python.org](https://python.org)

**Windows - 'miti' command not found after installation:**
If you see warnings during installation or the `miti` command doesn't work even after successful installation, this indicates Python is not correctly configured in your system environment variables.

**Solutions:**

1. **Reinstall Python from Official Source (Recommended):**
   - Download Python from the official website: [python.org](https://python.org/downloads/)
   - During installation, **CHECK** "Add Python to PATH" option
   - Restart your Command Prompt/PowerShell after installation
   - Verify installation: `python --version` and `pip --version`

2. **Manually Add Python to PATH:**
   ```cmd
   # Find Python installation path (usually):
   # C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\
   # C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts\
   
   # Add both paths to your system PATH environment variable
   ```

3. **Use Full Python Path:**
   ```cmd
   # If PATH is not configured, use full path
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python3x\Scripts\miti.exe
   ```

4. **Verify Installation Paths:**
   ```cmd
   # Check where pip installed the package
   pip show nepali-date-cli
   
   # Check Scripts directory
   where miti
   ```

**Windows Installation Warnings:**
- If you see warnings about "Scripts directory not in PATH"
- Or "Consider adding this directory to PATH"
- This confirms Python environment variables need configuration

**Both Platforms:**
- If the `miti` command is not found after installation, restart your terminal
- Use virtual environments to avoid conflicts with system packages
- For Windows: If `miti` still doesn't work after restart, check Python PATH configuration
- Verify successful installation with: `pip show nepali-date-cli`

## 🚀 Usage

### Command Line Interface
After installation, you can use the `miti` command:

#### If using pipx or system install:
```bash
miti
```

#### If using virtual environment:
```bash
# First activate the environment
source nepali-date-env/bin/activate

# Then run the command
miti
```

#### Windows:
```cmd
miti
```

This will display both the current English date and the corresponding Nepali date with Nepali numerals in a beautiful boxed format.

> **⚠️ Note:** The old `nepdate` command is deprecated and will show a warning. Please use `miti` instead.

### Verifying Installation
To verify that the installation was successful, run:

**All Platforms:**
```bash
miti --help    # Should show help information
pip show nepali-date-cli    # Shows package details
```

**Windows - Additional Verification:**
```cmd
# Check if miti is in PATH
where miti

# If not found, check Python Scripts directory
dir C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python3*\Scripts\miti*

# Alternative way to run if PATH issues
python -c "import nepali_date_cli; print('Package installed successfully')"
```

## 📸 Example Output

```
┌─────────────────────────────────────────────────────────┐
│                     Today's Date                        │
├─────────────────────────────────────────────────────────┤
     नेपाली मिति    २०८२-३-१४ (असार १४)      शनिबार       
     English Date   2025-06-28 (June 28)     Saturday       
└─────────────────────────────────────────────────────────┘
```

## ✨ Features

- ✅ Displays current English date with day name
- 🔢 Shows Nepali date in Devanagari numerals (देवनागरी अंक)
- 📅 Includes Nepali day names (e.g., आइतबार, सोमबार, etc.)
- 🎨 Beautiful boxed output format
- 💻 Simple command-line interface
- 🐍 Can be used as a Python module
- 🌍 Cross-platform support (Windows, macOS, Linux)

## 🔧 Requirements

- Python 3.6+
- nepali-datetime package (automatically installed)

## 📚 Additional Resources

### Getting Help
- For command-line help: `miti --help`
- For issues and bug reports: [GitHub Issues](https://github.com/yourusername/nepali-date-cli/issues)

### Development
This project is open source and contributions are welcome! Check out the source code on GitHub.

---

**Made with ❤️ for the Nepali community**


