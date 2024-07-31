#!/bin/env python3

# The script opens predefined websites using python dictionaries

import webbrowser

url = {
        "https://www.bleepingcomputer.com/",
        "https://securityaffairs.co/wordpress/",
        "https://hbr.org/",
        "https://www.theregister.com/",
        "https://www.hackread.com/",
        "https://www.information-age.com/",
        "https://www.darkreading.com/",
        "https://hackaday.com/",
        "https://www.nextgov.com/",
        "https://www.technologyreview.com/",
        "https://www.infosecurity-magazine.com/",
        "https://www.cyberscoop.com/",
        "https://krebsonsecurity.com/",
        }

for i in url:
    webbrowser.open(i)
