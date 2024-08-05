#!/bin/env python3

# The script opens predefined websites using python dictionaries

import json
import webbrowser

# Load JSON
with open('urls.json') as f:
    file = json.load(f)

# Open each URL in a separate tab
for item in file["links"]:
    webbrowser.open_new_tab(item)
        
