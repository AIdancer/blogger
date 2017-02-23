#encoding : utf8
import math
from WindPy import w
import numpy as np

def TsToTime(ts):
    hour = ts / 3600;
    minutes = (ts % 3600) / 60;
    seconds = ts % 60;
    return '%02d:%02d:%02d' % (hour, minutes, seconds)

def TimeToTs(hour, minutes, seconds):
    return hour*3600 + minutes*60 + seconds

class Bar:
    def __init__(self, _open = 0, _high = 0, _low = 0, _close = 0):
        self.open = _open
        self.high = _high
        self.low = _low
        self.close = _close
    def SetTs(self, _ts):
        self.ts = _ts
    def __str__(self):
        return '%s %.4f %.4f %.4f %.4f' % (TsToTime(self.ts), self.open, self.high, self.low, self.close)

def GetDailyData(year, month, day, instrument):
    bar_list = []
    date_str = '%4d-%02d%02d' % (year, month, day)
    data = w.wsi(instrument, 'open,high,low,close', '%s 09:00:00' % date_str, \
                 '%s 10:15:00' % date_str).Data
    cnt = 0
    open_, high_, low_, close_ = data[0], data[1], data[2], data[3]

    for ts in range(TimeToTs(9,0,0), TimeToTs(10,15,0), 60):
        bar = Bar(open_[cnt], high_[cnt], low_[cnt], close_[cnt])
        bar.SetTs(ts)
        bar_list.append(bar)
        cnt = cnt + 1
    data = w.wsi(instrument, 'open,high,low,close', '%s 10:30:00' % date_str, \
                 '%s 11:30:00' % date_str).Data
    cnt = 0
    open_, high_, low_, close_ = data[0], data[1], data[2], data[3]
    for ts in range(TimeToTs(10, 30, 0), TimeToTs(11, 30, 0), 60):
        bar = Bar(open_[cnt], high_[cnt], low_[cnt], close_[cnt])
        bar.SetTs(ts)
        bar_list.append(bar)
        cnt = cnt + 1
    data = w.wsi(instrument, 'open,high,low,close', '%s 13:30:00' % date_str, \
                 '%s 15:00:00' % date_str).Data
    cnt = 0
    open_, high_, low_, close_ = data[0], data[1], data[2], data[3]
    for ts in range(TimeToTs(13, 30, 0), TimeToTs(15, 00, 0), 60):
        bar = Bar(open_[cnt], high_[cnt], low_[cnt], close_[cnt])
        bar.SetTs(ts)
        bar_list.append(bar)
        cnt = cnt + 1
    return bar_list

def GetNightData(year, month, day, instrument):
    bar_list = []
    date_str = '%4d-%02d%02d' % (year, month, day)
    data = w.wsi(instrument, 'open,high,low,close', '%s 21:00:00' % date_str, \
                 '%s 23:30:00' % date_str).Data
    cnt = 0
    open_, high_, low_, close_ = data[0], data[1], data[2], data[3]
    n = len(open_);

    for ts in range(TimeToTs(21, 0, 0), TimeToTs(23, 30, 0), 60):
        if cnt >= n:
            break
        bar = Bar(open_[cnt], high_[cnt], low_[cnt], close_[cnt])
        bar.SetTs(ts)
        bar_list.append(bar)
        cnt = cnt + 1
    return  bar_list

if __name__ == '__main__':
    instrument_list = ['m1705.dce', 'ru1705.shf', 'i1705.dce', 'SR705.czc', 'pp1705.dce', 'l1705.dce']
    # instrument_list = ['m1705.dce']
    w.start()
    data_file = open('./data_all.mdt', 'wb')
    for instrument in instrument_list:
        list = GetDailyData(2017,2,22, instrument)
        for val in list:
            if math.isnan(val.open):
                continue
            line = '%s %s\n' % (instrument.split('.')[0], str(val))
            data_file.write(line)
    data_file.close()
    data_file = open('./data_all.mdt', 'a+')
    for instrument in instrument_list:
        list = GetNightData(2017, 2, 22, instrument)
        for val in list:
            if math.isnan(val.open):
                continue
            line = '%s %s\n' % (instrument.split('.')[0], str(val))
            data_file.write(line)
    data_file.close()
    print 'finished.'





