-- There are 3 tables in the database. The first two are book and member, for the library's books and members. The third table, checkout, is to keep track of which member checks out which books when, and when they return them.

-- Table: book
-- column	type
-- id	serial
-- title	varchar(255)
-- copies	int
-- Table: member
-- column	type
-- id	serial
-- name	varchar(255)
-- Table: checkout
-- column	type
-- book_id	int
-- member_id	int
-- checked_out_on	timestamp
-- returned_on	timestamp
-- Schema diagram
-- schema

-- 4
-- Borrowed book report
-- 5 PTS

-- For this problem, write an SQL query that will generate a "borrowed books" report. The report should include:

-- The book title
-- The name of the borrower
-- The date that the book was checked out
-- It should only show books that are currently checked out, who checked it out, and the timestamp of when it was checked out.

-- A book is checked out if the checked_out_on column has a value and the returned_on column does not have a value.

SELECT book.title, member.name, checkout.checked_out_on
FROM book
INNER JOIN checkout
  ON (book.id = checkout.book_id)
INNER JOIN member
  ON (checkout.member_id = member.id)
WHERE checkout.returned_on IS NULL;

-- For this problem, write an SQL query for a report for all of the books in the library. For each book it should show:

-- book title
-- number of copies
-- checked_out_on (if it's ever been checked out)
-- returned_on (if it's ever been checked out)
-- name of the borrower (it it's ever been checked out)
-- This is similar to what you wrote in the previous problem. However, you'll want to show all books and all of the checkouts.

-- book.title, num of copies, checkout_out_on (if not null), returned_on (if not null), borrower

-- Write your query for "complete book histories"
SELECT book.title, book.copies, checkout.checked_out_on, checkout.returned_on, member.name
FROM book
LEFT OUTER JOIN checkout
  ON (book.id = checkout.book_id)
LEFT OUTER JOIN member
  ON (checkout.member_id = member.id);