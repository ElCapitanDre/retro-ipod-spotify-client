from wifi import Cell, Scheme
import threading
import time
import json


class SettingsEntry() :
    __slots__ = ['id', 'name', 'sub_entry']
    def __init__(self, id, name, sub_entry):
        self.id = id
        self.name = name
        self.sub_entry = sub_entry

    def __str__(self):
        return self.name

class SubSettingsEntry() :
    __slots__ = ['id', 'parent_setting_id', 'name']
    def __init__(self, id, parent_setting_id, name):
        self.id = id
        self.name = name
        self.parent_setting_id = parent_setting_id

    def __str__(self):
        return self.name

def get_settings_entries():
    return entries

def get_sub_settings_title(id):
    sub_entry = None
    for entry in entries:
        if(entry.id == id):
            sub_entry = entry
            break
    return sub_entry.name

def get_sub_settings_entries(id):
    sub_entry = None
    for entry in entries:
        if(entry.id == id):
            sub_entry = entry
            break
    return sub_entry.sub_entry

def get_wlan_networks():
    cell_list = list(Cell.all('wlan0'))
    return cell_list


entries = []

entries.append(SettingsEntry('0', 'Wi-Fi', [SubSettingsEntry('0_0', '0', 'Scan Networks'), SubSettingsEntry('0_1', '0', 'Connect Network')]))
entries.append(SettingsEntry('1', 'Bluetooth', [SubSettingsEntry('1_0', '0', 'Scan Devices'), SubSettingsEntry('1_1', '1', 'Connect Device')]))