from pyecharts.charts import Pie, Timeline
from pyecharts import options as opts

datas = {
    220:[('魏', 50), ('蜀', 15), ('吴', 35)],
    230:[('魏', 60), ('蜀', 20), ('吴', 20)],
    240:[('魏', 40), ('蜀', 30), ('吴', 30)],
    250:[('魏', 35), ('蜀', 40), ('吴', 25)],
    260:[('魏', 50), ('蜀', 20), ('吴', 30)],
    270:[('魏', 60), ('蜀', 15), ('吴', 25)],
    280:[('魏', 80), ('蜀', 10), ('吴', 10)]
}

tl = Timeline()
for year, data in datas.items():
    pie = Pie().add(year, data)
    tl.add(pie, year)

tl.render('sadfasd.html')


