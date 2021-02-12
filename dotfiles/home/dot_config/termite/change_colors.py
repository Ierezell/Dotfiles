import os
import json

termite_conf = open(os.path.join(os.path.expanduser('~'),'.config','termite','config') ,'w')

with open(os.path.join(os.path.expanduser('~'),'.cache','wal','colors.json') ,'r') as color_file : 
    colors = json.load(color_file)


termite_conf.write(
"""
[options]
#allow_bold = true
#audible_bell = false
#bold_is_bright = true
#cell_height_scale = 1.0
#cell_width_scale = 1.0
#clickable_url = true
#dynamic_title = true
font = Monospace 9
#fullscreen = true
#icon_name = terminal
#mouse_autohide = false
#scroll_on_output = false
#scroll_on_keystroke = true
# Length of the scrollback buffer, 0 disabled the scrollback buffer
# and setting it to a negative value means "infinite scrollback"
scrollback_lines = 10000
#search_wrap = true
#urgent_on_bell = true
#hyperlinks = false

# $BROWSER is used by default if set, with xdg-open as a fallback
#browser = xdg-open

# "system", "on" or "off"
#cursor_blink = system

# "block", "underline" or "ibeam"
#cursor_shape = block

# Hide links that are no longer valid in url select overlay mode
#filter_unmatched_urls = true

# Emit escape sequences for extra modified keys
#modify_other_keys = false

# set size hints for the window
#size_hints = false

# "off", "left" or "right"
#scrollbar = off
""")

termite_conf.write("[colors]\n")
for name, color in list(colors['special'].items())+list(colors["colors"].items()):
    termite_conf.write(f"{name} = {color}\n")


termite_conf.close()
