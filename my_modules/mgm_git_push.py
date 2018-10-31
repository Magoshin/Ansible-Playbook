#!/usr/bin/env python
import subprocess
import os
import datetime
import logging

from ansible.module_utils.basic import *

logpath = "/home/ansible/log/ansible_module.log"
logger = logging.getLogger('LoggingTest')
logger.setLevel(10)
fh = logging.FileHandler(logpath)
logger.addHandler(fh)
sh = logging.StreamHandler()
logger.addHandler(sh)

def main():

    module = AnsibleModule(
        argument_spec = dict(
            src_dir=dict(required=True),
            git_user=dict(required=True)
        ),
        #supports_check_mode=True
        supports_check_mode=False
    )

    if module.check_mode:
        module.exit_json(changed=False)

    src_dir = module.params['src_dir']
    git_user = module.params['git_user']

    d = datetime.datetime.today()
    nowdatestr = d.strftime("%Y-%m-%d %H:%M:%S")
    os.chdir(src_dir)

    # update README
##    readmepath = src_dir + "/README.md"
##    os.remove(readmepath)
##    readme_fd = open(readmepath,'w')
##    readme_fd.write("this is the Infra as Code\n")
##    readme_fd.write("update: " + nowdatestr)
##    readme_fd.close

##    file_list0 = subprocess.check_output(['ls'],shell=True)
##    file_list = file_list0.replace('\n',' ')
##    cmd1 = ("git add " + file_list)
    cmd1 = ("git add .")
    cmd1_res = subprocess.call(cmd1, shell=True)

    # logging
##    logger.warning(file_list)
##    logger.warning(cmd1_res)

    cmd2 = ("git commit -m '" + nowdatestr + "'")
    cmd2_res = subprocess.call(cmd2, shell=True)

    # logging
    logger.warning(cmd2)
    logger.warning(cmd2_res)

    cmd3 = ("git push origin master")
    cmd3_res = subprocess.call(cmd3, shell=True)

if __name__ == '__main__':
    main()
