Inspiration
There are lot of hackathons and its difficult to efficiently search and explore them. I wanted to come up with an easier way to search for hackathons. So, I thought of combining the MLH Hackathon Listings, Alexa and the cloud. I wanted to provide users with a convenient interface for MLH.

What it does
Hackathon Finder is an Alexa skill used to find hackathons based on state, city and ranges of dates. The hackathon information is extracted from the MLH Website.

How is it built
The hackathon data was periodically extracted from MLH website using a web crawler. This data was stored in AWS RDS. I used flask-ask to build an Alexa skill which would utilize the AWS RDS data to answer to user queries in realtime. Amazon EC2 instances were used for computing resources.

Challenges we ran into
Software Architecture - Decision between using Dynamo DB and AWS RDS(MySQL) i.e. choosing between SQL or a NoSQL datastore.
Amazon Skill service downtime.
Troubleshooting AWS Security Group related problems in connecting our application to AWS MySQL.
Accomplishments that we're proud of
Achieving realtime performance.
Designing intuitive dialog system for Alexa.
What we learned
Learning overnight how to build an Alexa skill.
Experience with AWS Services like EC2, RDS MySQl, Amazon Dynamo DB.
What's next for Hackathon Finder
Adding recommendations model to recommend hackathons for users to go to.
Keeping track of hackathons and the related deadlines like application date.
Providing an interface for registering for a hackathon.
