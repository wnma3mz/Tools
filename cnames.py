# coding: utf-8
import matplotlib.pyplot as plt

# matplotlib画图用
cnames = {
'aliceblue':            '#F0F8FF',
'antiquewhite':         '#FAEBD7',
'aqua':                 '#00FFFF',
'aquamarine':           '#7FFFD4',
'azure':                '#F0FFFF',
'beige':                '#F5F5DC',
'bisque':               '#FFE4C4',
'black':                '#000000',
'blanchedalmond':       '#FFEBCD',
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chartreuse':           '#7FFF00',
'chocolate':            '#D2691E',
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'floralwhite':          '#FFFAF0',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'ghostwhite':           '#F8F8FF',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lightblue':            '#ADD8E6',
'lightcoral':           '#F08080',
'lightcyan':            '#E0FFFF',
'lightgoldenrodyellow': '#FAFAD2',
'lightgreen':           '#90EE90',
'lightgray':            '#D3D3D3',
'lightpink':            '#FFB6C1',
'lightsalmon':          '#FFA07A',
'lightseagreen':        '#20B2AA',
'lightskyblue':         '#87CEFA',
'lightslategray':       '#778899',
'lightsteelblue':       '#B0C4DE',
'lightyellow':          '#FFFFE0',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navajowhite':          '#FFDEAD',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6',
'palegoldenrod':        '#EEE8AA',
'palegreen':            '#98FB98',
'paleturquoise':        '#AFEEEE',
'palevioletred':        '#DB7093',
'papayawhip':           '#FFEFD5',
'peachpuff':            '#FFDAB9',
'peru':                 '#CD853F',
'pink':                 '#FFC0CB',
'plum':                 '#DDA0DD',
'powderblue':           '#B0E0E6',
'purple':               '#800080',
'red':                  '#FF0000',
'rosybrown':            '#BC8F8F',
'royalblue':            '#4169E1',
'saddlebrown':          '#8B4513',
'salmon':               '#FA8072',
'sandybrown':           '#FAA460',
'seagreen':             '#2E8B57',
'seashell':             '#FFF5EE',
'sienna':               '#A0522D',
'silver':               '#C0C0C0',
'skyblue':              '#87CEEB',
'slateblue':            '#6A5ACD',
'slategray':            '#708090',
'snow':                 '#FFFAFA',
'springgreen':          '#00FF7F',
'steelblue':            '#4682B4',
'tan':                  '#D2B48C',
'teal':                 '#008080',
'thistle':              '#D8BFD8',
'tomato':               '#FF6347',
'turquoise':            '#40E0D0',
'violet':               '#EE82EE',
'wheat':                '#F5DEB3',
'white':                '#FFFFFF',
'whitesmoke':           '#F5F5F5',
'yellow':               '#FFFF00',
'yellowgreen':          '#9ACD32'}



if __name__ == '__main__':
    # 动态展示
    # plt.ion()
    # plt.pause(0.1)
    # plt.ioff()

    # fig, axs = plt.subplots(3, 2) # 绘制3x2子图

    plt.cla()  # 清空画布
    plt.figure(figsize=(10, 10), dpi=100)  # 画布大小，分辨率
    plt.plot(x, y, 'o-', label=label)  # 绘制直线图, 并标注每点属性，与对应标签
    plt.scatter(x, y)  # 绘制散点图
    plt.bar(x, y, width=width, color='#d62728', alpha=0.5,
            label=label_[1])  # 绘制柱状图

    plt.text(xt, yt, text, ha='center', va='bottom', fontsize=7)  # 图中绘制文本
    plt.annotate(text,
                 xy=(x, y),
                 xytext=(6 * 0.9, p[6] * 0.9),
                 arrowprops=dict(arrowstyle="->",
                                 connectionstyle="arc3,rad=.2"))  # 图中注释文本
    plt.title(title)  # 画布标题
    plt.xlabel(xlabel_title)  # x轴标题

    plt.legend(loc=2, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)  # 输出图例等
    plt.legend("best")

    plt.xticks(rotation=90)  # x轴上坐标旋转90度
    plt.xlim(min_x, max_x)  # 限定x坐标最小值与最大值

    plt.tight_layout()  # 自适应画布
    # plt.gca().invert_xaxis()  # 逆序横坐标

    plt.show()  # 显示图片
    plt.savefig('count_gender.png')  # 保存图片

    # 多子图，共享x轴，双y轴
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y1, 'v-', label='1', color='royalblue')
    ax.plot(x, y2, 'x-', label='2', color='tomato')

    ax2 = ax.twinx()
    ax2.plot(x, y3, 'o-', label='3', color='orange')
    ax2.set_ylim(30, 100)
    # ax2.legend(loc=1)

    ax.set_xlabel("压力(GPa)")
    # ax.set_ylabel(r"bcc和hcp原子的结构含量(%)")
    # ax2.set_ylabel(r"fcc和结晶原子的结构含量(%)")
    # plt.xlabel(r"压力(GPa)")
    # plt.ylabel(r"结构含量(%)")
    fig.legend(loc=1, bbox_to_anchor=(1, 1), bbox_transform=ax.transAxes)
