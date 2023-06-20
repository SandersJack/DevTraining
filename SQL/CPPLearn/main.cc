#include <stdio.h>
#include <sqlite3.h> 
#include <string>
#include <iostream>
#include <cstring>

using namespace std;

static int callback(void *data, int argc, char **argv, char **azColName) {
    int i;

    fprintf(stderr, "%s: ", (const char*)data);

    for( i = 0; i<argc; i++) {
        printf("%s = %s \n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return(0);
}

static int createTable(sqlite3 *db, int rc, char *zErrMsg) {

    char *sql;

    // Create SQL Database //

    sql = "CREATE TABLE COMPANY(" \
        "ID INT PRIMARY KEY     NOT NULL," \
        "NAME           TEXT    NOT NULL," \
        "AGE            INT     NOT NULL," \
        "ADRESS         CHAR(50)," \
        "SALARY         REAL);";

    rc = sqlite3_exec(db, sql, callback, 0, &zErrMsg);

    if (rc != SQLITE_OK){
        fprintf(stderr, "SQL error: %s \n", zErrMsg);
        sqlite3_free(zErrMsg);
    } else {
        fprintf(stderr, "Table created successfully \n");
    }

    return(0);
}

static int addValues(sqlite3 *db, int rc, int id, string name, int age, string adress, int salary) {
    string sql;
    char *iErrMsg = 0;

    sql = "INSERT INTO COMPANY (ID,NAME,AGE,ADRESS,SALARY) " \
        "VALUES (" + to_string(id) + ", '" + name + "', " \ 
        + to_string(age) + ", '" + adress + "', " + to_string(salary) + " );";

    //cout << sql << endl;
    rc = sqlite3_exec(db, sql.c_str(), callback, 0, &iErrMsg);

    if( rc != SQLITE_OK ){
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
      fprintf(stdout, "Records created successfully\n");
    }

    return(0);
}

static int select(sqlite3 *db, int rc, const char *data, string query) {
    char *iErrMsg = 0;

    string sql = "SELECT " + query + " from COMPANY";

    rc = sqlite3_exec(db, sql.c_str(), callback, (void*)data, &iErrMsg);

    if( rc != SQLITE_OK ) {
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }

    return(0);
}

static int update(sqlite3 *db, int rc, const char *data, string query) {
    char *iErrMsg = 0;

    string sql = "UPDATE COMPANY set " + query + ";";

    rc = sqlite3_exec(db, sql.c_str(), callback, (void *)data, &iErrMsg);
    if( rc != SQLITE_OK ) {
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }

    return(0);
}

static int deleteEntry(sqlite3 *db, int rc, const char *data, int id) {
    char *iErrMsg = 0;

    string sql = "DELETE from COMPANY where ID=" + to_string(id) + "; ";

    rc = sqlite3_exec(db, sql.c_str(), callback, (void *)data, &iErrMsg);

    if( rc != SQLITE_OK ) {
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }

    return(0);
}

int main() {

    sqlite3 *db;
    char *zErrMsg = 0;
    int rc;
    const char* data = "Callback function called";
    

    rc = sqlite3_open("test.db", &db);

    if( rc ) {
        fprintf(stderr, "Can't open database: %s\n", sqlite3_errmsg(db));
        return(0);
    } else {
        fprintf(stderr, "Opened database successfully\n");
    }
    
    //addValues(db, rc, 1, "Jack", 32, "Geneva", 100000);
    //addValues(db, rc, 2, "Emily", 20, "Birmingham", 10000000);

    select(db, rc, data, "*");
    update(db, rc, data, "SALARY = 20000 where ID=2");
    select(db, rc, data, "*");
    deleteEntry(db, rc, data, 2);
    select(db, rc, data, "*");

    sqlite3_close(db);
    return 0;
}