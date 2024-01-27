# Export/Import Selenium Session to another computer
---
This repository contains Python scripts for **exporting any Selenium session**  and **import this session** back, on another  Selenium WebDriver instance.

## Usage
### Installation
1. Clone the repository:
```shell
git clone https://github.com/HugoCls/Import-Export-SeleniumSession
```
2. Install dependencies:
```shell
pip install -r requirements.txt
```

### Export a Session
1. You can either import the export_session() function into your code or modify export.py file.
```python
from session_exporter import export_session

# ... [Your code] ...

# Use export_session(driver) to save the session data
export_session(driver)

# ... [Continue with your code] ...
```

2. Run `export.py` or `[your_script].py`.

3. The session data, including cookies and storage information, will be exported to the `session.pkl` file.

### Import a Session
1. Change `https://yourwebsite.com` and run `import.py`.

2. The script will open a Chrome browser, navigate to your specified website, and import session data from the `session.pkl` file.

### License

This repository is under [MIT License](https://github.com/HugoCls/Import-Export-SeleniumSession/blob/main/LICENCE).