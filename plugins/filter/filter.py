#!usr/bin/env python

import re

class FilterModule:

    @staticmethod
    def filters():
        return {
            'ios_inventory': FilterModule.ios_inventory
        }

    @staticmethod
    def ios_inventory(text):
        ios_inventory = ['inventory' + s for s in text.split('inventory') if s]
        return_dict = {}
        for inventory in ios_inventory:
            # Parse the NAME from the inventory
            name_regex = re.compile(r'NAME: \D(?P<name1>\w+\w\s\w+)\D|NAME: \D(?P<name2>\w+)\D')
            name_match = name_regex.search(inventory)
            sub_dict = {}
            name_dict = {name_match.group('name'): sub_dict}
  
            # Parse the PID from the following string
            pid_regex = re.compile(r'PID: (\S*(?P<pid>\S*)')
            pid_matches = pid_regex.findall(inventory)
            sub_dict.update({'PID': pid_matches})
  
            # Parse the SN from the following string
            sn_regex = re.compile(r'SN: (\S*(?P<sn>)\S*)')
            sn_matches = sn_regex.findall(inventory)
            sub_dict.update({'SN': sn_matches})
  
            ## Append dictionary to return list
            return_dict.update(inventory_dict)
      
        return return_dict
