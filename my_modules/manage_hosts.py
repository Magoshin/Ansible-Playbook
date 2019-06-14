#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import shutil
import logging
import os
import subprocess
from ansible.module_utils.basic import AnsibleModule


def make_hostsfile(output_path, this_ipaddr, hostname_key, this_index, digit):

    with open(output_path, 'a') as fd:
        num_str = str(this_index)
        this_line = \
            this_ipaddr + " " + hostname_key + num_str.zfill(digit) + "\n"
        fd.write(this_line)


def prepare():

    ansible_logpath = "/var/log/ansible_module.log"
    if os.path.exists(ansible_logpath):
        pass
    else:
        cmd = "sudo touch " + ansible_logpath
        rslt = subprocess.call(cmd, shell=True)

    cmd = "sudo chmod 666 " + ansible_logpath
    rslt = subprocess.call(cmd, shell=True)

    logger = logging.getLogger('LoggingTest')
    logger.setLevel(10)
    fh = logging.FileHandler(ansible_logpath)
    logger.addHandler(fh)
    sh = logging.StreamHandler()
    logger.addHandler(sh)


if __name__ == '__main__':

    #prepare()

    module = AnsibleModule(
        argument_spec=dict(
            inventry_path=dict(required=True),
            output_path=dict(required=True),
            origin_hostsfile=dict(required=False),
            groupname=dict(required=True),
            hostname_key=dict(required=False),
            digit=dict(required=False),
            inheri_switch=dict(required=False)
        ),
        supports_check_mode=True
    )

    inventry_path_param = module.params['inventry_path']
    output_path_param = module.params['output_path']
    origin_hostsfile_param = module.params['origin_hostsfile']
    groupname_param = module.params['groupname']
    hostname_key_param = module.params['hostname_key']
    digit_param = module.params['digit']
    inheri_switch_param = module.params['inheri_switch']

    if module.check_mode:
        module.exit_json(changed=False , msg=inventry_path_param, mode='check mode')
    else :
        module.exit_json(changed=False , msg=inventry_path_param)
    
    # default
    #inventry_path = "/home/ansible/inventry"
    #output_path = "/home/ansible/hostsfile"
    origin_hostsfile = "/etc/hosts"
    groupname = "elasticsearch_cluster"
    hostname_key = "elasticsearch"
    digit = 2
    inheri_switch = 1

    module = AnsibleModule({})
    module.log("info log")
    module.debug("debug log")
    module.exit_json()

    startword = "[" + groupname + "]"
    line_index = 1
    start_index = 0
    end_flag = 0
    host_index = 1

    if inheri_switch == 1:
        shutil.copyfile(origin_hostsfile, output_path)

    with open(inventry_path, 'r') as fd:
        for row in fd:
            if row.find(startword) >= 0:
                start_index = line_index
            if start_index != 0 and line_index > (start_index):
                if len(row.strip()) == 0:
                    end_flag = 1
                test = re.match(r'\[', row.strip())
                if end_flag != 1:
                    result = make_hostsfile(output_path,
                                            row.strip(),
                                            hostname_key,
                                            host_index,
                                            digit)
                    host_index += 1

            line_index += 1

    result = line_index
    module.exit_json(**result)
