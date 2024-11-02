package main; 
public 
class  Application {
	
	Account account = new Account();

	

	//__feature_mapping__ [BankAccount] [5:6]
	 private void  nextDay__wrappee__BankAccount() {
	}

	
	

	//__feature_mapping__ [DailyLimit] [5:8]
	void nextDay() {
		nextDay__wrappee__BankAccount();
		account.withdraw = 0;
	}

	

	//__feature_mapping__ [BankAccount] [8:9]
	void nextYear() {
	}


}
