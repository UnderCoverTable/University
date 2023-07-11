use FCC;

/* Task1 */

select ROUND (194.382, 2) 
select ROUND(194.382, -2)



/* Task2 */

/* 1 */
select ENAME AS 'Employee', HIREDATE AS 'Hiring Date', EMPNO AS 'Employee Number',Dept.DNAME AS 'Department Name'
from Emp,Dept
where Emp.DEPTNO = Dept.DEPTNO and (Emp.MGR = 7698 or Emp.MGR = 67839)
ORDER by Emp.EMPNO ASC

/* 2 */
select  EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM AS 'BONUS', DEPTNO
from Emp
where JOB != 'CLERK' AND JOB != 'SALESMAN'

/* 3 */
select EMPNO,Emp.DEPTNO
from Emp
FULL OUTER JOIN Dept ON Emp.DEPTNO = Dept.DEPTNO

/* 4 */
select *
from Emp,Dept

/* 5 */
select  ( SUM(comm) / COUNT(EMPNO) ) AS ' Including NULL Values'
from Emp

select  AVG(COMM) AS ' Excluding NULL Values'
from Emp


/* 6 */
select *
from  Emp job, Emp emp
where	job.EMPNO = emp.EMPNO


/* 7 */
select COUNT(EMPNO) AS 'Employees in Sales and Operations'
from Emp,Dept
where Emp.DEPTNO = Dept.DEPTNO and (DNAME ='SALES' or DNAME = 'OPERATIONS') 


/* 8 */
select SUM(SAL) AS 'Salary Distributed to Research Department'
from Emp,Dept
where Emp.DEPTNO = Dept.DEPTNO and DNAME = 'RESEARCH'
