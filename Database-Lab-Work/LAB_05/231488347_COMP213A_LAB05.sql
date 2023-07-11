use Fcc

select * from	Emp	
select * from	Dept

/* 1 */
INSERT INTO	Emp	( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO )VALUES	(8000,'JONATHAN','JANITOR',7902,CONVERT (varchar(10),GETDATE(), 6),1900,60);
INSERT INTO	Emp	( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO )VALUES	(9000,'MARKY','OPERATOR',7902,CONVERT (varchar(10),GETDATE(), 6),2000,40);

INSERT INTO	Dept ( DEPTNO, DNAME, LOC)	VALUES	(50,'MANAGEMENT','TEXAS');
INSERT INTO	Dept ( DEPTNO, DNAME, LOC)	VALUES	(60,'CLEANING','CALIFORNIA');


/* 2 */
INSERT INTO Emp(EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO) 
	(select EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO
	from Emp
	where EMPNO = 8000 )


/* 3 */
Update Emp
SET COMM = 2000
where COMM = 1400


/* 4 */
DELETE 
from Emp
where SAL = 3000

/* 5 */
DELETE 
from Emp
where DEPTNO = (select DEPTNO
				from Dept
				where DNAME = 'SALES')

/* 6 */
MERGE Emp 
USING Dept 
ON(Emp.DEPTNO = Emp.DEPTNO)
WHEN MATCHED AND Emp.DEPTNO = 40 THEN
UPDATE SET SAL = 120
WHEN NOT MATCHED THEN
INSERT ( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO )VALUES(8001,'NEW GUY','JANITOR',7902,CONVERT (varchar(10),GETDATE(), 6),1900,60);

/* 7 */
BEGIN TRANSACTION
INSERT INTO	Emp	( EMPNO, ENAME, JOB, MGR, HIREDATE, SAL,DEPTNO )VALUES	(7369,'JOE','JANITOR',7902,CONVERT (varchar(10),GETDATE(), 6),20000,60);

select *
from Emp
where EMPNO = 7369 ROLLBACK TRANSACTION


/* 8 */
create table Location(
	ID INT PRIMARY KEY,	
	location_field VARCHAR (20) DEFAULT 'BOSTON')

/* No describe in SQL SERVER */
EXEC sp_columns 'dbo.Location'
EXEC sp_help 'dbo.Location'

/* 9 */
DROP TABLE Location