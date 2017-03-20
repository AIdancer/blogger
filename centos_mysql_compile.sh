# We assume version.c is the source code which using mysql.
# Please refer to http://zetcode.com/db/mysqlc/ for more information.
gcc version.c -o version  `mysql_config --cflags --libs`
