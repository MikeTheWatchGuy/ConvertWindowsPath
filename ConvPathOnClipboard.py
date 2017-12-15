
#windows
import win32clipboard

'''
NO MORE manually adding \ into your Windows paths!!

python ConvPathOnClipboard.py

Windows program converts the text on the clipboard into a fully escaped and 'paste-able'
version.  Best used as part of two-step process.  Press Contrl+C to copy to clipboard
and then a hotkey like Control+Alt+C that you map so that it executes this program. Then 
do a normal paste into your favorite Python IDE.
There is no output so can be run hidden.

Utilizes the ascii built-in function

FUNCTION ConvPathOnClipboard.py
    Converts the path that is located on the clipboard into a string with escape
        characters when a special character is encountered

    When run stand-alone, the clipboard contents are modified using 'ascii' built-in func
    Usage:    
        Best used as a standalone program that is assigned to a hotkey
        This sets up these simple steps for the programmer:
            User copies source code to clipboard
            Hotkey is pressed or some other mechanism runs this program
            User pastes the modified text into their IDE or other app
ENJOY!
'''

# ====____====____==== ConvertClipboardToEscapedString ====____====____====____====____====___ #
# Converts all \ characters in the clipboard to \\                                             #
#   Best used by binding a hotkey to the execution of this program.                            #
#  ------------------------------------------------------------------------------------------- #
def ConvertClipboardToEscapedString():
    # ----------------------- Open + Read the Clipboard ----------------------- #
    win32clipboard.OpenClipboard()
    clipboard = win32clipboard.GetClipboardData()
    # ----------------------- Do the convert ----------------------- #
    new_clipboard = ascii(clipboard)

    # ----------------------- Set the Clipboard to modified version ----------------------- #
    if new_clipboard is not None:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(new_clipboard)
    # ----------------------- Close the Clipboard ----------------------- #
    win32clipboard.CloseClipboard()
    return

# ====____====____==== MAIN ====____====____====____====____====___  #
# If run directly, convert the clipboard text                        #
# ------------------------------------------------------------------ #
if __name__ == '__main__':
    ConvertClipboardToEscapedString()
