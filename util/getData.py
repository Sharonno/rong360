# -*- coding: utf-8 -*-
__author__ = 'Shang'
from getTables import *
from getDB import dbutil
from sqlalchemy import func, select
from sqlalchemy import distinct
from sqlalchemy import desc
from sqlalchemy.sql import *
from sqlalchemy.orm import *
from time import time
import pickle
import pdb, logging

class getData:
    @staticmethod
    def get_train_label():
      """
      pickle: user_id: label
      """
      mysession = dbutil().get_session()
      u_l = mysession.query(t_user_label).all()
      result = {}
      for item in u_l:
        result[item.user_id] = item.label

      print "Saving to pickle ... "
      with open('user_label.pkl', 'w') as f:
        pickle.dump(result, f)
      print "DONE ! "

    @staticmethod
    def get_all_data():
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
                   45     46
                  用户编号     标签

                   ]

        44维特征，其中0-19是用户基本信息，20-44是用户消费信息；45列用户编号, 46列是标签
        """

        print "QUERY BEGIN!"
        start = time()
        mysession = dbutil().get_session()

        labels = pickle.load(open('user_label.pkl', 'r'))
        t_joined = mysession.query(t_user, t_consumption).filter(t_user.user_id == t_consumption.user_id).all()
        info = [[ tmp.t_user.age,
                  tmp.t_user.expect_quota,
                  tmp.t_user.max_month_repay,
                  tmp.t_user.occupation,
                  tmp.t_user.education,
                  tmp.t_user.marital_status,
                  tmp.t_user.live_info,
                  tmp.t_user.local_hk,
                  tmp.t_user.money_function,
                  tmp.t_user.company_type,
                  tmp.t_user.salary,
                  tmp.t_user.school_type,
                  tmp.t_user.flow,
                  tmp.t_user.gross_profit,
                  tmp.t_user.business_type,
                  tmp.t_user.business_year,
                  tmp.t_user.personnel_num,
                  tmp.t_user.pay_type,
                  tmp.t_user.product_id,
                  tmp.t_consumption.prior_period_bill_amt,
                  tmp.t_consumption.prior_period_repay_amt,
                  tmp.t_consumption.credit_lmt_amt,
                  tmp.t_consumption.curt_jifen,
                  tmp.t_consumption.current_bill_bal,
                  tmp.t_consumption.current_bill_min_repay_amt,
                  tmp.t_consumption.is_cheat_bill,
                  tmp.t_consumption.cost_cnt,
                  tmp.t_consumption.current_bill_amt,
                  tmp.t_consumption.adj_amt,
                  tmp.t_consumption.circle_interest,
                  tmp.t_consumption.prior_period_jifen_bal,
                  tmp.t_consumption.nadd_jifen,
                  tmp.t_consumption.current_adj_jifen,
                  tmp.t_consumption.avlb_bal_usd,
                  tmp.t_consumption.avlb_bal,
                  tmp.t_consumption.card_type,
                  tmp.t_consumption.pre_borrow_cash_amt_usd,
                  tmp.t_consumption.credit_lmt_amt_usd,
                  tmp.t_consumption.pre_borrow_cash_amt,
                  tmp.t_consumption.curr,
                  tmp.t_consumption.repay_stat,
                  tmp.t_consumption.current_min_repay_amt_usd,
                  tmp.t_consumption.current_repay_amt_usd,
                  tmp.t_consumption.current_convert_jifen,
                  tmp.t_consumption.current_award_jifen,
                  tmp.t_user.user_id,
                  labels.get(tmp.t_user.user_id, -1)

        ] for tmp in t_joined]
        print "QUERY DONE! It took ", time()-start, " seconds to execute the query!"
        with open('features.pkl', 'w') as f:
          pickle.dump(info, f)
        print "Features have been saved to pkl file !"

    @staticmethod
    def split_data():
      """
      return train_data, test_data
      """
      features = pickle.load(open('features.pkl', 'r'))
      labels = pickle.load(open('user_label.pkl', 'r'))
      label = set(labels.values())

      test_data = []
      train_data = []
      test_num = 0
      train_num = 0

      for f in features:
        if f[-1] not in label:
          logging.info("sample without label, set to label: %d" % f[-1])
          test_num += 1
          test_data.append(f[:-1])
        else:
          train_num += 1
          train_data.append(f)

      print "There are {: d} samples for predict and {: d} samples for training .".format(test_num, train_num)

      with open('train_f.pkl', 'w') as f:
        pickle.dump(train_data, f)

      with open('test_f.pkl', 'w') as f:
        pickle.dump(test_data, f)

      print "Features for each type have been saved ! "


 

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO,
                    filename='./my.log',
                    format='%(asctime)s %(filename)s[%(lineno)d] %(levelname)s %(message)s',
                    filemode='w'
                    )
    a = getData()
    a.get_all_data()
    a.split_data()



