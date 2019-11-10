import json
import subprocess

def parse_config(configfile):
    """
    reads configs saved as json record in configuration file and returns them
    :type configfile: str       path to config file
    :rtype          : dict      configs
    """
    conf = json.load(open(configfile, "r"))
    return replace_envvars_with_vals(conf)

def replace_envvars_with_vals(dic):
    """
    for a dictionary dic which may contain values of the form "$varname",
    replaces such values with the values of corresponding environmental variables
    :type dic: dict     dictionary where to parse environmental variables
    :rtype   : dict     dictionary with parsed environmental variables
    """
    for el in dic.keys():
        val = dic[el]
        if type(val) is dict:
            val = replace_envvars_with_vals(val)
        else:
            if type(val) in [str] and len(val) > 0 and '$' in val:
                command = "echo {}".format(val)
                dic[el] = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().strip()
    return dic