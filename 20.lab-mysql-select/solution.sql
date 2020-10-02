USE publications;

SELECT * from titleauthor; #relates ta.au_id with ta.title_id
SELECT * from authors; #a.au_id, a.au_lname, a.au_fname
SELECT * from titles; #relates t.title_id with t.title AND ALSO has t.pub_id that relates with publishers)
SELECT * from publishers; #p.pub_name AND p.pub_id



SELECT 
a.au_id as Author_ID,
a.au_lname as Last_Name,
a.au_fname as First_Name,
#ta.title_id,
#ta.au_id,
t.title as Title,
#t.title_id,
#t.pub_id,
#p.pub_id,
p.pub_name as Publisher

FROM titleauthor as ta

LEFT JOIN
authors as a ON ta.au_id = a.au_id

JOIN
titles as t ON ta.title_id = t.title_id

JOIN
publishers as p ON t.pub_id = p.pub_id;

