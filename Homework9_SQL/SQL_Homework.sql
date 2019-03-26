use sakila;
SET SQL_SAFE_UPDATES = 0;

-- 1a. Display the first and last names of all actors from the table actor.

SELECT first_name, last_name
FROM actor

-- 1b. Display the first and last name of each actor in a single column 
-- In upper case letters. 
-- Name the column Actor Name.

SELECT CONCAT(first_name, " ", last_name) as "Actor Name"
FROM actor;
WHERE "Actor Name" = UPPER("Actor Name")

-- 2a. You need to find the ID number, first name, and last name of an actor, 
-- of whom you know only the first name, "Joe."
-- What is one query would you use to obtain this information?

SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name = "Joe"

-- 2b. Find all actors whose last name contain the letters GEN:

SELECT first_name, last_name
FROM actor
WHERE last_name LIKE "%GEN%"

-- 2c. Find all actors whose last names contain the letters LI. 
-- This time, order the rows by last name and first name, in that order:

SELECT last_name,  first_name
FROM actor
WHERE last_name LIKE "%LI%"

-- 2d. Using IN, display the country_id and country columns of the following countries: 
-- Afghanistan, Bangladesh, and China

SELECT country_id, country
FROM country
WHERE country in ("Afghanistan", "Bangladesh", "China")

-- 3a. You want to keep a description of each actor. You don't think you will be performing 
-- queries on a description, so create a column in the table actor named description and use 
-- the data type BLOB 
-- (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).

ALTER TABLE actor
ADD description blob;

-- 3b. Very quickly you realize that entering descriptions for each actor is too much effort. 
-- Delete the description column.

ALTER TABLE actor
DROP description;

-- 4a. List the last names of actors, as well as how many actors have that last name.

SELECT last_name, count(*) 
FROM actor
GROUP BY last_name

-- 4b. List last names of actors and the number of actors who have that last name, 
-- but only for names that are shared by at least two actors

SELECT last_name, count(*)
FROM actor
GROUP BY last_name
HAVING COUNT(*) > 1

-- 4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. 
-- Write a query to fix the record.

-- First should search for the name "Groucho"
SELECT first_name, last_name
FROM actor
WHERE first_name = "Groucho" and last_name = "Williams"

-- Then update
UPDATE actor
SET first_name = "HARPO"
WHERE first_name = "Groucho" and last_name = "Williams"

-- Then check name
SELECT first_name, last_name
FROM actor
WHERE first_name = "HARPO"

-- 4d. Perhaps we were too hasty in changing GROUCHO to HARPO. 
-- It turns out that GROUCHO was the correct name after all! 
-- In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.

UPDATE actor
SET first_name = "GROUCHO"
WHERE first_name = "HARPO"

-- 5a. You cannot locate the schema of the address table. 
-- Which query would you use to re-create it?

SHOW CREATE SCHEMA address;

-- 6a. Use JOIN to display the first and last names, as well as the address, of each staff member.
-- Use the tables staff and address:

SELECT first_name, last_name, address
FROM staff s
INNER JOIN address a ON a.address_id = s.address_id

-- 6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. 
-- Use tables staff and payment.

SELECT first_name, last_name, sum(amount)
FROM staff s
INNER JOIN payment p ON s.staff_id = p.staff_id
WHERE p.payment_date LIKE "2005-08%"
GROUP BY s.staff_id

-- 6c. List each film and the number of actors who are listed for that film. 
-- Use tables film_actor and film. Use inner join.

SELECT title, count(actor_id)
FROM film f
INNER JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY title

-- 6d. How many copies of the film Hunchback Impossible exist in the inventory system?

SELECT title, count(inventory_id)
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
WHERE title = "Hunchback Impossible"

-- 6e. Using the tables payment and customer and the JOIN command, 
-- list the total paid by each customer. 
-- List the customers alphabetically by last name

SELECT first_name, last_name, sum(amount)
FROM customer c
INNER JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id
ORDER BY last_name

-- 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also 
-- soared in popularity. Use subqueries to display the titles of movies starting with 
-- the letters K and Q whose language is English.

-- First look at language to figure out Language ID. English = 1
SELECT * FROM sakila.language;

SELECT title 
FROM film
WHERE title LIKE "K%" 
	OR title LIKE "Q%"
    AND language_id = 1

-- 7b. Use subqueries to display all actors who appear in the film Alone Trip.

SELECT first_name, last_name, title
FROM actor a
INNER JOIN film_actor fa ON a.actor_id = fa.actor_id
INNER JOIN film f ON f.film_id = fa.film_id
WHERE title = "Alone Trip"

-- 7c. You want to run an email marketing campaign in Canada, 
-- for which you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.

SELECT * from sakila.customer -- address_id
SELECT * from sakila.address -- address_id, city_id
SELECT * from sakila.city -- city_id, country_id
SELECT * from sakila.country -- country_id

SELECT first_name, last_name, email, country
FROM address a
INNER JOIN customer cu ON a.address_id = cu.address_id
INNER JOIN city ci ON a.city_id = ci.city_id
INNER JOIN country co ON ci.country_id = co.country_id
WHERE country = "Canada"

-- 7d. Sales have been lagging among young families, and you wish to target all family movies 
-- for a promotion. Identify all movies categorized as family films.

SELECT * FROM film -- film_id
SELECT * FROM film_category -- film_id, category_id
SELECT * FROM category -- category_id Family = 8

SELECT title
FROM film f
INNER JOIN film_category fc ON f.film_id = fc.film_id
WHERE category_id = 8

-- 7e. Display the most frequently rented movies in descending order.

SELECT * FROM film -- film_id
SELECT * FROM inventory -- film_id, inventory_id
SELECT * FROM rental -- inventory_id, rental_id

SELECT title, count(rental_id)
FROM film f
INNER JOIN inventory i ON f.film_id = i.film_id
INNER JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY title
ORDER BY COUNT(rental_id)DESC

-- 7f. Write a query to display how much business, in dollars, each store brought in.

