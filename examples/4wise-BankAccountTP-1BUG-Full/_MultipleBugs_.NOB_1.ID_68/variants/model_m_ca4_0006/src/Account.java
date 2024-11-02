package main; 

public   class  Account {
	

	final int OVERDRAFT_LIMIT  = -5000;

	

	int balance = 0;

	

	//__feature_mapping__ [BankAccount] [7:8]
	Account() {
	}

	

	//__feature_mapping__ [BankAccount] [10:16]
	boolean update(int x) {
		int newBalance = balance + x;
		if (newBalance < OVERDRAFT_LIMIT)
			return false;
		balance = newBalance;
		return true;
	}

	

	//__feature_mapping__ [BankAccount] [18:24]
	boolean undoUpdate(int x) {
		int newBalance = balance - x;
		if (newBalance < OVERDRAFT_LIMIT)
			return false;
		balance = newBalance;
		return true;
	}

	

     //__feature_mapping__ [CreditWorthiness] [10:13]
	boolean credit( int amount )
    {
        return balance >= -amount;
    }

	
	
	private boolean lock = false;

	

	//__feature_mapping__ [Lock] [7:9]
	void lock() {
		lock = true;
	}

	

	//__feature_mapping__ [Lock] [11:13]
	void unLock() {
		lock = false;
	}

	

	//__feature_mapping__ [Lock] [15:17]
	boolean isLocked() {
		return lock;
	}


}
