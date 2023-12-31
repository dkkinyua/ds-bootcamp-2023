**Question: Imagine you are a Product Data Scientist at Instagram. Explain how you would describe the success of Instagram TV(IGTV).**

**Explanation and Solution**:
Instagram is one of the most used social media applications today and has more than 100 million users who use Instagram to share posts, create content, and send messages.

Instagram TV is an Instagram product where Instagram users can share short videos and create content up to 10 minutes per video

We have seen a great improvement in the success of IGTV in terms of the user engagement metric and have used a xgboost model to gauge its success.

Here, I would use the User Engagement metric which includes the following:
	(i) Viewership
    	(ii) Watch time
	(iii) User Retention

**(i) Viewership:**
	
The viewership metric for IGTV measures the total number of times your IGTV videos have been viewed by users on Instagram. It provides valuable insights into the reach and engagement of your video content. Viewership can be expressed as a cumulative count across all your IGTV videos or as an average view count per video.

**Formulae for Calculating Viewership Metric:**
Total View Count (Cumulative):
The total view count represents the total views for all your IGTV videos.

    > **Formula: Total View Count = View Count of Video 1 + View Count of Video 2 + ... + View Count of Video x**

**(ii) Watch Time:** 

Watch time is an essential metric for evaluating the engagement and retention of your IGTV video content. It quantifies the cumulative amount of time viewers have dedicated to watching your videos. This metric helps you assess your video content strategy's overall impact and effectiveness.

**Formula for Calculating Watch Time Metric:**
The formula for calculating the watch time metric on IGTV is straightforward. It involves summing up the total duration of time users have spent watching your videos:

    > **Watch Time (in seconds) = Duration of Video 1 (in seconds) + Duration of Video 2 (in seconds) + ... + Duration of Video x (in seconds)**

**(iii) User Retention:**

User retention, often expressed as a percentage, measures the proportion of viewers who watch a significant portion of your IGTV video content without dropping off. It helps assess the quality of your content and its ability to keep viewers engaged throughout the video's duration.

Let’s say that a successful threshold for User Retention for Instagram TV is 80%, this would act as a benchmark to gauge its success.

**Formula for Calculating User Retention Metric:**
The formula for calculating user retention on IGTV involves determining the percentage of viewers who watched a specific portion of the video (e.g., from the beginning to a specified time point). The formula is as follows:
   > User Retention (%) = (Number of Viewers at Time T / Total Views) x 100 (expressed as a percentage).

**(iv) Increase in followers:**

An increase in followers also shows the success of Instagram TV. If the successful threshold for follower increase is, let's say, 500 for heavy content creators(those who create content daily), this would show the success of Instagram TV


**Here's the process I would take to solve this question:**

**1. Collect Data:** Gather data related to your IGTV content, such as video duration, content category, post date, and any other relevant features. Also, include the user engagement metric you want to predict, such as user retention.

**2. Data Preprocessing:** Clean and preprocess your dataset. Handle missing values, encode categorical variables, and split the data into training and testing sets

**3. Import necessary libraries i.e. xgboost and pandas/pyforest**:
Here's to import your libraries and packages:

<pre>

import xgboost as xgb
from sklearn import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

</pre>

**4. Load and Prepare your dataset:**
Here's how to load and prepare your dataset:
<pre>

data = pd.read_csv("MOCK_DATA (2).csv")

X = data.dropna("videos", axis = 1)
y = data["videos"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

</pre>

**5. Train your XGBoost model:**
This is how to train your XGBoost model for your data:

<pre>

model = xgb.XGBClassifier()
model.fit(X_train, y_train)

</pre>

**6. Evaluate your model:**
Evaluate the model on your testing data to gauge the success of the user engagement metric prediction:

<pre>


accuracy = accuracy_score(y_test, y_pred)
print(f"The accuracy of this is: {accuracy}")

# Generate a classification report for detailed metrics
report = classification_report(y_test, y_pred)
print(report)

</pre>

This will provide you with metrics like the accuracy of the model, precision, and F1-score to gauge the performance of your model.

**7. Interpret your results:**
I interpreted the results and came to the conclusion that IGTV is a success according to the user engagement metric.
