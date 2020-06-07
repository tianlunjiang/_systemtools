import platform, sys, os
import spt_slate as slate



__VERSION__='0.0'
__OS__=platform.system()
__AUTHOR__="Tianlun Jiang"
__COPYRIGHT__="copyright %s 2020" % __AUTHOR__

__TITLE__={
    'save': 'Workbench Saver',
    'load': 'Workbench Loader',
    'export': 'Workbench Exporter',
    'import': 'Workbench Importer'
}

TYPE_CONFIG = {
    'nuke':{
        'mastercomp': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'},
        'subcomp': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'},
        'lookdev': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'},
        'backplate': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'},
        'lgtSlap': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'},
        'breakdown': {'DIR': slate.NUKE_DIR, 'EXT': 'nk'}
        }
}

TYPE_NOPASSNAME={
'nuke': ['mastercomp', 'backplate', 'lgtSlap', 'lookdev', 'breakdown']
}

PADDING_VER, PADDING_FRAME = slate.SHOW_CONFIG['padding']
PADDING_FRAME = '%0{}d'.format(int(PADDING_FRAME))
