## Consistency

Consistency is the property of a transaction that guarantees that the changes done will be following all the defined rules.

### Database Transaction

- a transaction can involve multiple operations
- e.g. money transfer (**transaction**):

1. subtraction from buyer
2. addition to seller

- money and item transfer could be also one transfer

## ACID

- The properties 

1. atomic 
2. consistent
3. isolated
4. durable 

are commonly known as the ACID properties of transactions.

To test/showcase we connect to a postgres db on **digital ocean**:

to connect via psql:

```bash
psql -h host_name_or_ip -p port_number -U myuser mydb
```

1. Setup

```sql
-- Drop the table if it exists
DROP TABLE IF EXISTS bank_accounts;

-- Create the example table with the constraint for non-negative balance
CREATE TABLE bank_accounts (
    account_id SERIAL PRIMARY KEY,
    account_name TEXT,
    account_balance NUMERIC DEFAULT 0 CHECK (account_balance >= 0));

INSERT INTO bank_accounts (account_name, account_balance) VALUES ('A', 100), ('B', 200);
```

### Atomicity:

A database transaction must be done as a whole or not done at all.

This transaction is successfully executed and committed:
```sql
BEGIN;
UPDATE bank_accounts SET account_balance = account_balance - 50 WHERE account_name = 'A';
UPDATE bank_accounts SET account_balance = account_balance + 50 WHERE account_name = 'B';
COMMIT;
```

Here we violate our constraint (negative account balance)
```sql
BEGIN;
UPDATE bank_accounts SET account_balance = account_balance - 100 WHERE account_name = 'A';
UPDATE bank_accounts SET account_balance = account_balance + 100 WHERE account_name = 'B';
COMMIT;
```
Therefore, an error is raised and all queries of this transaction are aborted.

This is called Atomicity.

### Consistency

- Data is in a consistent state when a transaction starts and when it ends.

e.g.an application that transfers funds from one account to another

the consistency property ensures that the *total value of funds in both the accounts* is the same at the start and end of each transaction.

The funds remains constant:

```sql
SELECT sum(account_balance) FROM bank_accounts; --will be constant before and after each transaction: 300$
```

### Isolation

- A database transaction must also be isolated.

User A:
```sql
begin;
UPDATE bank_accounts SET account_balance = account_balance + 100 WHERE account_name = 'A';
```

User B:
```sql
SELECT account_balance FROM bank_accounts WHERE account_name = 'A'; -- sees 0 $;
```

User A:
```sql
commit;
```
User B:
```sql
SELECT account_balance FROM bank_accounts WHERE account_name = 'A'; --sees 100$;
```
First User B sees the old balance and then the updated balance after User A committed;
This demonstrates Isolation.

### Durability
- A database transaction must also be durable.
- The changes should be persistent.
- Once a change is done, it is written on the file system
- only another change will remove that change.

### Savepoints

- it is a way to split a tranaction into smaller blocks tha can b rolled back independently of each other:


```sql
begin;
UPDATE bank_accounts SET account_balance = account_balance - 50 WHERE account_name = 'A';
UPDATE bank_accounts SET account_balance = account_balance + 50 WHERE account_name = 'B';

SAVEPOINT money_transferA_to_B; --defining savepoint her

UPDATE bank_accounts SET account_balance = account_balance - 50 WHERE account_name = 'A';
UPDATE bank_accounts SET account_balance = account_balance + 50 WHERE account_name = 'B';

ROLLBACK TO SAVEPOINT money_transferA_to_B;
-- all queries after the savepoint are ignored

COMMIT; -- the first two querie are commited
```

### ACID COMPLIANCE

- postgres
- mysql
- sqlite

But ACID is a relational concept.

Another model is called BASE.
Most NoSQL use the BASE properties

- BASE properties focus on availability rather than consistency


### BASE Model

The BASE model is an alternative transaction model to the traditional ACID model.

The need for an alternative arose from the challenges faced when trying to achieve **high availability, fault tolerance, and scalability** in distributed and NoSQL databases. 

BASE emphasizes a looser, more scalable approach, which is a fit for many modern web and cloud-based applications.

