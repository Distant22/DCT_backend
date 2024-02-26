import pymysql

MYSQL_HOST = "mysql"
MYSQL_USER = "dct_user"
MYSQL_PASSWORD = "dct_secret"
MYSQL_DB = "DCT"

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    db=MYSQL_DB,
    cursorclass=pymysql.cursors.DictCursor
)

async def draw_image(name: str, image: int):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `user` (`name`, `imageType`) VALUES (%s, %s)"
        cursor.execute(sql, (name, image))
    connection.commit()
    return
