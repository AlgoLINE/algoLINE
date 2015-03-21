class Node {
private:
	int _lc;
	int _tc;
	bool _balance;
	string _data;

public:
	Node() {
		_lc = 0;
		_tc = 0;
		_balance = false;
	}

	void SetLc(int lc) {
		_lc = lc;
	}

	void SetTc(int tc) {
		_tc = tc;
	}

	void SetBalance(bool balance) {
		_balance = balance;
	}

	int GetLc() {
		return _lc;
	}

	int GetTc() {
		return _tc;
	}

	bool GetBalance() {
		return _balance;
	}

	void SetData(const char *data) {
		_data = string(data);
	}

	const char *GetData() {
		return _data.c_str();
	}
};


class Solution {
public:
	vector<string> generateParenthesis(int n) {
		queue<Node> nodeQ;
		vector<string> resultVector;
		Node root;
		root.SetData("(");
		root.SetLc(1);
		root.SetTc(1);
		root.SetBalance(false);

		nodeQ.push(root);

		for (int i = 1; i < (n * 2); i++) {
			queue<Node> nodeQ2;

			while (!nodeQ.empty()) {
				Node tmpNode = nodeQ.front();

				Node leftNode;//포인터만 저장할 경우 원본데이터가 날라갈수도 있음. 안 되면 큐를 Node* 에서 Node로 바꿔서 해볼것.
				leftNode.SetData((string(tmpNode.GetData()) + "(").c_str());
				leftNode.SetLc(tmpNode.GetLc() + 1);
				leftNode.SetTc(tmpNode.GetTc() + 1);
				leftNode.SetBalance(false);

				Node rightNode;
				rightNode.SetData((string(tmpNode.GetData()) + ")").c_str());
				rightNode.SetLc(tmpNode.GetLc());
				rightNode.SetTc(tmpNode.GetTc() + 1);
				int lc = rightNode.GetLc();
				int tc = rightNode.GetTc();
				if ((tc / lc) == 2 && (tc % lc == 0)) {
					rightNode.SetBalance(true);
				}
				else {
					rightNode.SetBalance(false);
				}

				if (!tmpNode.GetBalance()) {
					nodeQ2.push(rightNode);
				}
				nodeQ2.push(leftNode);
				nodeQ.pop();
			}

			nodeQ = nodeQ2;
		}

		while (!nodeQ.empty()) {
			Node tmpNode = nodeQ.front();
			if (tmpNode.GetBalance()) {
				resultVector.push_back(string(tmpNode.GetData()));
			}
			nodeQ.pop();
		}

		return resultVector;
	}

};