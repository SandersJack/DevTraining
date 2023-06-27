#ifndef Person_H
#define Person_H 

#include <string>
#include <stdio.h>
#include <sqlite3.h> 

using namespace std;

class Person {
    public:
        Person();
        Person(int PersonID,string Name,string Email,int Age);

        int GetPersonID() { return fPersonID;};
        string GetName() { return fName;};
        string GetEmail() { return fEmail;};
        int GetAge() { return fAge;};

        void SetPersonID(int val) {fPersonID = val;};
        void SetName(string val) {fName = val;};
        void SetEmail(string val) {fEmail = val;};
        void SetAge(int val) { fAge = val;};

    private:

        int fPersonID;
        string fName;
        string fEmail;
        int fAge;
        
};

#endif