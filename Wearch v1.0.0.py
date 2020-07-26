a="[版本 Version 1.0.0 Alpha]"
b="@ 2020 HornCopper. 保留所有权利"
c=" "
d="1.计算器"
e="2.生成URL"
f="3.Minecraft Wiki搜索"
print(" ")
print("Wearch For Python "+a)
print(b)

print(c)

print(d)
print(e)
print(f)
print(c)
g = input("请选择功能[填写序号]:")
if g == '1':
    j = input("请选择计算法则(加/减/乘/除):")
    if j == '加':
        h = input("请输入第一数字:")
        i = input("请输入第二数字:")
        print("计算结果请查看resultValue值,通常整数显示为1位小数")
        h = float(h)
        i = int(i)
        print("aType:",type(h))
        print("bType:",type(i))

        result = h + i
        print("resultValue:",result)
        print("resulyType:",type(result))
    
    if j == '减':
        h = input("请输入第一数字:")
        i = input("请输入第二数字:")
        print("计算结果请查看resultValue值,通常整数显示为1位小数")
        h = float(h)
        i = int(i)
        print("aType:",type(h))
        print("bType:",type(i))

        result = h - i
        print("resultValue:",result)
        print("resulyType:",type(result))
    if j == '乘':
        h = input("请输入第一数字:")
        i = input("请输入第二数字:")
        print("计算结果请查看resultValue值,通常整数显示为1位小数")
        h = float(h)
        i = int(i)
        print("aType:",type(h))
        print("bType:",type(i))

        result = h * i
        print("resultValue:",result)
        print("resulyType:",type(result))
    if j == '除':
        h = input("请输入第一数字:")
        i = input("请输入第二数字:")
        print("计算结果请查看resultValue值,通常整数显示为1位小数")
        h = float(h)
        i = int(i)
        print("aType:",type(h))
        print("bType:",type(i))

        result = h / i
        print("resultValue:",result)
        print("resulyType:",type(result))
    else:
        print("检测到非法输入，Wearch已自动关闭，可执行py <本软件路径>!")
if g == '2':
    k = input("请选择搜索引擎(百度/360/搜狗[所有搜索引擎不支持抓取简介！])：")
    if k == '百度':
        bd_url="https://www.baidu.com/s?ie=UTF-8&wd="
        bd_search=input("请输入搜索内容：")
        
        print(" ")
        print("URL请查看resultValue值")
        print(" ")
        print("bd_urlType:",type(bd_url))
        print("bd_searchType:",type(bd_search))

        print(" \n")
        print("成功生成URL：")
        result = bd_url + bd_search
        print("请在外部Web浏览器中打开")
        print("resultValue:",result)
        print("resultType:",type(result))
    if k == '360':
        qihoo_url="https://www.so.com/s?ie=utf-8&fr=233&src=home_233&q="
        qihoo_search=input("请输入搜索内容：")

        print(" ")
        print("URL请查看resultValue值")
        print(" ")
        print("qihoo_urlType:",type(qihoo_url))
        print("qihoo_searchType:",type(qihoo_search))

        print(" ")
        print("成功生成URL：")
        result = qihoo_url + qihoo_search
        print("请在外部Web浏览器中打开")
        print("resultValue:",result)
        print("resultType:",type(result))
    if k == '搜狗':
        sogou_url="https://www.sogou.com/web?query="
        sogou_search=input("请输入搜索内容：")

        print(" ")
        print("URL请查看resultValue值")
        print(" ")
        print("sogou_urlType:",type(sogou_url))
        print("sogou_searchType:",type(sogou_search))

        print(" ")
        print("成功生成URL：")
        result = sogou_url + sogou_search
        print("请在外部Web浏览器中打开")
        print("resultValue:",result)
        print("resultType:",type(result))
else:
    print("检测到非法输入，Wearch已自动关闭，可执行py <本软件路径>!")