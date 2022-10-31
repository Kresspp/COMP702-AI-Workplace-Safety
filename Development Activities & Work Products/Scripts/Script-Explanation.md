**Explaining Scripts**

Three scripts are used on the Raspberry Pi to run the video capture, and upload these videos to Inviols Azure Storage, event API, which allows our videos 
to be viewable on their application (in the development enviroment)
These scripts are:
- event_api.py
- shapley_video.py
- mastercamera.py

The below screenshots show the result of running these scripts.
This image shows a successful run of the scripts, where the video is created, uploaded to the Azure Storage, and then added to the event api
![image](https://user-images.githubusercontent.com/80650732/198967782-40bb7fa2-23e8-4f54-a2fd-c08c84b85fbc.png)

This image shows the out_0.mp4 video and the out_bb_0.mp4 video that have been uploaded to the azure storage. The out_0.mp4 is the original video, while
the out_bb_0.mp4 video is the video that contains the bounding boxes that have been added from the model
<img width="1512" alt="image" src="https://user-images.githubusercontent.com/80650732/198968005-bf6c3da7-c88e-406c-88e3-2afa90b37014.png">

This image shows the event in the api
<img width="1405" alt="image" src="https://user-images.githubusercontent.com/80650732/198968501-032b7799-3ed9-47bc-95a2-dcec00557b45.png">

This image shows a test video that is viewable on Inviol's application
![Uploading image.png…]()
