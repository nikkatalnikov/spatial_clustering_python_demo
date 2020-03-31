from datetime import datetime
from typing import Tuple, List
import pandas as pd
from mpl_toolkits.basemap import Basemap


def split_b_days_weekends(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    b_days = df[df.index.dayofweek < 5]
    weekends = df[df.index.dayofweek >= 5]
    return b_days, weekends


def split_by_days(ts: pd.DataFrame) -> List[pd.DataFrame]:
    return [group[1] for group in ts.groupby(ts.index.day)]


def dateparse(ts: int) -> datetime:
    return datetime.fromtimestamp(float(ts))


def yesterday_night(ts: pd.DataFrame) -> pd.DataFrame:
    return ts.between_time('00:00', '05:00', include_end=False)


def mornings(ts: pd.DataFrame) -> pd.DataFrame:
    return ts.between_time('05:00', '09:00', include_end=False)


def daytimes(ts: pd.DataFrame) -> pd.DataFrame:
    return ts.between_time('09:00', '18:00', include_end=False)


def nights(ts: pd.DataFrame) -> pd.DataFrame:
    return ts.between_time('18:00', '00:00', include_end=False)


def draw_map(df: pd.DataFrame, bound: float = 1.0) -> Basemap:
    m = Basemap(
        projection='merc',
        resolution='l',
        area_thresh=1000,
        llcrnrlon=df.longitude.min() - bound,
        llcrnrlat=df.latitude.min() - bound,
        urcrnrlon=df.longitude.max() + bound,
        urcrnrlat=df.latitude.max() + bound)

    m.drawcoastlines(linewidth=0.1)
    m.drawstates(linewidth=0.1)
    m.drawlsmask(land_color='white', ocean_color='skyblue')

    return m
