import csv
import json
import os
from flask import Flask, render_template,request
from pyecharts.charts import Bar, Page, Timeline,Map
from pyecharts import options as opts

app = Flask(__name__)

mapTips = "教育经费"
mapCSV = "中国教育经费1999-2017.csv"
mapName = "查看中国1999-2017年教育经费投入情况"
indexTitle = "中国各级各类学校数量"
returnBtnName = "返回中国各级各类学校数量"
dataDir = os.getcwd() + "/data"
fileSuffix = ".csv"

@app.route("/")
def index():
    return render_template('index.html',result = {'mapName':mapName,'indexTitle':indexTitle})

@app.route("/menuList")
def menuList():
    print(dataDir)
    dataDirList = os.listdir(dataDir)
    dataDirList.remove(mapCSV)
    list = []
    for file in dataDirList:
        list.append(file.replace(fileSuffix,""))
    return json.dumps({'list':list},ensure_ascii=False)

@app.route("/pyecharts")
def pyecharts():
    val = request.args.get('select')
    isMap = request.args.get('isMap')
    returnBtn = ""
    if isMap == 'true':
        val = mapCSV
        returnBtn = returnBtnName
    return render_template('pyecharts.html',result = {'select':val,'isMap':isMap,"returnBtn":returnBtn})

@app.route("/barCharts")
def barCharts():
    val = request.args.get('select')
    print(val)
    with open(dataDir + val)as f:
        f_csv = csv.reader(f)
        head = []
        map = {}
        i = 0
        for row in f_csv:
            if i ==0:
                head = row[1:len(row)]

            else:
                map[row[0]] = row[1:len(row)]

            i=+1
    bar = (
        Bar()
            .add_xaxis(head)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=val),
                datazoom_opts=opts.DataZoomOpts(),
            )
    )
    bar.width = "100%"
    bar.height = "700px"
    for key in map:
        print(key)
        print(map[key])
        bar.add_yaxis(key,map[key])
    # return Markup(bar.render_embed())
    return bar.dump_options_with_quotes()

@app.route("/timeline")
def timeline():
    val = request.args.get('select')
    isMap = request.args.get('isMap')
    fileName = val
    if isMap != 'true':
        fileName += fileSuffix
    print(fileName)
    with open(dataDir + "/" + fileName)as f:
        f_csv = csv.reader(f)
        head = []
        city = {}
        cityX = []
        i = 0
        rows = []
        for row in f_csv:
            if i == 0:
                head = row[1:len(row)]
                print(head)
            else:
                rows.append(row)
                cityX.append(row[0])
            i = +1
        k = 1
        city = {}
        for year in head:
            city[year] = [row[k] for row in rows]
            k = k + 1
    x = cityX
    tl = Timeline()
    for year in head:
        if isMap == 'true':
            cityMap = []
            i = 0
            maxInt = 0
            t = Timeline()
            for c in x:
                if city[year][i] and city[year][i] != '':
                    if maxInt == 0:
                        maxInt = int(city[year][i])
                    else:
                        ci = int(city[year][i])
                        if ci > maxInt:
                            maxInt = ci
                cityMap.append([c,city[year][i]])
                i = i+1

            map0 = (
                Map()
                    .add(mapTips, cityMap, "china")
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title=val),
                    visualmap_opts=opts.VisualMapOpts(max_=maxInt),
                )
            )
            tl.add(map0, year)
        else:
            bar = (
                Bar()
                    .add_xaxis(x)
                    .add_yaxis(val, city[year])
                    .set_global_opts(title_opts=opts.TitleOpts(val))
            )
            tl.add(bar, year)
    # return Markup(tl.render_embed())
    return tl.dump_options_with_quotes()

if __name__ == "__main__":
    #运行项目
    app.run(host="0.0.0.0",debug = True)
