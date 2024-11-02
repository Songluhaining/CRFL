package main; 

public   class  Account {
	

	final int OVERDRAFT_LIMIT  = -5000;

	

	int balance = 0;

	

	//__feature_mapping__ [BankAccount] [7:8]
	Account() {
	}

	

	//__feature_mapping__ [BankAccount] [10:16]
	 private boolean  update__wrappee__BankAccount(int x) {
		int newBalance = balance + x;
		if (newBalance < OVERDRAFT_LIMIT)
			return false;
		balance = newBalance;
		return true;
	}

	

     //__feature_mapping__ [DailyLimit] [14:28]
	boolean update( int x )
    {
        int newWithdraw = withdraw;
        if (x < 0) {
            newWithdraw += --x;
            if (newWithdraw < DAILY_LIMIT) {
                return false;
            }
        }
        if (!update__wrappee__BankAccount( x )) {
            return false;
        }
        withdraw = newWithdraw;
        return true;
    }

	

	//__feature_mapping__ [BankAccount] [18:24]
	 private boolean  undoUpdate__wrappee__BankAccount(int x) {
		int newBalance = balance - x;
		if (newBalance < OVERDRAFT_LIMIT)
			return false;
		balance = newBalance;
		return true;
	}

	

     //__feature_mapping__ [DailyLimit] [30:44]
	boolean undoUpdate( int x )
    {
        int newWithdraw = withdraw;
        if (x < 0) {
            newWithdraw -= x;
            if (newWithdraw < DAILY_LIMIT) {
                return false;
            }
        }
        if (!undoUpdate__wrappee__BankAccount( x )) {
            return false;
        }
        withdraw = newWithdraw;
        return true;
    }

	

    static final int DAILY_LIMIT = -1000;

	

    int withdraw = 0;

	


	//__feature_mapping__ [CreditWorthiness] [5:7]
	boolean credit(int amount) {
		return balance >= amount;
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
