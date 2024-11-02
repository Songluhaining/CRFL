package main; 
public  class  Transaction {
	

	//__feature_mapping__ [Transaction] [4:22]
	public boolean transfer(Account source, Account destination, int amount) {
		if (!lock(source, destination)) return false;
		try {
			if (amount <= 0) {
				return false;
			}
			if (!source.update(amount * -1)) {
				return false;
			}
			if (!destination.update(amount)) {
				source.undoUpdate(amount * -1);
				return false;
			}
			return true;
		} finally {
			source.unLock();
			destination.unLock();
		}
	}

	

	//__feature_mapping__ [Transaction] [24:30]
	private static synchronized boolean lock(Account source, Account destination) {
		if (source.isLocked()) return false;
		if (destination.isLocked()) return false;
		source.lock();
		destination.lock();
		return true;
	}


}
