# COMP702-AI-Workplace-Safety
GitHub Repository for the Research and Development Project "Inviol Body Camera Project"

The Inviol Body Camera Project is a project that works with Inviol through a research and development team from AUT.
This github serves as a portfolio of the deliverables that were achieved during the timespan of the project.

**Reports**
Team Proposal:
Mid Term Report: 

**Scripts**
The scripts for the raspberry pi can be found in the 'Scripts' directory of this GitHub. The scripts run on the raspberry pi and capture the video, upload
it to the Clients Azure Blob Storage, draws the bounding boxes using our trained model and then uploads the boudning box video to the Azure Storage. 
These videos create an 'event' which is created in the Clients event api, to then be viewable on their application.

**Diagrams**
Diagrams the explain the system of our project, the raspberry pi and how the model works to create the videos is found in the 'Diagrams' directory
of this GitHub

**Test Videos** 
These videos were taken on the raspberry pi. We took these videos using the PPE equipment provided by the client Inviol, and used these videos to train
our model
Link: https://autuni-my.sharepoint.com/:f:/g/personal/zqj5293_autuni_ac_nz/Enaec8vegTRKtUKqLntqIcYBy8BcZlac9sVr55XwR8EyrA?e=84fHPA 

**Bounding Box Videos**
These videos have been labeled using our model and detect people, helmets and hivis
Link: https://autuni-my.sharepoint.com/:f:/g/personal/zqj5293_autuni_ac_nz/EkJQKQdx1ENEqEZekRDGdl4BHusCcqt_LV2z_4uMyWdqsg?e=wRaQBL 

**Model**
The model weights and config are avalible to view through this link, as they are to large to upload to GitHub.
Link: https://autuni-my.sharepoint.com/:f:/g/personal/zqj5293_autuni_ac_nz/Ekf3Luc1gedGr4aZux2ytZ8BjvoGZ6lz8hUJ2PBnqM2EHg?e=MdjLoE


**Dataset**


These dataset was collected before the model training phase. It included all the required elements (Mask, PPE). All the images are labelled. However, due to problems from formatting of images, it was not be used eventually. Two zipped folder for Mask data and PPE data has already uploaded on ondrive. Please visit by clicking the link below. 
https://autuni-my.sharepoint.com/:f:/g/personal/tfp3422_autuni_ac_nz/Etw-2TmsqkVDj2qBZc5EWgEBMM1lsj51sH2AFMIIEyf-EQ?e=feEfMa

**Video Frame**

https://autuni-my.sharepoint.com/:f:/g/personal/tfp3422_autuni_ac_nz/ErbuNl9zHpROsI0yyIdMNkcBeEsq2OhSk9pobS9kHcghGA?e=WgWzun

