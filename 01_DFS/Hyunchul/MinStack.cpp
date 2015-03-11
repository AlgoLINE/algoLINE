//
//  MinStack.cpp
//  min_stack
//
//  Created by LinePlus on 2015. 3. 9..
//  Copyright (c) 2015년 LinePlus. All rights reserved.
//

#include <iostream>
#include "list"

using namespace std;

class MinStack {
private:
    list<int> stack_list;
    list<int>::iterator min_itor;
public:
    void push(int x) {
        if (stack_list.empty()) {
            stack_list.push_front(x);
            min_itor = stack_list.begin();
        } else {
            stack_list.push_front(x);
            if (x < *min_itor) {
                min_itor = stack_list.begin();
            }
        }
    }
    
    void pop() {
        if (stack_list.empty()) {
            return;
        }
        
        if (stack_list.begin() == min_itor) {
            stack_list.pop_front();
            if (stack_list.empty()) {
                return;
            }
            
            list<int>::iterator itor;
            int min = stack_list.front();
            min_itor = stack_list.begin();
            
            for (itor = stack_list.begin(); itor != stack_list.end(); itor++) {
                if (*itor < min) {
                    min_itor = itor;
                }
            }
            
        } else {
            stack_list.pop_front();
        }
    }
    
    int top() {
        int top_val = 0;
        if (stack_list.empty()) {
            cout << "no element" << endl;
        } else {
            top_val = stack_list.front();
        }
        
        return top_val;
    }
    
    int getMin() {
        int min_val = 0;
        if (stack_list.empty()) {
            cout << "no element" << endl;
        } else {
            min_val = *min_itor;
        }
        
        return min_val;
    }
};