create database FCC;

use FCC; /* Selects FCC database to be selected and be used going forward */
/* Creates table and addes the attributes we entered */
/* int for numbers. char for string and varchar works for everything */
create table student(

	id int primary key,	/* primary key makes it so that id cannot be duplicated for different entries */
	STUname varchar (30) not null, /* not null, makes it so that we cannot leave it empty when entering data */
	major varchar (25),
)

/* insert data into table student */
insert into student (id,STUname,major) values (01,'sam','CS'); /* used to enter data when you want to enter into a specific attribute */
insert into student  values (02,'sam2','CS'); /* Enters values into all attributes in order */
insert into student  values (03,'sam3','CS');

/*Prints all data in table, student  */
select * from student

/* Data retreival */
select	STUname	/* attribute */
from	student	/* Table name */
where	major = 'CS2' OR id = 03	/* condition */
order by id /*orders table by the attribute mentioned in ascending order */


/* update data */
update student
set STUname = 'sam2', major = 'Math'
where id = 02

/* delete data */
delete from student 
where id = 02;

/* Removes table from database */
drop table student