# Development Environment Setup

This guide will help you set up your development environment on Windows installing the following tools:

- Chocolatey
- WSL2
- Docker Desktop
- Git for Windows
- VS Code
- Dagger

## Prerequisites

- Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11.
- Ensure you have PowerShell installed on your system. You can use the built-in PowerShell that comes with Windows.

## Step 1: Install Chocolatey

First, install Chocolatey, a package manager for Windows.

1. Open PowerShell as an Administrator.
2. Run the following command to install Chocolatey:

    ```powershell
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    ```

## Step 2: Install WSL2

1. Enable the WSL feature:

    ```powershell
    wsl --install
    ```

2. Set WSL2 as the default version:

    ```powershell
    wsl --set-default-version 2
    ```

3. Install a Linux distribution (e.g., Ubuntu):

    ```powershell
    wsl --install -d Ubuntu
    ```

## Step 3a: Install Docker Desktop [Option A]

1. Install Docker Desktop using Chocolatey:

    ```powershell
    choco install docker-desktop
    ```

2. After installation, start Docker Desktop from the Start menu.

3. Ensure Docker is configured to use WSL2:

    - Open Docker Desktop settings.
    - Go to the "General" tab and check "Use the WSL 2 based engine".

## Step 3b: Install Rancher Desktop [Option B]

1. Install Rancher Desktop using Chocolatey:

    ```powershell
    choco install rancher-desktop
    ```

2. After installation, start Rancher Desktop from the Start menu.

3. Ensure Rancher is configured to use `dockerd`:

    - Go to Preferences.
    - Select Container Engine.
    - Choose `dockerd (moby)` as the container engine.

## Step 4: Install Git for Windows

1. Install Git for Windows using Chocolatey:

    ```powershell
    choco install git
    ```

2. Verify the installation:

    ```powershell
    git --version
    ```

### Step 4.1: Configure Git

1. Set your username:

    ```powershell
    git config --global user.name "Your Name"
    ```

2. Set your email:

    ```powershell
    git config --global user.email "your.email@example.com"
    ```

## Step 5: Install Visual Studio Code

1. Install Visual Studio Code using Chocolatey:

    ```powershell
    choco install vscode
    ```

2. Verify the installation by launching Visual Studio Code from the Start menu or by running:

    ```powershell
    code --version
    ```

## Step 6: Dagger CLI

1. Install Dagger CLI using Chocolatey:

    ```powershell
    choco install dagger
    ```

2. Verify the installation:

    ```powershell
    dagger version
    ```

You have now successfully set up your development environment on Windows using PowerShell and Chocolatey.
