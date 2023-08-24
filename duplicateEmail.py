Select email 
FROM Person 
Group By email
Having COUNT(email)>1 
