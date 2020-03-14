""" Game fix Jade Empire: Special Edition
"""
#pylint: disable=C0103

import threading
import os
import subprocess

def _taskset():
    """Use taskset to set mask of JadeEmpire.exe"""
    # avoiding an external library as proc should be available on linux
    again = True
    badexes = ['JadeEmpire.exe']
    while again:
        pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
        for pid in pids:
            try:
                with open(os.path.join('/proc', pid, 'cmdline'), 'rb') as proc_cmd:
                    cmdline = proc_cmd.read()
                    for exe in badexes:
                        if exe in cmdline.decode():
                            mask = subprocess.check_output(['taskset', '-p', str(pid)])
                            while 'mask: 1' not in str(mask):
                                mask = subprocess.check_output(['taskset', '-p', str(pid)])
                            res = subprocess.check_output(['taskset', '-p', '4', str(pid)])
                            again = False
            except IOError:
                continue

def main():
    """ Set mask of JadeEmpire.exe after it is running """
    thread = threading.Thread(target=_taskset, args=())
    thread.daemon = False
    thread.start()
