#!/usr/bin/env python3

import shutil
import sys
import types

# Specify the application name you want to check
APP_NAME = "terraform"
APP_DESC = "Terra Form"

installedApps = [{"name":"ab", "desc":"Apache Bench"}, 
                 {"name":"terraform", "desc":"Terra Form"}, 
                 {"name":"git", "desc":"Git"}, 
                 {"name":"curl", "desc":"Curl"}, 
                 {"name":"dig", "desc":"dig"}]

def isAppInstalled(app):
    # Check if the application is installed
    if type(shutil.which(app['name'])) is types.NoneType:
        return False
    else:
        return True

for app in installedApps:
    print(f"Now checking {app['desc']}...")
    if not isAppInstalled(app):
        print(f" {app['desc']} is not installed.")
        sys.exit(1)
print("All Necessary Applications are Installed")

    