1. **Basically Available**: 
- This suggests that the system does guarantee availability, but might not guarantee up-to-the-moment data accuracy across the entire system. 
- Data might be stale or might not be synchronized across all nodes
- In practice, this means that the system continues to function even if a portion of its infrastructure is offline or has failed.

2. **Soft State**: 
- The state of the system might change over time, even without any input. This is due to the eventual consistency model.
- The "soft" nature indicates that the system's state may not remain consistent at all times
-As opposed to "hard state" systems, where a change leads to an immediate and consistent new state everywhere, "soft state" systems recognize and allow temporary inconsistencies.

3. **Eventually Consistent**: 
- While the system may not always reflect a consistent state to all users at all times
-it promises that, given a certain amount of time without new updates, it will eventually converge towards a consistent state.
- This contrasts with the immediate consistency seen in ACID systems. 

The trade-offs between ACID and BASE depend on the specific use case. 

- **ACID** guarantees strict consistency, atomicity, and isolation, making it a fit for systems where correctness and consistency are paramount (e.g., banking transactions).

- **BASE**, on the other hand, trades consistency for availability and fault tolerance. It is more suitable for systems where high availability is essential, and where the application can tolerate temporary inconsistencies (e.g., social media posts, caching systems).

### Concurrent Writing Transactions

- Concurrent writing transactions are executed sequentially to prevent isolation issues.

- While the system executes the first transaction the rest stays “on hold”, waiting for the first to finish.
- So how do Write Transaction know they need to wait?

1. A writing transaction request arrives. It checks if it has access to the data. It does, so it executes.

2. When the transaction is executed, a **lock** is added to the database.

3. A second transaction request arrives. It checks if it has access to the data. It finds the lock, so it waits.

4. When the first transaction finishes, the lock is released and the next transaction checks again.

5. A COMMIT; and a ROLLBACK; will release the lock.

### Some writing transactions can be done simultaneously.

- Each new transaction has a lock and a key. 
- Checks if the key fits in the current lock.
- If the key fits, adds its own lock and executes.
- A third transaction will try to open every lock it finds on its way to the data. 
- If it succeeds, adds a new lock and executes.


### Locks in PostgreSQL

In databases, a lock is a mechanism employed to control access to a database resource by multiple transactions. 

The primary objective of locks is to ensure data integrity in concurrent access scenarios.

By using locks, PostgreSQL ensures that two transactions don't interfere with each other,
especially in scenarios that could compromise the integrity of the database.

- to see thr locks, run:
```sql
SELECT relation::regclass, mode, granted 
FROM pg_locks 
WHERE relation = 'my_table'::regclass;
```
1. **ACCESS SHARE**
   - **Typically Acquired By**: `SELECT ...`
   - **Conflicts with**: ACCESS EXCLUSIVE
   - **SQL Example**:
     ```sql
     SELECT * FROM my_table;
     ```

2. **ROW EXCLUSIVE**
- **Typically Acquired By**: `INSERT`, `UPDATE`, `DELETE`
- **Conflicts with**: SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE
- **SQL Example**:
     ```sql
     INSERT INTO my_table VALUES (1, 'data');
     UPDATE my_table SET column_name = 'new_value' WHERE condition;
     DELETE FROM my_table WHERE condition;
     ```

3. **SHARE**
  - **Typically Acquired By**: `CREATE INDEX` (not concurrently)
  - **Conflicts with**: ROW EXCLUSIVE, SHARE ROW EXCLUSIVE, EXCLUSIVE, ACCESS EXCLUSIVE
  - **SQL Example**:
     ```sql
     CREATE INDEX idx_column_name ON my_table(column_name);
     ```

4. **ACCESS EXCLUSIVE**
- **Typically Acquired By**: `ALTER TABLE`, `DROP TABLE`, etc.
- **Conflicts with**: All other locks (ACCESS SHARE, ROW SHARE, ROW EXCLUSIVE, SHARE UPDATE EXCLUSIVE, SHARE, SHARE ROW EXCLUSIVE, EXCLUSIVE)
- **SQL Example**:
     ```sql
     ALTER TABLE my_table ADD COLUMN new_column INT;
     DROP TABLE my_table;
     ```





```sql

```

```sql

```

```sql

```

```sql

```

```sql

```

```sql

```
