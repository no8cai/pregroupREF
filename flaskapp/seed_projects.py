from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models import Project

with app.app_context():

     project1=Project(creatorId=1,title="newproject01",category="art",subcategory="concept art",city="houston",state="texas",country="usa",imageurl="http://image.com/image01",fundingGoal=200000,startDate="05-02-2023",endDate="10-10-2023",description="this is a good place to start",risk="people dont like arts",budget=3000)

     project2=Project(creatorId=2,title="newproject02",category="music",subcategory="concept art",city="houston",state="texas",country="usa",imageurl="http://image.com/image01",fundingGoal=200000,startDate="05-02-2023",endDate="10-10-2023",description="this is a good place to start",risk="people dont like arts",budget=3000)

     project3=Project(creatorId=3,title="newproject03",category="tech",subcategory="concept art",city="houston",state="texas",country="usa",imageurl="http://image.com/image01",fundingGoal=200000,startDate="05-02-2023",endDate="10-10-2023",description="this is a good place to start",risk="people dont like arts",budget=3000)


     db.session.add(project1)
     db.session.add(project2)
     db.session.add(project3)
     db.session.commit()  
     
        