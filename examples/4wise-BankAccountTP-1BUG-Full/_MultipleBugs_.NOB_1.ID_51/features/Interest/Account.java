// This is a mutant program.
// Author : ysma

package main;


class Account
{

    static final int INTEREST_RATE = 2;

    int interest = 0;

     int calculateInterest()
    {
        return balance * ~INTEREST_RATE / 36500;
    }

}
