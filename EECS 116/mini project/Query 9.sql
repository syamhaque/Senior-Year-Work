select topic.id, topic.description, blurt.location, count(blurt.email) as total_blurts, avg(blurt_analysis.sentiment) as average_sentiment
from topic, blurt, blurt_analysis
where topic.id = blurt_analysis.topicid and blurt_analysis.email = blurt.email and blurt_analysis.blurtid = blurt.blurtid
group by topic.id, topic.description, blurt.location
having average_sentiment < 0;
