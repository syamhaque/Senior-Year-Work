select user.name, count(follow.followee) as followers
from celebrity, follow, user
where follow.followee = celebrity.email and follow.followee = user.email
group by follow.followee;