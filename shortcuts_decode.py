import json
import re


def find(x, y):
    return re.search(x, y).group(1)


# Load file data
userid = "215954729"
filepath = "C:/Program Files (x86)/Steam/userdata/%s/config/shortcuts.vdf" % userid
with open(filepath, "rb") as f:
    data = f.read()
pattern = rb"\x00\d+\x00.*?\x08\x08"
shortcut_strings = re.findall(pattern, data)

shortcuts = {}
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

for shortcut_string in shortcut_strings:
    shortcut = {
        "tags": {}
    }

    # ID in array
    pattern = rb"\x00(\d+)\x00"
    id = find(pattern, shortcut_string).decode()

    # String variables
    for key in strings:
        pattern = rb"\x01%b\x00(.*?)\x00" % bytes(key, "utf-8")
        shortcut[key] = find(pattern, shortcut_string).decode()

    # Bool variables
    for key in bools:
        pattern = rb"\x02%b\x00(\x00|\x01)\x00\x00\x00" % bytes(key, "utf-8")
        shortcut[key] = find(pattern, shortcut_string) == b"\x01"

    # Last play time
    pattern = rb"\x02LastPlayTime\x00(.*?)\x00"
    time_string = find(pattern, shortcut_string)
    time_value = int.from_bytes(time_string, byteorder="little")
    shortcut["LastPlayTime"] = time_value

    # Tags
    pattern = rb"tags\x00(.*?)\x08\x08"
    tags_string = find(pattern, shortcut_string)
    pattern = rb"\x01(\d+)\x00(.*?)\x00"
    tags_strings = re.findall(pattern, tags_string)
    for tag in tags_strings:
        shortcut["tags"][tag[0].decode()] = tag[1].decode()

    shortcuts[id] = shortcut

with open("shortcuts.json", "w") as f:
    json.dump({"shortcuts": shortcuts}, f, indent=4, sort_keys=True)
