#!usr/bin/env python

import pandas as pd
import json

class FilterModule:

    @staticmethod
    def filters():
        return {
            'json_to_dict': FilterModule.json_to_dict
        }

    @staticmethod
    def json_to_dict(text):
        r = json.dumps(text)
        return_dict = json.loads(r)
        return return_dict
