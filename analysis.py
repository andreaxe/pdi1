import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

sns.set(style="ticks", font_scale=1.5, font="Times New Roman")

colnames = ['country', 'timestamp', 'predicted', 'observed']

data = pd.read_csv("pdi_total_load.csv", sep=',', names=colnames)
print(data.head())

data.loc[:, 'timestamp'] = pd.to_datetime(
    data["timestamp"], format="%Y-%m-%d %H:%M:%S").dt.tz_localize('UTC').dt.tz_convert("Europe/Lisbon")
data.set_index("timestamp", inplace=True)

data_2018 = data['2018-04-01':'2018-05-01']
data_2019 = data['2019-04-01':'2019-05-01']
data_2020 = data['2020-04-01':'2020-05-01']


# -- plot valores medios por hora do dia da semana
to_plot_2018 = data_2018.groupby(data_2018.index.strftime(
    "%A-%H")).mean().rename(columns={"observed": '2018'})["2018"]
to_plot_2019 = data_2019.groupby(data_2019.index.strftime(
    "%A-%H")).mean().rename(columns={"observed": '2019'})["2019"]
to_plot_2020 = data_2020.groupby(data_2020.index.strftime(
    "%A-%H")).mean().rename(columns={"observed": '2020'})["2020"]
to_plot = to_plot_2018.to_frame().join(to_plot_2019).join(to_plot_2020)
print(to_plot.index)

wdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
new_ix = []
for d in wdays:
    new_ix += [f"{d}-{str(x).zfill(2)}" for x in range(0, 24)]

to_plot = to_plot.reindex(index=new_ix)
print(to_plot.index)
# to_plot.index = [x.split('-')[0] for x in to_plot.index]
fig, ax = plt.subplots(1, 1, figsize=(15, 7))
to_plot.plot(ax=ax)
plt.xticks(np.arange(168), ['Monday'] + [" "]*23 + ['Tuesday'] + [" "]*23 + ['Wednesday'] + [" "]*23 + [
           'Thursday'] + [" "]*23 + ['Friday'] + [" "]*23 + ['Saturday'] + [" "]*23 + ['Sunday'] + [" "]*23)
ax.set_ylabel("Average Power Consumption [MW]")
ax.set_xlabel("Hour of Day of the Week")
plt.tight_layout()
plt.show()


# --- Plot todos os dias do mes (barras)

fig, ax = plt.subplots(1, 1, figsize=(15, 7))
data_2018 = data['2018-04-01':'2018-04-30 23:59']
data_2019 = data['2019-04-01':'2019-04-30 23:59']
data_2020 = data['2020-04-01':'2020-04-30 23:59']
ax.set_rasterized(True)
# to_plot_2018.to_frame().savefig('rasterized_fig.eps')
to_plot_2018 = data_2018.groupby(data_2018.index.strftime(
    "%m-%d")).sum().rename(columns={"observed": '2018'})["2018"]
to_plot_2019 = data_2019.groupby(data_2019.index.strftime(
    "%m-%d")).sum().rename(columns={"observed": '2019'})["2019"]
to_plot_2020 = data_2020.groupby(data_2020.index.strftime(
    "%m-%d")).sum().rename(columns={"observed": '2020'})["2020"]


to_plot = to_plot_2018.to_frame().join(to_plot_2019).join(to_plot_2020)
to_plot.to_clipboard()
to_plot.plot(ax=ax, kind="bar")

ax.set_ylabel("Accumulated Power Consumption [MW]")
ax.set_xlabel("Day of the month")
plt.tight_layout()
plt.show()

# --- Plot todos os dias do mes (area)

fig, ax = plt.subplots(1, 1, figsize=(15, 7))

to_plot_2018 = data_2018.groupby(data_2018.index.strftime(
    "%d")).sum().rename(columns={"observed": '2018'})["2018"]
to_plot_2019 = data_2019.groupby(data_2019.index.strftime(
    "%d")).sum().rename(columns={"observed": '2019'})["2019"]
to_plot_2020 = data_2020.groupby(data_2020.index.strftime(
    "%d")).sum().rename(columns={"observed": '2020'})["2020"]
to_plot = to_plot_2018.to_frame().join(to_plot_2019).join(to_plot_2020)

to_plot.plot(ax=ax, kind="area", stacked=False)
markers = ['s', 'd', 'o']
for i, line in enumerate(ax.get_lines()):
    line.set_marker(markers[i])

ax.set_ylabel("Accumulated Power Consumption [MW]")
ax.set_xlabel("Day of the month")
plt.xticks(np.arange(0, 30), [str(x) for x in range(1, 31)])
plt.ylim(80000, 190000)
plt.tight_layout()
plt.show()
