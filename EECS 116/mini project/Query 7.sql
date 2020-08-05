select distinct A.name, B.name
from blurt_analysis Ab, blurt_analysis Bb, user A, user B
where Ab.email != Bb.email and Ab.email = A.email and Bb.email = B.email and Ab.topicid = Bb.topicid
and Ab.email not in (select follow.follower from follow where follow.followee = Bb.email);