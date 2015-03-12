class MinStack {
public:
    stack<int> s, m;
    
    void push(int x) {
        if(m.empty() || x < m.top()){
            m.push(x);
        }else{
            m.push(m.top());
        }
        s.push(x);
    }

    void pop() {
        s.pop();
        m.pop();
    }

    int top() {
        return s.top();
    }

    int getMin() {
        return m.top();
    }
};