/*
 * This file was automatically generated by EvoSuite
 * Sat Feb 06 15:47:03 GMT 2021
 */

package main;

import org.junit.Test;
import static org.junit.Assert.*;
import main.Account;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true, useJEE = true) 
public class Account_ESTest extends Account_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.update(36500);
      assertTrue(boolean0);
      
      int int0 = account0.estimatedInterest(36500);
      assertEquals(73000, int0);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.undoUpdate(0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      Account account0 = new Account();
      account0.interest = (-596);
      int int0 = account0.estimatedInterest((-596));
      assertEquals((-596), int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      Account account0 = new Account();
      int int0 = account0.calculateInterest();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.update(36500);
      assertTrue(boolean0);
      
      int int0 = account0.calculateInterest();
      assertEquals(2, int0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      Account account0 = new Account();
      account0.balance = 0;
      account0.balance = (-4356);
      account0.balance = (-30827);
      int int0 = account0.calculateInterest();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.undoUpdate(2);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.undoUpdate((-367));
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.update((-1794));
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.update(0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      Account account0 = new Account();
      account0.lock();
      boolean boolean0 = account0.isLocked();
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      Account account0 = new Account();
      boolean boolean0 = account0.isLocked();
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      Account account0 = new Account();
      int int0 = account0.estimatedInterest((-1));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      Account account0 = new Account();
      account0.unLock();
  }
}