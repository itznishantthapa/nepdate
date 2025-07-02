# Nepali Date CLI

A simple command-line tool to display Nepali dates with beautiful boxed output and Nepali numerals (देवनागरी अंक).

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### 🍎 macOS Installation

#### Option 1: Using Homebrew (Recommended)
If you have [Homebrew](https://brew.sh/) installed:

```bash
# Install Python if not already installed
brew install python

# Install the package
pip3 install nepali-date-cli
```

#### Option 2: Using System Python
```bash
# Install using pip3 (recommended for macOS)
pip3 install nepali-date-cli

# If you encounter permission issues, use --user flag
pip3 install --user nepali-date-cli
```

#### Option 3: Using Virtual Environment (Best Practice)
```bash
# Create a virtual environment
python3 -m venv nepali-date-env

# Activate the virtual environment
source nepali-date-env/bin/activate

# Install the package
pip install nepali-date-cli

# To deactivate later (optional)
deactivate
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
pip3 install --upgrade nepali-date-cli
```

#### Windows:
```cmd
pip install --upgrade nepali-date-cli
```

### ⚠️ Troubleshooting

#### Common Issues and Solutions:

**macOS:**
- If you get "command not found: pip3", install Python via Homebrew: `brew install python`
- If permission denied, use: `pip3 install --user nepali-date-cli`
- For M1/M2 Macs, ensure you're using the correct Python architecture

**Windows:**
- If "pip is not recognized", add Python to your PATH or use: `python -m pip install nepali-date-cli`
- If you get permission errors, run Command Prompt as Administrator
- Ensure Python and pip are properly installed from [python.org](https://python.org)

**Both Platforms:**
- If the `miti` command is not found after installation, restart your terminal
- Use virtual environments to avoid conflicts with system packages

## 🚀 Usage

### Command Line Interface
After installation, you can use the `miti` command in your terminal:

#### macOS/Linux:
```bash
miti
```

#### Windows (Command Prompt):
```cmd
miti
```

#### Windows (PowerShell):
```powershell
miti
```

This will display both the current English date and the corresponding Nepali date with Nepali numerals in a beautiful boxed format.

> **⚠️ Note:** The old `nepdate` command is deprecated and will show a warning. Please use `miti` instead.

### Verifying Installation
To verify that the installation was successful, run:

```bash
miti --help    # Should show help information
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


