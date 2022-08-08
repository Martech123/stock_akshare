import akshare as ak
import pandas as pd
tool_trade_date_hist_sina_df = ak.tool_trade_date_hist_sina()

trade_date_list = []
for y in range(2002, 2022):
    for index, row in tool_trade_date_hist_sina_df.iterrows():
        trade_date = "{}{:0>2d}{:0>2d}".format(row["trade_date"].year, row["trade_date"].month, row["trade_date"].day)
        #print(type(row["trade_date"].year))
        if row["trade_date"].year == y:
            print(index, trade_date)
            trade_date_list.append(trade_date)
    
    df = pd.DataFrame()
    for day in trade_date_list:
        zhangting_df = ak.stock_zt_pool_em(date=day)
        #for index, row in zhangting_df.iterrows():
        #    print(row)
        df = pd.concat([df, zhangting_df])
    df.to_csv("zhangting_{}.csv".format(y))
