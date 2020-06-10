'''

Functions per application for:
- Saving, Loading, Importing, Exporting

'''


#------------------------------------------------------------------------------
#-Global Variables
#------------------------------------------------------------------------------




import spt_Globals as glb
import spt_slate as slate
from spt_kputl import joinPath




#------------------------------------------------------------------------------
#-Main Functions
#------------------------------------------------------------------------------




def gui_save(gui_app, filename):
    '''saving functions
    @gui_app: current application, KP_GUI (str)
    @filename: save file, full file path (str)
    '''

    if gui_app == 'nuke':
        import nuke
        nuke.scriptSave(filename)
        print('saved: %s' % filename)


def gui_load(gui_app, filename):
    '''loading Functions
    @gui_app: current application, KP_GUI (str)
    @filename: load file, full file path (str)
    '''

    if gui_app == 'nuke':
        import nuke
        nuke.scriptClose()
        nuke.scriptOpen(filename)
        print('open: %s' % filename)
