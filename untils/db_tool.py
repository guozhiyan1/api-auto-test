import pymysql.cursors
import logging


def selectDBData(env, db, sql, is_single=True):
    """
    操作数据库
    :param env:
    :param db: 数据库
    :param sql: 要操作的sql
    :param is_single: 是否是单条操作，True：是，False：否
    :return:
    """

    # 测试环境
    logging.info(f"操作数据库, {env}")
    logging.info(sql)
    if 'test' == env:
        host = "47.103.81.238"
        user = "root"
        password = "Mysql@1234"
        port = 3306
    if 'qa' == env:
        host = ""
        user = ""
        password = ""
        port = 3306

    # 连接数据库
    connect = pymysql.connect(host=host,
                              user=user,
                              passwd=password,
                              database=db,
                              port=port,
                              charset="utf8mb4")

    try:
        # 获取游标
        with connect.cursor() as cursor:
            # 操作数据库
            if is_single:
                cursor.execute(sql)
            else:
                cursor.executemany(sql)
            result = cursor.fetchall()
            logging.info(f"【查询结果】{result}")
        # 关闭连接
        connect.commit()

        return result
    except Exception as e:
        logging.info("操作数据库异常，", e)
    finally:
        # 关闭数据库连接
        connect.close()


def updateDBData(env, db, sql):
    """
    操作数据库
    :param env:
    :param db: 数据库
    :param sql: 要操作的sql
    :param is_single: 是否是单条操作，True：是，False：否
    :return:
    """

    # 测试环境
    logging.info(f"操作数据库, {env}")
    logging.info(sql)
    if 'test' == env:
        host = "47.103.81.238"
        user = "root"
        password = "Mysql@1234"
        port = 3306
    if 'qa' == env:
        host = "47.101.221.124"
        user = "root"
        password = "Mysql@1234"
        port = 3306

    # 连接数据库
    connect = pymysql.connect(host=host,
                              user=user,
                              passwd=password,
                              database=db,
                              port=port,
                              charset="utf8mb4")

    try:
        # 获取游标
        with connect.cursor() as cursor:
            # 操作数据库
            cursor.execute(sql)
        # 关闭连接
        connect.commit()
    except Exception as e:
        logging.info("操作数据库异常，", e)
    finally:
        # 关闭数据库连接
        connect.close()
