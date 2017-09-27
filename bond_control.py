#!/usr/bin/env python
# coding:utf8
# By:dub

import os
import sys
from dialog import Dialog
import psutil
import subprocess


#TODO ip,netmask,gate Valid
class BondControl(object):
    net_home_dir = '/sys/class/net/'

    def __init__(self):
        self.ui = Dialog(dialog='dialog')
        self.ui.set_background_title("RAID Control")
        self.bond_list = self.get_bond()
        self.ethernets = self.get_net()
        self.edit_bond_ethernets = []
        self.bond = ""
        self.CREATE = False
        self.bond_ip = ""
        self.bond_mask = ""
        self.bond_gate = ""
        self.bond_detail = []

    def get_bond(self):
        file_list = os.listdir(self.net_home_dir)
        tmp=[]
        for item in file_list:
            if item.startswith('bond') and os.path.isdir(self.net_home_dir+item):
                tmp.append(item)
        return tmp

    def get_net(self):
        net_list = []
        file_list = os.listdir(self.net_home_dir)
        for key in file_list:
            if key != 'lo' and not key.startswith('bond'):
                if not os.path.exists(self.net_home_dir+'/%s/%s'%(key,
                    'bonding_slave')):
                    net_list.append(key)
        return net_list

    def start(self):
        code, tags = self.ui.menu(u"选择",
                                  choices=[
                                      ("1", u"新建bond"),
                                      ("2", u"编辑bond")
                                  ])
        if code == u"ok":
            if tags == u"1":
                self.CREATE = True
                self.second_create_step()
            else:
                self.CREATE = False
                self.second_edit_step()

    def second_create_step(self):
        bondindex = 0
        while "bond%d" % bondindex in self.get_bond():
            bondindex += 1

        self.bond = "bond%d" % bondindex
        choices = []
        for index, item in enumerate(self.ethernets):
            choices.append(( item,'', False))

        code, tags = self.ui.checklist(u"选择添加到bond的网卡", choices=choices)

        if code == u"ok":
            if not len(tags):
                self.ui.msgbox(u'至少选择一块网卡')
                self.second_create_step()
            else:
                self.edit_bond_ethernets.extend(tags)
                self.edit_bond_ip()
        else:
            sys.exit()

    def second_edit_step(self):
        choices = []
        if len(self.bond_list) == 0:
            self.ui.msgbox(u"没有bond可以操作！")
            sys.exit()
        for item in self.bond_list:
            choices.append((item,''))

        code, tags = self.ui.menu(u"选择bond", choices=choices)

        if code == u"ok":
            self.bond = tags
            self.delete_eth()
        else:
            sys.exit()

    def edit_bond_ip(self):
        ipcode, iptag = self.ui.inputbox(
                u"请输入bond的IP地址:",
                ok_label="Next",
                width=50)
        if ipcode == u"ok":
            self.bond_ip = iptag
            self.edit_bond_mask()

    def edit_bond_mask(self):
        maskcode, masktag = self.ui.inputbox(
                u"请输入bond的掩码地址:",
                extra_button=True,
                extra_label="Back",
                ok_label="Next",
                width=50)
        if maskcode == u"ok":
            self.bond_mask = masktag
            self.edit_bond_gateway()
        elif maskcode == u"extra":
            self.edit_bond_ip()

    def edit_bond_gateway(self):
        gatecode, gatetag = self.ui.inputbox(
                u"请输入bond的网关地址:",
                extra_button=True,
                extra_label="Back",
                ok_label="Next",
                width=50)
        if gatecode == u"ok":
            self.bond_gate = gatetag
            self.ui.msgbox(
                    "%s Info \
                    \nIP:%s\
                    \nNetmask:%s\
                    \nGateway:%s" %\
                    (self.bond,
                    self.bond_ip,
                    self.bond_mask,
                    self.bond_gate ))
            self.apply_config()
        elif gatecode == u"extra":
            self.edit_bond_mask()

    def get_bond_detail(self):
        f = open('%s/%s/bonding/slaves'%(self.net_home_dir,self.bond))
        for line in f.readlines():
            self.bond_detail.append(line)

        f.close()
        if len(self.bond_detail) == 0:
            self.ui.msgbox(u"没有网卡")
            sys.exit()

    def delete_eth(self):
        self.get_bond_detail()
        choices = []
        for item in self.bond_detail:
            choices.append((item,''))
        code, tags = self.ui.menu(u"选择删除的网卡", choices=choices)
        if code == u"ok":
            print tags
            self.del_eth = tags
            self.apply_config()

    def apply_config(self):
        if self.CREATE:
            create_cmd_list = ['nmcli', 'connection', 'add', 'type', 'bond',
                    'ifname', self.bond, 'mode', '6']
            #Create bond mode 6
            subprocess.call(create_cmd_list)
            for net in self.edit_bond_ethernets:
                add_net_cmd = ['nmcli', 'connection', 'add', 'type',
                        'bond-slave', 'ifname', net, 'master', self.bond]
                subprocess.call(add_net_cmd)
            set_ip_cmd = ['nmcli', 'connection', 'modify', 'bond-%s'%self.bond,
                    'ipv4.addresses','%s/%d' % (self.bond_ip,
                    decimalTobinary(self.bond_mask))]
            change_static = ['nmcli', 'connection', 'modify', 'bond-%s' %\
                    self.bond, 'ipv4.method','manual','ipv4.addresses','%s/%d'\
                    % (self.bond_ip, decimalTobinary(self.bond_mask))]
            #Change dhcp To static
            subprocess.call(change_static)
            start_up = ['nmcli', 'connection', 'up', 'bond-%s' % self.bond]
            #apply
            subprocess.call(start_up)
        else:
            del_cmd = ['nmcli', 'connection', 'delete', 'bond-slave-%s' % \
                    self.del_eth]
            subprocess.call(del_cmd)



# 十进制转二进制掩码值
def decimalTobinary(netmask):
    net = netmask.split('.')
    mask = 0
    for item in net:
        sl = bin(int(item))[2:]
        mask += list(sl).count('1')
    return int(mask)

