select vendor.name, vendor_ambassador.email, count(follow.followee) as followers
from vendor, vendor_ambassador, user, follow
where vendor.id = vendor_ambassador.vendorid and vendor_ambassador.email = user.email and vendor_ambassador.email = follow.followee
group by vendor_ambassador.email;