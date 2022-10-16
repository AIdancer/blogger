### 相关sample
```
https://zetcode.com/db/mysqlc/
```

```c++
#include <iostream>
#include <cassert>
#include <cstring>
#include <mysql.h>

using namespace std;

int ctest() {
    MYSQL* conn;
    if (!(conn = mysql_init(0)))
    {
        fprintf(stderr, "unable to initialize connection struct\n");
        exit(1);
    }

    // Connect to the database
    if (!mysql_real_connect(
        conn,                 // Connection
        "localhost", // Host
        "root",            // User account
        "nicaicai",   // User password
        "test",               // Default database
        3306,                 // Port number
        NULL,                 // Path to socket file
        0                     // Additional options
    ))
    {
        // Report the failed-connection error & close the handle
        fprintf(stderr, "Error connecting to Server: %s\n", mysql_error(conn));
        mysql_close(conn);
        exit(1);
    }

    // Use the Connection
    cout << "mysql version : " << mysql_get_client_info() << endl;
    mysql_query(conn, "show databases");
    MYSQL_RES* result = mysql_store_result(conn);
    int num_fields = mysql_num_fields(result);
    int num_rows = mysql_num_rows(result);
    cout << "num_fields : " << num_fields << "      num_rows : " << num_rows << endl;
    MYSQL_ROW row;
    while (row = mysql_fetch_row(result)) {
        for (int i = 0; i < num_fields; i++) {
            if (row[i]) cout << row[i] << " ";
            else cout << "NULL" << " ";
        }
        cout << endl;
    }

    // Close the Connection
    mysql_close(conn);
    return 0;
}

int main() {
    
    int res = ctest();
    return 0;
}
```
