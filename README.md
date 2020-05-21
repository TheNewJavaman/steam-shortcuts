# steam-shortcuts
A couple tools to edit your non-Steam games cache

# help
Get and push changes to C:/Program Files (x86)/Steam/userdata/{id}/config/shortcuts.vdf

Steps:
1. Copy shortcuts.vdf to local folder
2. Decode using script
3. Change shortcuts.json file to your preferences
4. Encode using script
5. Copy shortcuts.vdf to Steam config folder

# file overview
- data_visualization.py : shows file structures of shortcuts.vdf and shortcuts.json
- shortcuts_decode.py : convert shortcuts.vdf to shortcuts.json
- shortcuts_encode.py : convert shortcuts.json to shortcuts.vdf