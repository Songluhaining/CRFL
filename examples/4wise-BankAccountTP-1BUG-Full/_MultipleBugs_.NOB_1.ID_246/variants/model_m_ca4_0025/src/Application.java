package main; 
public 
class  Application {
	
	Account account = new Account();

	

	//__feature_mapping__ [BankAccount] [5:6]
	 private void  nextDay__wrappee__BankAccount() {
	}

	
	

	//__feature_mapping__ [DailyLimit] [5:8]
	 private void  nextDay__wrappee__DailyLimit() {
		nextDay__wrappee__BankAccount();
		account.withdraw = 0;
	}

	

	//__feature_mapping__ [Interest] [4:7]
	void nextDay() {
		nextDay__wrappee__DailyLimit();
		account.interest += account.calculateInterest();
	}

	

	//__feature_mapping__ [BankAccount] [8:9]
	 private void  nextYear__wrappee__BankAccount() {
	}

	

	//__feature_mapping__ [Interest] [9:13]
	void nextYear() {
		nextYear__wrappee__BankAccount();
		account.balance += account.interest;
		account.interest = 0;
	}


}
