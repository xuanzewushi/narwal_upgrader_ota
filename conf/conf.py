#!/usr/bin/env python
# encoding: utf-8
"""
@author: xingrong.peng
@file: conf.py
@time: 2023/3/3 下午4:35
"""


from oprate_ini_file import DisposeIni


def get_ini_data(name):
    """
    调用操作ini文档模块，获取ini文档的所有内容
    :param name: ini文件名称
    :return:
    """
    dis = DisposeIni('./upgrader_ota_file/upgrade_stress_test_one/config/' + name)
    get_sections = dis.get_sections()
    ts = ''
    for i in range(len(get_sections)):
        get_items = dis.get_items(get_sections[i])
        txt = ''
        for m in range(len(get_items)):
            txt = txt + get_items[m][0] + ' = ' + get_items[m][1] + '\n'
        ts = ts + '[' + get_sections[i] + ']\n' + txt + '\n'
    return ts


def write_ini_data(path, name, data):
    dis = DisposeIni('./' + path + '/upgrade_stress_test_one/config/' + name)
    data_list = data.split('\n')
    nb_list = []
    for i in range(len(data_list)):
        # print(data_list[i])
        if data_list[i].find('[') == 0:
            nb_list.append(i)
            # print(data_list[i])
    section = ''
    for n in range(len(data_list)):
        if n in nb_list:
            section = data_list[n].strip('[]')
        elif data_list[n].find('[') != 0 and data_list[n] != '':
            ts = data_list[n].split(' = ')
            # section = data_list[nb_list[m]].strip('[]')
            dis.set_option(section, ts[0], ts[1])
            print(section, ts[0], ts[1])

# if __name__ == '__main__':
#     ss = get_stress_test_config_data()
#     print(ss)
