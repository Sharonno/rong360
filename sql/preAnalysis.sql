-- 申请金额分布
SELECT 
SUM(CASE WHEN expect_quota >= 1000000  THEN 1 ELSE 0 END) AS '>=100万',
SUM(CASE WHEN expect_quota >= 100000  AND expect_quota < 1000000 THEN 1 ELSE 0 END) AS '>=10万',
SUM(CASE WHEN expect_quota >= 10000 AND expect_quota < 100000 THEN 1 ELSE 0 END) AS '>=1万',
SUM(CASE WHEN expect_quota >= 1000 AND expect_quota < 10000 THEN 1 ELSE 0 END) AS '>=1000',
SUM(CASE WHEN expect_quota >= 100 AND expect_quota < 1000 THEN 1 ELSE 0 END) AS '>=100',
SUM(CASE WHEN expect_quota >= 10 AND expect_quota < 100 THEN 1 ELSE 0 END) AS '>=10',
SUM(CASE WHEN expect_quota < 10 THEN 1 ELSE 0 END) AS '<10'
FROM rong360.t_user
JOIN rong360.t_user_label ON t_user.user_id = t_user_label.user_id
WHERE label = 0;

-- 薪水分布 
SELECT 
SUM(CASE WHEN salary >= 1000000000 THEN 1 ELSE 0 END) AS '>=10亿',
SUM(CASE WHEN salary >= 100000000 AND salary < 1000000000 THEN 1 ELSE 0 END) AS '>=1亿',
SUM(CASE WHEN salary >= 10000000 AND salary < 100000000 THEN 1 ELSE 0 END) AS '>=1000万',
SUM(CASE WHEN salary >= 1000000 AND salary < 10000000 THEN 1 ELSE 0 END) AS '>=100万',
SUM(CASE WHEN salary >= 100000 AND salary < 1000000 THEN 1 ELSE 0 END) AS '>=10万',
SUM(CASE WHEN salary >= 10000 AND salary < 100000 THEN 1 ELSE 0 END) AS '>=1万',
SUM(CASE WHEN salary >= 1000 AND salary < 10000 THEN 1 ELSE 0 END) AS '>=1000',
SUM(CASE WHEN salary >= 100 AND salary < 1000 THEN 1 ELSE 0 END) AS '>=100',
SUM(CASE WHEN salary >= 10 AND salary < 100 THEN 1 ELSE 0 END) AS '>=10',
SUM(CASE WHEN salary < 10 THEN 1 ELSE 0 END) AS '<10'
FROM rong360.t_user
JOIN rong360.t_user_label ON t_user.user_id = t_user_label.user_id
WHERE label = 0;


-- 年龄分布
SELECT 
SUM(CASE WHEN age >= 60 THEN 1 ELSE 0 END) AS '>=60',
SUM(CASE WHEN age >= 50 AND age < 60 THEN 1 ELSE 0 END) AS '>=50',
SUM(CASE WHEN age >= 40 AND age < 100000000 THEN 1 ELSE 0 END) AS '>=40',
SUM(CASE WHEN age >= 30 AND age < 10000000 THEN 1 ELSE 0 END) AS '>=30',
SUM(CASE WHEN age >= 20 AND age < 1000000 THEN 1 ELSE 0 END) AS '>=20',
SUM(CASE WHEN age >= 10 AND age < 100000 THEN 1 ELSE 0 END) AS '>=10',
SUM(CASE WHEN age >= 1 AND age < 10 THEN 1 ELSE 0 END) AS '<10',
SUM(CASE WHEN age = 0 THEN 1 ELSE 0 END) AS '未填写年龄'
FROM rong360.t_user
JOIN rong360.t_user_label ON t_user.user_id = t_user_label.user_id
WHERE label = 1
;

-- 热门app
