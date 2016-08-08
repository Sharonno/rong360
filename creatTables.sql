-- 表：用户基本信息

CREATE TABLE `rong360`.`t_user` (
    `user_id`  VARCHAR(32) NOT NULL,
    `age`  INT(10) NOT NULL,
    `sex`  INT(10) NOT NULL,
    `expect_quota`  INT(10) NOT NULL,
    `max_month_repay`  INT(10) NOT NULL,
    `occupation`  INT(10) NOT NULL,
    `education`  INT(10) NOT NULL,
    `marital_status`  INT(10) NOT NULL,
    `live_info`  INT(10) NOT NULL,
    `local_hk`  INT(10) NOT NULL,
    `money_function`  INT(10) NOT NULL,
    `company_type`  INT(10) NOT NULL,
    `salary`  INT(10) NOT NULL,
    `school_type`  INT(10) NOT NULL,
    `flow`  INT(10) NOT NULL,
    `gross_profit`  INT(10) NOT NULL,
	`business_type`  INT(10) NOT NULL,
    `business_year`  INT(10) NOT NULL,
    `personnel_num`  INT(10) NOT NULL,
    `pay_type`  INT(10) NOT NULL,
    `product_id`  INT(10) NOT NULL,
    `tm_encode`  INT(10) NOT NULL,

  PRIMARY KEY (`user_id`));


LOAD DATA LOCAL INFILE '/Users/Atina/Program/selfTaught/rong360/data/user_info_new.txt' INTO TABLE t_user
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;

-- 表：用户关系2
LOAD DATA LOCAL INFILE '/Users/Atina/Program/selfTaught/rong360/data/relation2.txt' INTO TABLE t_relation_2
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;

-- 表：用户消费信息

CREATE TABLE `rong360`.`t_consumption` (
    `user_id`  VARCHAR(32) NOT NULL,
`bill_id`  INT(10) NOT NULL,
`prior_period_bill_amt`  INT(10) NOT NULL,
`prior_period_repay_amt`  INT(10) NOT NULL,
`credit_lmt_amt`  INT(10) NOT NULL,
`curt_jifen`  INT(10) NOT NULL,
`current_bill_bal`  INT(10) NOT NULL,
`current_bill_min_repay_amt`  INT(10) NOT NULL,
`is_cheat_bill`  INT(10) NOT NULL,
`cost_cnt`  INT(10) NOT NULL,
`current_bill_amt`  INT(10) NOT NULL,
`adj_amt`  INT(10) NOT NULL,
`circle_interest`  INT(10) NOT NULL,
`prior_period_jifen_bal`  INT(10) NOT NULL,
`nadd_jifen`  INT(10) NOT NULL,
`current_adj_jifen`  INT(10) NOT NULL,
`avlb_bal_usd`  INT(10) NOT NULL,
`avlb_bal`  INT(10) NOT NULL,
`card_type`  INT(10) NOT NULL,
`pre_borrow_cash_amt_usd`  INT(10) NOT NULL,
`credit_lmt_amt_usd`  INT(10) NOT NULL,
`pre_borrow_cash_amt`  INT(10) NOT NULL,
`curr`  INT(10) NOT NULL,
`repay_stat`  INT(10) NOT NULL,
`current_min_repay_amt_usd`  INT(10) NOT NULL,
`current_repay_amt_usd`  INT(10) NOT NULL,
`current_convert_jifen`  INT(10) NOT NULL,
`current_award_jifen`  INT(10) NOT NULL,
PRIMARY KEY (`user_id`)
);


LOAD DATA LOCAL INFILE '/Users/Atina/Program/selfTaught/rong360/data/consumption_record.txt' INTO TABLE t_consumption
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;

-- 表：用户下载应用
CREATE TABLE `rong360`.`t_rong_tag` (
    `user_id`  VARCHAR(32) NOT NULL,
    `rong_tag` INT(10) NOT NULL,
    PRIMARY KEY (`user_id`)
);

LOAD DATA LOCAL INFILE '/Users/Atina/Program/selfTaught/rong360/data/rong_tag.txt' INTO TABLE t_rong_tag
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;

-- 表： 用户标签
CREATE TABLE `rong360`.`t_user_label` (
    `user_id`  VARCHAR(32) NOT NULL,
    `label` INT(10) NOT NULL,
    PRIMARY KEY (`user_id`)
);

LOAD DATA LOCAL INFILE '/Users/Atina/Program/selfTaught/rong360/data/train.txt' INTO TABLE t_user_label
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  IGNORE 1 LINES;