#ifndef Person_H
#define Person_H 

#include <string>
#include <stdio.h>
#include <sqlite3.h> 

using namespace std;

class Person {
    public:
        Person();

        int GetPersonID() { return fPersonID;};
        string GetName() { return fName;};
        string GetEmail() { return fEmail;};
        int GetAge() { return fAge;};

    private:

        int fPersonID;
        string fName;
        string fEmail;
        int fAge;
        
};

#endif