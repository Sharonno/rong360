# -*- coding: utf-8 -*-
__author__ = 'Shang'
from sqlalchemy import Column, Integer, VARCHAR, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class t_user(Base):
    __tablename__ = 't_user'

    # id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(VARCHAR, primary_key = True)
    age = Column(Integer)
    sex = Column(Integer)
    expect_quota = Column(Integer)
    max_month_repay = Column(Integer)
    occupation = Column(Integer)
    education = Column(Integer)
    marital_status = Column(Integer)
    live_info = Column(Integer)
    local_hk = Column(Integer)
    money_function = Column(Integer)
    company_type = Column(Integer)
    salary = Column(Integer)
    school_type = Column(Integer)
    flow = Column(Integer)
    gross_profit = Column(Integer)
    business_type = Column(Integer)
    business_year = Column(Integer)
    personnel_num = Column(Integer)
    pay_type = Column(Integer)
    product_id = Column(Integer)
    tm_encode = Column(Integer)


class t_consumption(Base):
    __tablename__ = 't_consumption'

    
    user_id = Column(VARCHAR, ForeignKey("t_user.user_id"))
    bill_id = Column(Integer)
    prior_period_bill_amt = Column(Integer)
    prior_period_repay_amt = Column(Integer)
    credit_lmt_amt = Column(Integer)
    curt_jifen = Column(Integer)
    current_bill_bal = Column(Integer)
    current_bill_min_repay_amt = Column(Integer)
    is_cheat_bill = Column(Integer)
    cost_cnt = Column(Integer)
    current_bill_amt = Column(Integer)
    adj_amt = Column(Integer)
    circle_interest = Column(Integer)
    prior_period_jifen_bal = Column(Integer)
    nadd_jifen = Column(Integer)
    current_adj_jifen = Column(Integer)
    avlb_bal_usd = Column(Integer)
    avlb_bal = Column(Integer)
    card_type = Column(Integer)
    pre_borrow_cash_amt_usd = Column(Integer)
    credit_lmt_amt_usd = Column(Integer)
    pre_borrow_cash_amt = Column(Integer)
    curr = Column(Integer)
    repay_stat = Column(Integer)
    current_min_repay_amt_usd = Column(Integer)
    current_repay_amt_usd = Column(Integer)
    current_convert_jifen = Column(Integer)
    current_award_jifen = Column(Integer)
    id = Column(Integer, primary_key = True, autoincrement = True)


class t_rong_tag(Base):
    __tablename__ = 't_rong_tag'
    
    user_id = Column(VARCHAR, ForeignKey("t_user.user_id"))
    rong_tag = Column(Integer)
    id = Column(Integer, primary_key = True, autoincrement = True)


class t_user_label(Base):
    __tablename__ = 't_user_label'
    
    user_id = Column(VARCHAR, ForeignKey("t_user.user_id"))
    label = Column(Integer)
    id = Column(Integer, primary_key = True, autoincrement = True)



