# ppbc-capstone
#Problem statement 
Write a py file to automate the process to determine the certificate eligibility of learners upon course completion and understand the overal performance of the learners. 

#A brief summary of my solution to the problem. 
The data needed are in a few different Google sheet. 
First, data cleaning will be done and work on the missing values.
Join the necessary info into a dataframe. Simple data analysis will be done to understand the learners performance according to courses.
Then, from the combined_dataframe, run the py file to identify the learners who are eligible to receive certificates. In the py file, it contains the criteria for receiving a certificate

This process is important because 
(1) automating the process so that there are lesser manual work;
(2) we can understand the learners performance and satisfaction scores. 


#A summary of your technical solution. This can include more technical descriptions of the work you did.
1. using pandas to read and analyse the google sheet file
2. check on the missing values, fill in the missing values, remove the unnecessary columns/ rows
3. join the 3 dataframe into 1 on email
4. run the basic analysis to understand the combined_dataframe
5. create a function to run through some conditions and find out whether a particuar learner will be eligible for a certificate (then save it as py file)
6. run analysis to undestand more about the population (course demand, satisfaction, perfomance)
7. plot 1 or 2 graphs to observe patterns


#A brief summary of each of the files in your repository.
1. jupyter notebook file with all the working steps
2. py file on the automation for certificate

#Contact information so people can reach out to you to learn more.
Pearl - pearl@excelerate.asia
