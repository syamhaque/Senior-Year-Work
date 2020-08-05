select user.name, count(blurt.email) as blurts
from celebrity, user, blurt
where blurt.email = user.email and blurt.email = celebrity.email
group by celebrity.email
order by blurts desc;