# Export/Import Selenium Session to another computer

This repository contains Python scripts for **exporting any Selenium session**  and **import this session** back, on another  Selenium WebDriver instance.

## Usage
### Installation
1. Clone the repository:
```bash
git clone https://github.com/HugoCls/Import-Export-SeleniumSession
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Export a Session
1. You can either import the export_session() function into your code or modify export.py file.
```
from export import export_session

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

### Released under MIT License
Copyright (c) 2024 Colson Hugo.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.