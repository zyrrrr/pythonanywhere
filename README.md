## pythonanywhere地址：
* [中国教育经费1999-2017](http://zyrrrrr.pythonanywhere.com)
* 【温馨提示】：页面刷新可能比较慢，图出现可能需要等等。

## 文档描述：

### HTML档描述(前端设计)

* **html文本**：共有两个HTML文件，一个是网页首页，页面内容为 介绍今年来的中国各级学校数量；github的readme跳转链接；和一个iframe标签，标签内用于展示选择的图表；一个下拉列表，用于选择所要展示的数据，展示方式未一个柱状图；一个跳转链接，点击跳转到另一个网页。

* 另一个页面是展示近年来中国各地的教育经费投入情况，将各地经费数据的多少转换成对应地区地图颜色的深浅，直观的显示近年来各地教育经费的变化，以及各地区间的对比；通过选择时间轴上不同的年份，展示年份对应的数据。

* **js函数**：页面内的下拉框以及点击事件，均使用jequery封装的ajax请求，在不刷新页面的情况下，随着选择的变化，动态展示不同的数据。

* **css样式**：添加了背景美化，字体大小的改变，使页面观看性更高。

### Python档描述（后端设计）

* 使用csv模块，将数据从.csv文件中导出；

* 使用json模块，将数据dump成json格式，上传到前端页面

* 利用flask框架完成Python的web开发，实现前后端的交互；

* 使用pyecharts模块，在交互环境中将数据可视化；

* 利用Python的列表、字符串等容器，实现数据的加工、保存、处理等。

### web APP动作描述（交互端设计）

* @app.route("/")：跳转学校数量的页面。

* @app.route("/pyecharts")：展示教育经费的页面。

* @app.route("/barCharts")：返回选择的下拉列表中各级学校对应的数据，通过ajax请求在页面中动态加载，展示为柱状图。

*  @app.route("/timeline")：返回选择的时间轴对应的各个地区教育经费数据，通过ajax请求在页面动态加载，数据通过js渲染到中国地图中，数据量大小对应地图中颜色的深浅。

#### 也就是总共有4个url跳转页面。


