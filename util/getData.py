# -*- coding: utf-8 -*-
__author__ = 'Shang'
from getTables import *
from dbutil import dbutil
from sqlalchemy import func
from sqlalchemy import distinct
from sqlalchemy import desc
from time import time


class getData:
    @staticmethod
    def get_train_data():
        """     
                      0    1     2          3         4       5        6
        return data[年龄，性别, 申请金额, 最大月还款 ,职业类型, 教育程度, 婚姻状态,
                      7         8       9         10    11     12      13
                   房屋类型, 户口类型, 贷款用途, 公司类型, 薪水, 学校类型, 月盈利余额, 
                       14     15        16       17       18      19      
                   毛利润率, 营业类别, 营业年限, 公司规模, 收入类型, 产品ID, 
                       20
                   上期账单金额, 上期还款金额, 信用卡额度, 当前积分, 本期账单余额, 本期账单最低还款额, 是否恶意账单, 

                  可消费笔数, 本期账单金额, 调整金额, 循环利息, 上期积分余额, 新增积分, 本期调整积分,

                  可用余额, 卡类型, 预借现金额度美元, 信用额度美元, 预借现金额度, 币种, 还款状态, 

                  本期最低还款额美元, 本期应还款金额美元, 本期兑换积分, 本期奖励积分，
                   45
                  标签

                   ]

        44维特征，其中0-19是用户基本信息，20-44是用户消费信息；45列是标签
        """



# consumption_info = mysession.query(t_consumption)
# app_info = mysession.query(t_rong_tag)

        print "QUERY BEGIN!"
        start = time()
        mysession = dbutil().get_session()
        user = mysession.query(t_user).all()
        # all_info = mysession.query(t_user, t_consumption, t_user_label).filter(t_user.user_id == t_consumption.user_id).filter(t_user.user_id == t_user_label.user_id).all()
        # all_info = mysession.query(t_user, t_consumption, t_user_label).join(t_consumption).join(t_user_label).all()
        print "QUERY DONE! It took ", time()-start, " seconds to execute the query!"
        # print all_info.column_descriptions
        print len(user)


if __name__ == '__main__':
    a = getData()
    a.get_train_data() 


