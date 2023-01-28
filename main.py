import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.charts import Map
from pyecharts.charts import Boxplot
from pyecharts.globals import ThemeType
import matplotlib.pyplot as plt

dc = pd.read_csv('result-covid.csv', encoding='utf-8')
dv = pd.read_csv('result-vaccined.csv', encoding='utf-8')

mtmp = dc.loc[dc['area_name'] == 'World']
date_list = mtmp['date'].values.tolist()
date_list.reverse()


def world_trend() -> Line:
    tmp = dc.loc[dc['area_name'] == 'World']
    data_x = date_list
    data_y = tmp['tot_confirmed'].values.tolist()
    data_y.reverse()

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
            .add_xaxis(data_x)
            .add_yaxis("全球总确诊人数", data_y, is_smooth=True, is_connect_nones=True)
            .set_series_opts(
            areastyle_opts=opts.AreaStyleOpts(opacity=0.8)
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="World trend - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='日期',
                is_show=True,
                name_location='end',
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                ),
                min_=264000000,
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            )
        )
    )

    return c


def new_confirmed_top_10() -> Line:
    tmp = dc['new_confirmed'].groupby(dc['area_name']).sum()
    tmp.sort_values(inplace=True, ascending=False)
    country_list = tmp.index.tolist()[1:11]
    tmp = dc.loc[dc['area_name'].isin(country_list)]
    data_x = date_list

    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
            .add_xaxis(data_x)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="New confirmed top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='日期',
                is_show=True,
                name_location='end',
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='每日新增确诊数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True,
                    linestyle_opts=opts.LineStyleOpts(
                        type_='dashed'
                    )
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='bottom',
                pos_bottom='bottom'
            )

        )
    )
    for i in range(1, 11):
        tmp_y = tmp.loc[tmp['area_name'] == country_list[i - 1]]
        data_y = tmp_y['new_confirmed'].values.tolist()
        data_y.reverse()
        for j in range(len(data_y)):
            if data_y[j] <= 0:
                data_y[j] = None

        c_ = (
            Line(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px'))
                .add_xaxis(data_x)
                .add_yaxis(country_list[i - 1], data_y, is_smooth=True, is_connect_nones=True)
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        c.overlap(c_)
    return c


def confirmed_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='tot_confirmed', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['tot_confirmed'].values.tolist()[1:11]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('tot_confirmed', data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total confirmed top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='top',
                pos_bottom='top'
            )
        )
    )
    return c


def confirmed_percentage() -> Pie:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='tot_confirmed', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:13]
    data_y = ttmp['tot_confirmed'].values.tolist()[1:13]
    data_x.append('Others')
    sum_y = 0
    for it in data_y:
        sum_y += it
    data_y.append(ttmp.loc[ttmp['area_name'] == 'World']['tot_confirmed'].values[0] - sum_y)
    data = []
    for i in range(len(data_x)):
        data.append((data_x[i], data_y[i]))
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1000px', height='600px'))
            .add(
            "",
            data,
            radius=[30, 180]
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b} : {d}%"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Confirmed percentage - Covid-19 pandamic"),
            legend_opts=opts.LegendOpts(
                pos_right='right',
                pos_bottom='bottom'
            )
        )
    )
    return c


def confirmed_rate_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='affected_population_rate', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['affected_population_rate'].values.tolist()[1:11]
    for it in data_y:
        it = float("%.2f" % it)

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('affected_population_rate', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}.0%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Confirmed rate top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数占比',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


def tot_vaccined() -> Map:
    data_x = dv['area_name'].values.tolist()
    data_y = dv['tot_vaccined'].values.tolist()
    data = []
    for i in range(len(data_x)):
        if np.isnan(data_y[i]):
            data_y[i] = 0
        data.append((data_x[i], data_y[i]))
    print(data)
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1200px', height='600px'))
            .add('tot_vaccined', data, "world")
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False), showLegendSymbol=False)
            .set_global_opts(
            title_opts=opts.TitleOpts(title='Total vaccined'),
            visualmap_opts=opts.VisualMapOpts(max_=100000000)
        )
    )
    return c


