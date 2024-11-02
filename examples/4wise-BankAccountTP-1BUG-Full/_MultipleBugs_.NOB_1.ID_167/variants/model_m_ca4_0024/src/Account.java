package main; 
public 
class  Account {
	

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

	


	//__feature_mapping__ [CreditWorthiness] [5:7]
	boolean credit(int amount) {
		return balance >= amount;
	}


}
