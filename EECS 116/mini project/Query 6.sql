select v1.name, count(distinct b1.email) as "advertisement-gap"
from vendor as v1, vendor_topics as vt, blurt as b1, blurt_analysis as ba1
where vt.vendorid = v1.id and ba1.topicid = vt.topicid and ba1.blurtid = b1.blurtid and ba1.email = b1.email
and b1.email 
not in (select b2.email
		from vendor as v2, blurt_analysis as ba2, blurt as b2, advertisement as a, user_ad as ua
		where a.vendorid = vt.vendorid and ba2.topicid = vt.topicid and ua.adid=a.id 
        and ua.email = b2.email and b2.email = ba2.email and ua.email = b1.email)
group by vt.vendorid
order by count(distinct b1.email) desc;