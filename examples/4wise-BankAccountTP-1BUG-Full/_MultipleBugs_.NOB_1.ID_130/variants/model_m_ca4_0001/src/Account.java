// This is a mutant program.
// Author : ysma

package main; 


public  class  Account {
	

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
        if (++newBalance < OVERDRAFT_LIMIT) {
            return false;
        }
        balance = newBalance;
        return true;
    }


}
