import pandas as pd
import numpy as np

#****************************************************************************************************

"""
    1- Tenkan-Sen (Conversion Line ) = (Highest High + Lowest Low) / 2, for the past 9 periods
    2- Kijun-Sen (Base Line) = (Highest High + Lowest Low) / 2, for the past 26 periods
    3- Chikou Span (Lagging Span) = Today's closing price plotted 26 periods behind
    3- Senkou Span A = (Tenkan-Sen + Kijun-Sen) / 2, plotted 26 periods ahead
    4- Senkou Span B = (Highest High + Lowest Low) / 2, for the past 52 periods, plotted 26 periods ahead
"""

#****************************************************************************************************

def Ichimoku(Data):

    _data = Data[:] # A copy to prevent change on origital DataFram
    
    TenkanSen = pd.Series((_data['High'].rolling(9, min_periods = 9).max()
                           + _data['Low'].rolling(9, min_periods = 9).min()) / 2
                          , name = 'TenkanSen')
    
    KijunSen = pd.Series((_data['High'].rolling(26, min_periods = 26).max()
                          + _data['Low'].rolling(26, min_periods = 26).min()) / 2
                         , name = 'KijunSen')

    ChikouSpan = pd.Series(_data['Close'], name = 'ChikouSpan').shift(-26)

    SenkouSpanA = pd.Series((TenkanSen + KijunSen) / 2, name = 'SenkouSpanA').append(pd.Series([0] * 26, name = 'SenkouSpanA'), ignore_index = True).shift(26)
                           
    SenkouSpanB = pd.Series((_data['High'].rolling(52, min_periods = 52).max()
                           + _data['Low'].rolling(52, min_periods = 52).min()) / 2
                          , name = 'SenkouSpanB').append(pd.Series([0] * 26, name = 'SenkouSpanB'), ignore_index = True).shift(26)
    
    for i in range(len(_data),len(_data) + 26):
        _data.loc[i] = [None,None,None,None,None,None]

    _data = _data.join(TenkanSen)
    _data = _data.join(KijunSen)
    _data = _data.join(ChikouSpan)    
    _data = _data.join(SenkouSpanA)
    _data = _data.join(SenkouSpanB)

    return _data
    
#****************************************************************************************************

def IchimokuArash(Data):

    _data = Data[:] # A copy to prevent change on origital DataFram
    
    TenkanSen1 = pd.Series((_data['High'].rolling(9, min_periods = 9).max()
                           + _data['Low'].rolling(9, min_periods = 9).min()) / 2
                          , name = 'TenkanSen1')
    
    KijunSen1 = pd.Series((_data['High'].rolling(26, min_periods = 26).max()
                          + _data['Low'].rolling(26, min_periods = 26).min()) / 2
                         , name = 'KijunSen1')

    ChikouSpan1 = pd.Series(_data['Close'], name = 'ChikouSpan1').shift(-26)

    SenkouSpanA1 = pd.Series((TenkanSen1 + KijunSen1) / 2, name = 'SenkouSpanA1').shift(26)
                           
    SenkouSpanB1 = pd.Series((_data['High'].rolling(52, min_periods = 52).max()
                           + _data['Low'].rolling(52, min_periods = 52).min()) / 2
                          , name = 'SenkouSpanB1').shift(26)

    #-----------------------------------------------------------------------------------

    TenkanSen2 = pd.Series((_data['High'].rolling(18, min_periods = 18).max()
                           + _data['Low'].rolling(18, min_periods = 18).min()) / 2
                          , name = 'TenkanSen2')
    
    KijunSen2 = pd.Series((_data['High'].rolling(52, min_periods = 52).max()
                          + _data['Low'].rolling(52, min_periods = 52).min()) / 2
                         , name = 'KijunSen2')

    SenkouSpanA2 = pd.Series((TenkanSen2 + KijunSen2) / 2, name = 'SenkouSpanA2').shift(52)
    
    SenkouSpanB2 = pd.Series((_data['High'].rolling(104, min_periods = 104).max()
                           + _data['Low'].rolling(104, min_periods = 104).min()) / 2
                          , name = 'SenkouSpanB2').shift(52)

    #-----------------------------------------------------------------------------------
    
    TenkanSen3 = pd.Series((_data['High'].rolling(36, min_periods = 36).max()
                           + _data['Low'].rolling(36, min_periods = 36).min()) / 2
                          , name = 'TenkanSen3')
    
    KijunSen3 = pd.Series((_data['High'].rolling(104, min_periods = 104).max()
                          + _data['Low'].rolling(104, min_periods = 104).min()) / 2
                         , name = 'KijunSen3')

    SenkouSpanA3 = pd.Series((TenkanSen3 + KijunSen3) / 3, name = 'SenkouSpanA3').shift(104)
    
    SenkouSpanB3 = pd.Series((_data['High'].rolling(208, min_periods = 208).max()
                           + _data['Low'].rolling(208, min_periods = 208).min()) / 2
                          , name = 'SenkouSpanB3').shift(104)

    #-----------------------------------------------------------------------------------
    
    _data = _data.join(TenkanSen1)
    _data = _data.join(KijunSen1)
    _data = _data.join(ChikouSpan1)    
    _data = _data.join(SenkouSpanA1)
    _data = _data.join(SenkouSpanB1)

    _data = _data.join(TenkanSen2)
    _data = _data.join(KijunSen2)
    _data = _data.join(SenkouSpanA2)
    _data = _data.join(SenkouSpanB2)

    _data = _data.join(TenkanSen3)
    _data = _data.join(KijunSen3)
    _data = _data.join(SenkouSpanA3)
    _data = _data.join(SenkouSpanB3)

    #-----------------------------------------------------------------------------------

    return _data
    
#****************************************************************************************************

