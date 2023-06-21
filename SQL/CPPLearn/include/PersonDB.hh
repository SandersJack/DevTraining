#ifndef PersonDB_H
#define PersonDB_H 

#include "Person.hh"

#include <string>
#include <stdio.h>
#include <sqlite3.h> 

using namespace std;

class PersonDB {
    public:
        PersonDB();

        int createDatabase(sqlite3 *db, int rc, char *zErrMsg);
        int saveEntry(sqlite3 *db, int rc, Person *entry);
        int selectEntry(sqlite3 *db, int rc, const char *data, string query);

    private:
        
};

#endif