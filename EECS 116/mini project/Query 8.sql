select distinct fa.follower as A, fa.followee as B, fb.followee as C
from follow fa, follow fb
where fa.followee = fb.follower and fb.followee != fa.follower
and (fa.follower, fb.followee) not in (select * from follow);
