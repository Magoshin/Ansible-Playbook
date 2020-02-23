zabbix-server_ver40_rhel8
=========

 - Install zabbix server 4.0
 - Set up SNMPTT 1.4

Requirements
------------

 - Ansible 2.9
 - AWS
 - EC2 instance (RHEL 8)

Role Variables
--------------

◆roles

```
zabbix-server_ver40_rhel8
|-- defaults
|   +-- main.yml
|-- handlers
|   +-- main.yml
|-- meta
|   +-- main.yml
|-- README.md
|-- tasks
|   |-- main.yml
|   |-- Snmptt.yml
|   +-- ZabbixServer.yml
|-- templates
|   |-- client.cnf.j2
|   |-- httpd.conf.j2
|   |-- logrotate_snmptt.j2
|   |-- mariadb-server.cnf.j2
|   |-- mysql-clients.cnf.j2
|   |-- snmptrapd.conf.j2
|   |-- snmptt.conf.j2
|   |-- snmptt.ini.j2
|   |-- snmptt.service.j2
|   |-- zabbix.conf.j2
|   |-- zabbix.conf.php.j2
|   +-- zabbix_server.conf.j2
|-- tests
|   |-- inventory
|   +-- test.yml
+-- vars
    +-- main.yml
```

◆vars
common.yml
 - zabbix_db_password: zabbix DB password
 - zabbix_snmp_community: zabbix snmptrap community name

Dependencies
------------


Example Playbook
----------------


License
-------

BSD

Author Information
------------------

mgmjoke79_mgm

