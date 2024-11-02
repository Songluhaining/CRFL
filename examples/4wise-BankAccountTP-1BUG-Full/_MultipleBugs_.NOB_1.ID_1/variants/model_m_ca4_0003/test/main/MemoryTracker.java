package main;
import javassist.*;

public class MemoryTracker {
    public static void main(String[] args) {


        try {
            ClassPool pool = ClassPool.getDefault();
            pool.insertClassPath("/home/whn/Desktop/BankAccountTP/4wise-BankAccountTP-1BUG-Full/_MultipleBugs_.NOB_1.ID_1/variants/model_m_ca4_0003/build/main/main");
            CtClass cc = pool.get("main.Transaction");

            CtMethod method = cc.getDeclaredMethod("transfer");

            method.insertBefore("amount=-1151;");
            cc.toClass();
            Transaction_ESTest obj = new Transaction_ESTest();
            obj.test4();
            cc.detach();
        } catch (NotFoundException e) {
            throw new RuntimeException(e);
        } catch (CannotCompileException e) {
            throw new RuntimeException(e);
        } catch (Throwable e) {
            throw new RuntimeException(e);
        }
    }
}
