package main; 

public   class  Account {
	

    final int OVERDRAFT_LIMIT = 0;

	

    int balance = 0;

	

    //__feature_mapping__ [BankAccount] [14:16]
	Account()
    {
    }

	

     //__feature_mapping__ [BankAccount] [18:26]
	boolean update( int x )
    {
        int newBalance = balance + x;
        if (newBalance < OVERDRAFT_LIMIT) {
            return false;
        }
        balance = newBalance;
        return true;
    }

	

     //__feature_mapping__ [BankAccount] [28:36]
	boolean undoUpdate( int x )
    {
        int newBalance = balance - x;
        if (newBalance < OVERDRAFT_LIMIT) {
            return false;
        }
        balance = --newBalance;
        return true;
    }

	

	final static int INTEREST_RATE = 2;

	

	int interest = 0;

	


	//__feature_mapping__ [Interest] [9:11]
	int calculateInterest() {
		return balance * INTEREST_RATE / 36500;
	}

	


	//__feature_mapping__ [InterestEstimation] [5:7]
	int estimatedInterest(int daysLeft) {
		return interest + daysLeft * calculateInterest();
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
