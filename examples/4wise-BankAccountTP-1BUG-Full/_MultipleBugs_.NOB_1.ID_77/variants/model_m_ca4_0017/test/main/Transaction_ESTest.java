/*
 * This file was automatically generated by EvoSuite
 * Sat Feb 06 15:52:04 GMT 2021
 */

package main;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import main.Account;
import main.Transaction;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true, useJEE = true) 
public class Transaction_ESTest extends Transaction_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      boolean boolean0 = transaction0.transfer(account0, account0, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      // Undeclared exception!
      try { 
        transaction0.transfer(account0, (Account) null, 0);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("main.Transaction", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      account0.lock();
      Account account1 = new Account();
      boolean boolean0 = transaction0.transfer(account1, account0, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      account0.balance = (-7157);
      Account account1 = new Account();
      boolean boolean0 = transaction0.transfer(account1, account0, 734);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      account0.balance = (-7157);
      boolean boolean0 = transaction0.transfer(account0, account0, 734);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      boolean boolean0 = transaction0.transfer(account0, account0, 734);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      account0.lock();
      boolean boolean0 = transaction0.transfer(account0, account0, 0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      Transaction transaction0 = new Transaction();
      Account account0 = new Account();
      boolean boolean0 = transaction0.transfer(account0, account0, (-7157));
      assertFalse(boolean0);
  }
}