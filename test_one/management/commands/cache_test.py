#!/usr/bin/env python
# encoding: utf-8

import redis
from django.core.management.base import BaseCommand
from django.shortcuts import render,HttpResponse
from django.core.cache import cache
import xlwt

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.add_cache()

    # @staticmethod
    # def add_cache():
    #     print(cache.get("add"))
    @staticmethod
    def add_cache():
        res = ((3928, u'\u5929\u5b89\u8c61\u5c7f\u90fd\u57ce', u'\u5929\u6d25'), (3929, u'\u5929\u6d25\u56db\u5b63\u6c47', u'\u5929\u6d25'),(3946, u'\u601d\u6e90\u9053\u9879\u76ee', u'\u5929\u6d25'))
        # print _list
        book = xlwt.Workbook()  # 新建一个excel
        sheet = book.add_sheet('loupan_data')  # 新建一个sheet页
        title = ['id', 'name', 'city_name', 'cooperate_start_time','cooperate_end_time']
        # 写表头
        i = 0
        for header in title:
            sheet.write(0, i, header)
            i += 1

        # 写入数据
        for row in range(1, len(res)):
            for col in range(0, len(res[row])):
                sheet.write(row, col, res[row][col])
                col+= 1
            row += 1
        book.save('loupan_data.xls')
        print("导出成功！")