// This is a mutant program.
// Author : ysma

package main; 


public   class  Account {
	
	final int OVERDRAFT_LIMIT = 0;

	

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

	

	final static int INTEREST_RATE = 2;

	

	int interest = 0;

	


	//__feature_mapping__ [Interest] [9:11]
	int calculateInterest() {
		return balance * INTEREST_RATE / 36500;
	}

	

    private boolean lock = false;

	

     //__feature_mapping__ [Lock] [12:15]
	void lock()
    {
        lock = true;
    }

	

     //__feature_mapping__ [Lock] [17:20]
	void unLock()
    {
        lock = false;
    }

	

     //__feature_mapping__ [Lock] [22:25]
	boolean isLocked()
    {
        return !lock;
    }


}
