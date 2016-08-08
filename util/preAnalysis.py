def app_user_cnt(result):
    app_user_cnt_dict = {}
    cnt_range = ['>=3000', '>=2500', '>=2000', '>=1500', '>=1000', '>=500', '>=100', '>=10', '0']
    cnt_val = [0 for i in xrange(13)]
    app_user_cnt_dict = dict(zip(cnt_range, cnt_val))
    for item in  result:
        cnt = int(item[1])
        if cnt >= 3000:
            app_user_cnt_dict[cnt_range[0]] += 1
        elif cnt >= 2500:
            app_user_cnt_dict[cnt_range[1]] += 1
        elif cnt >= 2000:
            app_user_cnt_dict[cnt_range[2]] += 1
        elif cnt >= 1500:
            app_user_cnt_dict[cnt_range[3]] += 1
        elif cnt >= 1000:
            app_user_cnt_dict[cnt_range[4]] += 1
        elif cnt >= 500:
            app_user_cnt_dict[cnt_range[5]] += 1
        elif cnt >= 100:
            app_user_cnt_dict[cnt_range[6]] += 1
        elif cnt >= 10:
            app_user_cnt_dict[cnt_range[7]] += 1
        else:
            app_user_cnt_dict[cnt_range[8]] += 1
    print app_user_cnt_dict