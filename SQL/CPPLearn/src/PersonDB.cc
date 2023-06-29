#include "PersonDB.hh"
#include <cstring>
#include <iostream>

struct PersonRecord{
    vector<int> ID;
    vector<string> Name;
    vector<string> Email;
    vector<int> Age;
};

int select_callback(void *p_data, int num_fields, char **argv, char **szColName)
{
    PersonRecord* personRecord = static_cast<PersonRecord*>(p_data);
    for(int i = 0; i < num_fields; i++)
        {
            if (strcmp(szColName[i], "ID") == 0)
            {
                personRecord->ID.push_back(atoi(argv[i]));
            } 
            else if (strcmp(szColName[i], "NAME") == 0)
            {
                personRecord->Name.push_back(argv[i]);
            } 
            else if (strcmp(szColName[i], "EMAIL") == 0)
            {
                personRecord->Email.push_back(argv[i]);
            }
            else if (strcmp(szColName[i], "AGE") == 0)
            {
                personRecord->Age.push_back(atoi(argv[i]));
            }
            cout << szColName[i] << " = " << argv[i] << endl;
        }
    return 0;
}


static int callback(void *data, int argc, char **argv, char **azColName) {
    int i;

    fprintf(stderr, "%s: ", (const char*)data);

    for( i = 0; i<argc; i++) {
        printf("%s = %s \n", azColName[i], argv[i] ? argv[i] : "NULL");
    }
    printf("\n");
    return(0);
}

PersonDB::PersonDB() {

}

int PersonDB::createDatabase(sqlite3 *db, int rc, char *zErrMsg){
    string sql;

    // Create SQL Database //

    sql = "CREATE TABLE PERSONS(" \
        "ID INT PRIMARY KEY     NOT NULL," \
        "NAME           TEXT    NOT NULL," \
        "EMAIL          TEXT    NOT NULL," \
        "AGE            INT     NOT NULL);";

    rc = sqlite3_exec(db, sql.c_str(), callback, 0, &zErrMsg);

    if (rc != SQLITE_OK){
        fprintf(stderr, "SQL error: %s \n", zErrMsg);
        sqlite3_free(zErrMsg);
        return 1;
    } else {
        fprintf(stderr, "Table created successfully \n");
    }

    return 0;
}

int PersonDB::saveEntry(sqlite3 *db, int rc, Person *entry) {
    string sql;
    char *iErrMsg = 0;

    sql = "INSERT INTO PERSONS (ID,NAME,EMAIL,AGE) " \
        "VALUES (" + to_string(entry->GetPersonID()) + ", '" + entry->GetName() + "', '" \
        + entry->GetEmail() + "', " + to_string(entry->GetAge()) + " );";

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

int PersonDB::printEntry(sqlite3 *db, int rc, const char *data, string query) {
    char *iErrMsg = 0;

    string sql = "SELECT * from PERSONS WHERE " + query;

    rc = sqlite3_exec(db, sql.c_str(), callback, (void*)data, &iErrMsg);

    if( rc != SQLITE_OK ) {
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }

    return(0);
}

Person *PersonDB::getEntry(sqlite3 *db, int rc, const char *data, string query) {
    char *iErrMsg = 0;

    Person *outputPerson = new Person();

    PersonRecord recordsPerson;

    string sql = "SELECT * from PERSONS WHERE " + query;

    rc = sqlite3_exec(db, sql.c_str(), select_callback, &recordsPerson, &iErrMsg);

    if( rc != SQLITE_OK ) {
      fprintf(stderr, "SQL error: %s\n", iErrMsg);
      sqlite3_free(iErrMsg);
    } else {
        fprintf(stdout, "Operation done successfully\n");
    }
    outputPerson->SetPersonID(recordsPerson.ID[0]);
    outputPerson->SetName(recordsPerson.Name[0]);
    outputPerson->SetEmail(recordsPerson.Email[0]);
    outputPerson->SetAge(recordsPerson.Age[0]);


    return(outputPerson);
}