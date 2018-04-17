# ElectronicsProject

I) SeatMonitor
   1. Requirements to run
      A) Django
      B) boto3 (pip install boto3)
      	 i) setup
	    a) set up credentials in ~/.aws/credentials
	       [default]
	       aws_access_key_id = AKIAIEHXCGSMBLGMYJGQ	
	       aws_secret_access_key = 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   
	    b) set up default region in ~/.aws/config
	       [default]
	       region=us-east-1	
   2. Description
      This app uses information from a Postgres DB table in AWS to display which study rooms are available in specific buildings on UGA's Campus.
      Our application solves the issue of students searching for study rooms and allows for a cheap solution. In the future we look to implement
      this project on an iPhone application

II) Arduino Code
   1. Requirements to run
      a) arduino board
      b) **arduino code program**