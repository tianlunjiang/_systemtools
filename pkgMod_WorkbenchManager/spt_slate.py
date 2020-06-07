'''

file to parse slate variables

'''



import json, os
from spt_kputl import *




SHOW = os.getenv('KP_SHOW')
SCENE = os.getenv('KP_SCENE')
SHOT = os.getenv('KP_SHOT')

if SHOW and SCENE and SHOT:
    SHOW_ROOT_DIR = r'k:/PROJECTS/Personal/'
    SHOW_DIR = joinPath(SHOW_ROOT_DIR, SHOW)
    SHOT_DIR = joinPath(SHOW_DIR, SHOT)
    SHOW_CONFIG_FILE = joinPath(SHOW_DIR, '_configShow.json')
    SHOT_CONFIG_FILE = joinPath(SHOT_DIR, '_configShot.json')

    RENDER_DIR = joinPath(SHOT_DIR, 'render/')
    ELEMENTS_DIR = joinPath(SHOT_DIR, 'assets', 'elements/')
    DELIVERY_DIR = joinPath(SHOW_DIR, '_delivery/')
    SHOW_TOOL_DIR = joinPath(SHOW_DIR, 'showtools/')

    NUKE_DIR = joinPath(SHOT_DIR, 'workbench', 'nuke/')
    MAYA_DIR = joinPath(SHOT_DIR, 'workbench', 'maya/scenes/')
    BLENDER_DIR = joinPath(SHOT_DIR, 'workbench', 'blender/')
    PS_DIR = joinPath(SHOT_DIR, 'workbench', 'ps/')
    AE_DIR = joinPath(SHOT_DIR, 'workbench', 'ae/')

    SHOW_CONFIG, SHOT_CONFIG = None, None
    try:
        with open(SHOW_CONFIG_FILE, 'r') as f:
            SHOW_CONFIG = json.load(f)
        with open(SHOT_CONFIG_FILE, 'r') as f:
            SHOT_CONFIG = json.load(f)
    except:
        print("No show/shot config file found ")
else:
    print("show enviroment not set up")
