import json

# Load file data
with open("shortcuts.json", "r") as f:
    json_data = json.load(f)

vdf_data = b"\x00"
vdf_data += b"shortcuts\x00"

strings = [
    "AppName",
    "Exe",
    "StartDir",
    "icon",
    "ShortcutPath",
    "LaunchOptions",
    "DevkitGameID"
]
bools = [
    "IsHidden",
    "AllowDesktopConfig",
    "AllowOverlay",
    "openvr",
    "Devkit"
]
other = [
    "LastPlayTime",
    "tags"
]

for id, shortcut in json_data["shortcuts"].items():
    # ID in array
    vdf_data += b"\x00%s\x00" % id.encode()

    # String variables
    for key in strings:
        variable = (key.encode(), shortcut[key].encode())
        vdf_data += b"\x01%s\x00%s\x00" % variable

    # Bool variables
    for key in bools:
        variable = (key.encode(), shortcut[key].to_bytes(
            3, byteorder="little"))
        vdf_data += b"\x02%s\x00%s\x00" % variable

    # Last play time
    key = "LastPlayTime"
    variable = (key.encode(), shortcut[key].to_bytes(4, byteorder="little"))
    vdf_data += b"\x02%s\x00%s\x00" % variable

    # Tags
    vdf_data += b"tags\x00"
    for id, tag in shortcut["tags"].items():
        variable = (id.encode(), tag.encode())
        vdf_data += b"\x01%s\x00%s\x00" % variable
    vdf_data += b"\x08"

    vdf_data += b"\x08"

vdf_data += b"\x08"
vdf_data += b"\x08"

# Write file data
filepath = "shortcuts.vdf"
with open(filepath, "wb") as f:
    f.write(vdf_data)
