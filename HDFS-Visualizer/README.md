# HDFS Web Management Console v2.0

A modern, dark-themed web interface for managing and interacting with the Hadoop Distributed File System (HDFS) using Python Flask.

---

![HDFS Console Screenshot](screenshot.png)

---

## Features

- Start / Stop HDFS and YARN services
- Check Hadoop processes via `jps`
- Browse HDFS directories
- View file contents
- Upload files to HDFS (`put`)
- Download files from HDFS (`get`)
- Copy & move files inside HDFS
- Create and remove directories
- Append local files to HDFS files
- Interactive terminal-style output panel with custom command input
- Clean, dark IDE-style UI

---

## Project Structure

```
project/
├── app.py              # Main Flask application
├── commands.py         # Shell/HDFS command execution
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # Jinja2 HTML template (redesigned UI)
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tasnim00ahmed/HDFS-Web-Management-Console.git
cd HDFS-Web-Management-Console
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Configure Hadoop

Make sure Hadoop and HDFS are installed and configured. Test with:

```bash
hdfs dfs -ls /
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## Supported Commands

| Operation        | HDFS Command             |
|------------------|--------------------------|
| List Files       | `hdfs dfs -ls`           |
| View File        | `hdfs dfs -cat`          |
| Upload File      | `hdfs dfs -put`          |
| Download File    | `hdfs dfs -get`          |
| Copy File        | `hdfs dfs -cp`           |
| Move File        | `hdfs dfs -mv`           |
| Remove File      | `hdfs dfs -rm -r`        |
| Create Directory | `hdfs dfs -mkdir`        |
| Append File      | `hdfs dfs -appendToFile` |

---

## Technologies Used

- Python + Flask
- HTML / CSS (vanilla, no frameworks)
- Jinja2 templating
- Hadoop HDFS / YARN
- JetBrains Mono & Syne fonts (Google Fonts CDN)
- Tabler Icons (CDN)

---

## Author

**Tasnim Ahmed** — Junior Big Data Engineer  
Faculty of Computers & Artificial Intelligence
