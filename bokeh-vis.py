from bokeh.io import show, output_notebook, output_file
from bokeh.models.widgets import Div
from bokeh.io import curdoc
from bokeh.layouts import column, row, widgetbox
from bokeh.models import (
    GeoJSONDataSource,
    HoverTool,
    LinearColorMapper,
    ColorBar,
    BasicTicker,
    PrintfTickFormatter,
    LogColorMapper,
    LogTicker,
    Range1d,
    Plot,
    Text
)
from bokeh.plotting import figure
import geopandas as gpd

with open('/home/drogon/Desktop/Rescue-1122-project/punjab_districts(area_pop_den).geojson', 'r') as f:
    geo_source = GeoJSONDataSource(geojson=f.read())

df = gpd.read_file('/home/drogon/Desktop/Rescue-1122-project/punjab_districts(area_pop_den).geojson')
density = df['density']

colors = ['#000003', '#3B0F6F', '#8C2980', '#DD4968', '#FD9F6C']
colors.reverse()
color_mapper = LogColorMapper(palette="Viridis256", low=density.min(), high=density.max())
TOOLS = "pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure( title="Punjab Districts", tools=TOOLS,
           x_axis_location=None, y_axis_location=None, width=600, height=600)
p.grid.grid_line_color = None
p.title.text_font_size = '30pt'

p.patches('xs', 'ys', fill_alpha=0.9, fill_color={'field': 'density', 'transform': color_mapper},
          line_color='white', line_width=1, source=geo_source)


hover = p.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [("District", "@district"),
                  ("Density", "@density"),
                  ("Area", "@area")]

color_bar = ColorBar(color_mapper=color_mapper, major_label_text_font_size="10pt",
                     ticker=LogTicker(desired_num_ticks=9),
                     formatter=PrintfTickFormatter(format="%d"),
                     label_standoff=10, border_line_color=None, location=(0, 0))
p.add_layout(color_bar, 'right')

xdr = Range1d(0, 220)
ydr = Range1d(0, 120)

plot = figure(
    x_range=xdr,
    y_range=ydr,
    title="",
    plot_width=250,
    plot_height=120,
    min_border=0,
)
# Add the writing
country = Text(x=5, y=50, text='district')
percent = Text(x=15, y=10, text='hello', text_color='blue')  # nopep8
percent_sign = Text(x=69, y=10, text=['%'], text_color='blue')  # nopep8
line_one = Text(x=90, y=28, text=['of people had'])
line_two_p1 = Text(x=90, y=14, text=['access in'])
line_two_p2 = Text(x=136, y=14, text='year')
plot.add_glyph(geo_source, Text(), selection_glyph=country)
plot.add_glyph(geo_source, Text(), selection_glyph=percent)
plot.add_glyph(geo_source, Text(), selection_glyph=percent_sign)
plot.add_glyph(line_one)
plot.add_glyph(line_two_p1)
plot.add_glyph(geo_source, Text(), selection_glyph=line_two_p2)

# div = Div(text="Bokeh text "+ hover)
curdoc().add_root(row(column(p)))