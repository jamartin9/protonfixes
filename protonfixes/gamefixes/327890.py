""" Game fix I am bread
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Needs: force directx11 dimensions """
    sys.argv.append('-force-d3d11 -screen-width 1280 -screen-height 720')
