import datetime
import xlwt


# 创建excel文件
workbook = xlwt.Workbook(encoding="utf-8")

# 创建表并命名
sheet = workbook.add_sheet("库存统计表", cell_overwrite_ok=True)

# 表格头部样式
style_heading = xlwt.easyxf("""
    font:
      name 宋体,
      colour_index black,
      bold on,
      height 0xD8;
    align:
      wrap off,
      vert center,
      horiz center;
    pattern:
      pattern solid,
      fore-colour white;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    """
                            )
# 内容样式
style_body = xlwt.easyxf("""
    font:
      name 宋体,
      bold off,
      height 0xD8;
    align:
      wrap on,
      vert center,
      horiz left;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    """

                         )

# 行高初始化
sheet.row(0).height_mismatch = True
# 设置行高
sheet.row(0).height = 24 * 24
# 设置每一列的宽度
sheet.col(0).width = 1800
sheet.col(1).width = 7500
sheet.col(2).width = 7500
sheet.col(3).width = 7500
sheet.col(4).width = 7500

head_name = ["序号", "名称", "数量(kg/个/盒)", "单价", "总价"]

# write_merge(a,b,c,d,message)函数将从第a行到第b行的第c列到第d列的单元格合并，并填入内容message
# 合并第0行的第0列到第2列，并添加内容。
sheet.write_merge(0, 0, 0, 4, '库存表', style_heading)

# 将头部内容添加到表格,标题占据了第0行，头部得从第1行开始
for i in range(len(head_name)):
    sheet.write(1, i, str(head_name[i]), style_heading)

lnz_datas = ({"MC": "新能源有限公司", "DZ": "xx市xxx路xxxxx北门口南xxx号",},)

# # 将内容添加到表格，内容得从第2行开始
# k = 2
# for j in lnz_datas:
#     print(j)
#     sheet.write(k, 0, k, style_body)
#     sheet.write(k, 1, j["MC"], style_body)
#     sheet.write(k, 2, j["DZ"], style_body)
#     k += 1

# 表格重命名
now_time = datetime.datetime.now()
now_date = now_time.strftime("%Y%m%d%H%M%S")
excel_name = "统计报表" + str(now_date) + ".xls"

# 存储excel文件到本地
workbook.save('.\\' + excel_name)
