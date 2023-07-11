use FCC;

select * from Emp
select * from Dept

/* 1* */
select MAX(SAL) AS 'Highest Salary'
from Emp

/* 2 */
select AVG(SAL) AS 'Avg salary of Clerk'
from Emp
where JOB = 'CLERK'

/* 3 */
select AVG(SAL) AS 'Avg salary of Clerk'
from Emp
where DEPTNO = 30

/* 4 */
select MIN(SAL + COMM)
from Emp

/* 5 */
select COUNT(EMPNO) AS 'Number of Sales employees'
from Emp
where DEPTNO = 
				(select DEPTNO
				 from Dept
				 where DEPTNO = 30)

/* 6 */
select AVG(SAL) AS 'AVG Salary',DEPTNO
from Emp
group by DEPTNO


/* 7 */
select *
from Emp
where SAL > 1000 AND JOB = 
							(select JOB
							from Emp
							where ENAME = 'SMITH')

/* 8 */
select AVG(SAL),JOB, DEPTNO
from Emp
group by JOB,DEPTNO


/* 9 */
select *
from Emp,Dept
where Emp.DEPTNO = Dept.DEPTNO AND DNAME = 
										(select DNAME
										 from Dept
										 where DNAME = 'SALES' OR DNAME = 'OPERATIONS')

/* 10 */
select MAX(SAL),DEPTNO
from Emp
where SAL > 100
group by DEPTNO

/* 11 */
select  EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, Emp.DEPTNO
from Emp,Dept
where Emp.DEPTNO = Dept.DEPTNO AND LOC = 
										(select LOC 
										 from Dept
										 where LOC = 'NEW YORK')
/* 12 */
select MAX(avg_sal.AverageSalary) AS 'Max Dept Average Salary'
from (  select AVG(SAL) AS 'AverageSalary'
		from Emp
		group by DEPTNO )avg_sal


/* 13 */
select MIN(SAL),DEPTNO
from Emp
group by DEPTNO
HAVING MIN(SAL) > 
					(select MIN(SAL)
					 from Emp
					 where DEPTNO = 30)





