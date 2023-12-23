#include <iostream>
#include <fstream>
#include <unordered_map>
using namespace std;

unordered_map<string, string> cmd_table;

void init_cmd_hash() {

    ifstream file("D:\\tkyCommand\\config.ini", ios::in);
    if (!file) {
        cout << "Please check the config file!" << endl;
        exit(0);
    }

    string cmd, cmd_str;

    while (!file.eof()) {
        getline(file, cmd);
        getline(file, cmd_str);
        cmd_table[cmd] = cmd_str;
    }

    file.close();
}


void run() {
    while (true) {
        string cmd, cmd_str;
        cin >> cmd;
        cmd_str = cmd_table[cmd];
        if (cmd_table[cmd] == "" && cmd != "exit") {
            cout << "Unknown command" << endl;
        }
        else if(cmd == "exit") {
            return;
        }
        else {
            system(cmd_str.c_str());
        }
    }
}

int main() {

    init_cmd_hash();

    run();


    return 0;
}