def vaccined_bottom_10() -> Bar:
    tmp = dv.sort_values(by='tot_vaccined_rate', ascending=True)
    data_x = tmp['area_name'].values.tolist()[1:11]
    data_y = tmp['tot_vaccined_rate'].values.tolist()[1:11]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('vaccined_bottom_10', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Vaccined rate bottom 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='接种人口比例',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


def GDP_top_10_confirmed() -> Boxplot:
    country_list = ['United States of America', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France',
                    'Italy', 'Canada', 'South Korea']
    tmp = dc.loc[dc['area_name'].isin(country_list)].loc[dc['date'] == 'Dec 20']
    data_x = ['Countries']
    data_y = tmp['tot_confirmed'].values.tolist()

    c = (Boxplot(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='800px', height='600px')))
    c.add_xaxis(data_x)
    c.add_yaxis('GDP_top_10_vaccined', c.prepare_data([data_y]))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="GDP top 10 vaccined - Covid-19 pandamic"),
        legend_opts=opts.LegendOpts(
            pos_left='right',
            pos_right='right',
            pos_top='top',
            pos_bottom='top'
        )
    )

    plt.boxplot(data_y, showmeans=True, vert=True, labels=['countries'])
    plt.show()

    return c


def death_rate_top_10() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='death_rate', ascending=False)
    data_x = ttmp['area_name'].values.tolist()[1:11]
    data_y = ttmp['death_rate'].values.tolist()[1:11]
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('death_rate_top_10', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Death rate top 10 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='死亡率',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


def confirmed_rate_bottom_12() -> Bar:
    tmp = dc.loc[dc['date'] == 'Dec 20']
    ttmp = tmp.sort_values(by='affected_population_rate', ascending=True)
    data_x = ttmp['area_name'].values.tolist()[1:13]
    data_y = ttmp['affected_population_rate'].values.tolist()[1:13]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('tot_confirmed_rate', data_y)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Total confirmed rate bottom 12 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='确诊人数',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='right',
                pos_right='right',
                pos_top='top',
                pos_bottom='top'
            )
        )
    )
    return c


def vaccined_top_12() -> Bar:
    tmp = dv.sort_values(by='tot_vaccined_rate', ascending=False)
    data_x = tmp['area_name'].values.tolist()[1:13]
    data_y = tmp['tot_vaccined_rate'].values.tolist()[1:13]

    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK, width='1400px', height='600px'))
            .add_xaxis(data_x)
            .add_yaxis('vaccined_top_12', data_y)
            .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%'))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Vaccined rate top 12 - Covid-19 pandamic"),
            xaxis_opts=opts.AxisOpts(
                name='国家',
                is_show=True,
                name_location='end',
                axislabel_opts=opts.LabelOpts(
                    interval=0
                )
            ),
            yaxis_opts=opts.AxisOpts(
                name='接种人口比例',
                is_show=True,
                name_location='end',
                name_textstyle_opts=opts.TextStyleOpts(
                    padding=[0, 100, 0, 0]
                )
            ),
            legend_opts=opts.LegendOpts(
                pos_left='center',
                pos_right='center',
                pos_top='bottom',
                pos_bottom='bottom'
            )
        )
    )
    return c


def covid_predict():
    tmp = dc.loc[dc['area_name'] == 'World']
    data_x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tmp_y = tmp['tot_confirmed'].values.tolist()
    tmp_y.reverse()
    data_y = np.array(tmp_y[1:11])

    # 最小二乘法求解线性回归并进行分析
    x_mean = np.mean(data_x)
    y_mean = np.mean(data_y)
    numerator = 0.0
    denominator = 0.0
    for i in range(len(data_x)):
        numerator += (data_x[i] - x_mean) * (data_y[i] - y_mean)
        denominator += np.square((data_x[i] - x_mean))
    a_ = numerator / denominator
    b_ = y_mean - a_ * x_mean

    x_predic = [11, 12, 13, 14, 15]
    real_val = tmp_y[11:16]
    predic_val = []
    abs_dif = []
    rel_dif = []
    for it in x_predic:
        predic_val.append(it * a_ + b_)
    labels = ['Data', 'Dec 15', 'Dec 16', 'Dec 17', 'Dec 18', 'Dec 19']
    for i in range(len(real_val)):
        abs_dif.append(abs(predic_val[i] - real_val[i]))
        rel_dif.append(round(10000 * abs_dif[i] / real_val[i], 1))
    real_val.insert(0, 'real_value')
    predic_val.insert(0, 'predict_value')
    abs_dif.insert(0, 'abs_difference')
    rel_dif.insert(0, 'rel_difference(*1e-4)')
    data = [tuple(predic_val), tuple(real_val), tuple(abs_dif), tuple(rel_dif)]
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.max_rows', 20)
    pd.set_option('max_colwidth', 200)
    df = pd.DataFrame.from_records(data, columns=labels)
    print(df)


# world_trend().render()
# new_confirmed_top_10().render()
# confirmed_top_10().render()
# confirmed_percentage().render()
# confirmed_rate_top_10().render()
# tot_vaccined().render()
# vaccined_bottom_10().render()
# GDP_top_10_confirmed().render()
# death_rate_top_10().render()

# confirmed_rate_bottom_12().render()
# vaccined_top_12().render()

covid_predict()
