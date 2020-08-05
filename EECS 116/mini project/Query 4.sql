select user.name
from celebrity, user
where celebrity.email = user.email
and celebrity.email not in (select follower from follow);