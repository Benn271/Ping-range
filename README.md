# Overview
Ping  all ip addresses within a given range.

# Creation Reason
To indicate most, if not all, of the alive ip addresses within your given range allowing you to run further scans - like nmap. 

# Features
* Given a range of ip addresses, it will ping all where the last octet is the only octet changed in order to     see all alive hosts.
* Shows the ping results in terminal.
  # V2 Features - Release date TBD
  * Supports any octet change.
  * Uses threading for faster results.
  # Potential Later Versions
  * Output to a file that is specified.
  * GUI
  
# Installation
    # Linux
    1. Run the following commands in the terminal
    ```
    sudo apt-get update
    sudo apt-get install python3
    sudo apt-get install python-pip3
    sudo git clone https://github.com/Benn271/Ping-range/tree/main
    cd Ping-range
    sudo pip3 install -r requirements.txt
    ```
    
    # Windows
    1. Run the following commands in cmd
    ```
    @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
    choco install -y python3
    curl https://bootst/rap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```
    2. Download the zip of the Ping-range code file from github
    3. Run the following commands in Powershell
    ```
    pip3 install -r requirements.txt
    ```

# How to use

```
python3 ping.py -h (help page) -start <start ip> -end <end ip>
```

# License
I am not responsible for any misuse of this tool. Any trouble you get into with this tool is not tied back to me. I just make educational tools. It may not show all alive hosts, it just pings and it is up to you to interpret the data.

