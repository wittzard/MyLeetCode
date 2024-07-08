# Write your MySQL query statement
SELECT tweet_id FROM Tweets
WHERE CHAR_Length(content) > 15;