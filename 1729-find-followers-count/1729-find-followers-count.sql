# Write your MySQL query statement below
SELECT fl.user_id,COUNT(DISTINCT fl.follower_id) AS followers_count
FROM followers fl GROUP BY fl.user_id ORDER BY fl.user_id ASC