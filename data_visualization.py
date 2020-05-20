# A formatted hexdump template of shortcuts.vdf
# Key:
#   ... = string
#   tf = true or false, little endian, \x00\x00\x00 or \x01\x00\x00
#   time = unix epoch, little endian
rb'''
\x00 shortcuts \x00
    \x00 0 \x00
        \x01 AppName \x00 ... \x00
        \x01 Exe \x00 ... \x00
        \x01 StartDir \x00 ... \x00
        \x01 icon \x00 ... \x00
        \x01 ShortcutPath \x00 ... \x00
        \x01 LaunchOptions \x00 ... \x00
        \x02 IsHidden \x00 tf \x00
        \x02 AllowDesktopConfig \x00 tf \x00
        \x02 AllowOverlay \x00 tf \x00
        \x02 openvr \x00 tf \x00
        \x02 Devkit \x00 tf \x00
        \x01 DevkitGameID \x00 ... \x00
        \x02 LastPlayTime \x00 time \x00
        tags \x00
            \x01 0 \x00 ... \x00
        \x08\x08
\x08\x08
'''

# A formatted JSON template of shortcuts.json
{
    "shortcuts": {
        "0": {
            "AllowDesktopConfig": false,
            "AllowOverlay": false,
            "AppName": "",
            "Devkit": false,
            "DevkitGameID": "",
            "Exe": "",
            "IsHidden": false,
            "LastPlayTime": 0,
            "LaunchOptions": "",
            "ShortcutPath": "",
            "StartDir": "",
            "icon": "",
            "openvr": false,
            "tags": {
                "0": ""
            }
        }
    }
}
