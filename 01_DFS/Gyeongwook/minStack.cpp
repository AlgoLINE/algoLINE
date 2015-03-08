class MinStack {
public:
    void push(int x) {
        base.push(x);
        if (min.empty() || min.top() >= x)
            min.push(x);
    }

    void pop() {
        if (base.empty())
            return;
        
        if (!min.empty() && base.top() == min.top())
            min.pop();
            
        base.pop();
    }

    int top() {
        return base.top();
    }

    int getMin() {
        return min.top();
    }
    
private:
    std::stack<int> base;
    std::stack<int> min;
};
