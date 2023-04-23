import redis,time,pymysql

REDIS_INFO = {
    'host':'192.168.0.40',
    'port': 32352,
    'db': 0
}
MYSQL_INFO = {
    'host':'192.168.0.40',
    'user':'root',
    'passwd':'123.com',
    'db':'test',
    'port': 31494
}
# r = redis.Redis(**REDIS_INFO)
#         if v:
#             r.set(k,v,time1)
#             res = 'OK'
#         else:
#             res = r.get(k).decode()
#         return res

# def my_redis(k,v=None,time1=None):
    
# my_redis()
def my_redis():
    T1 = time.time()
    r = redis.Redis(**REDIS_INFO)
    for i in range(1000000):
        if i:
            v = i
            r.set(i,v)
    
    print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))

def my_db():
    T1 = time.time()
    conn = pymysql.connect(**MYSQL_INFO)
    cur = conn.cursor()
    for i in range(2000000):
        sql = 'insert into info (name,age) values ("{}",{});'.format('韩'+str(i),i)
        cur.execute(sql)
    if sql.strip()[:6].upper()=='SELECT':
        res = cur.fetchall()
    else:
        conn.commit()
        res = 'OK'
    cur.close()
    conn.close()
    T2 = time.time()
    return '程序运行时间:%s毫秒' % ((T2 - T1)*1000)

print(my_db())