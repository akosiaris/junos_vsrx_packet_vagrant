#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def main():
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    confs = []
    for neighbor in root.iter('lldp-neighbor-information'):
        localif = neighbor.find('lldp-local-interface').text
        remoteif = neighbor.find('lldp-remote-port-description').text
        remotesys = neighbor.find('lldp-remote-system-name').text
        confs.append('''
    %(localif)s {
        description "%(remotesys)s - %(remoteif)s"
    }
''' % {
                'localif': localif,
                'remoteif': remoteif,
                'remotesys': remotesys,
        })
    with open(sys.argv[2], 'w') as f:
        f.write('interfaces {')
        f.write(''.join(confs))
        f.write('}\n')


if __name__ == '__main__':
    main()
