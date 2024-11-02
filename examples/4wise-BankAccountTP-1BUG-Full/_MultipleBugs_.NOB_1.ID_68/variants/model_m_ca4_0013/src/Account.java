// This is a mutant program.
// Author : ysma

package main; 


public 


class  Account {
	
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

	

     //__feature_mapping__ [CreditWorthiness] [10:13]
	boolean credit( int amount )
    {
        return balance >= -amount;
    }


}
