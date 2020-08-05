select topic.id, topic.description, IFNULL(COUNT(blurt_analysis.topicid),0) as count
from topic left join blurt_analysis on topic.id = blurt_analysis.topicid
group by topic.id
order by topic.id;