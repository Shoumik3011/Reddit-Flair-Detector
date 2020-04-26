Reddit-Flair-Detector
=========

## Introduction 
Reddit-Flair-Detector is a flair detector for posts belonging to [r/india](https://www.reddit.com/r/india/) subreddit on Reddit. Its web app is deployed using Heroku which can be accessed [here](https://red-flair-detector.herokuapp.com/). It scrapes post's using the URL and then uses an SVC model to predict the flair of that post.The link for the automated testing can be accessed  [here](https://red-flair-detector.herokuapp.com/automated_testing) .

## How to Use the App 
### Steps to use the Web-app to predict flairs of posts.

1. Open the app at [Reddit-Flair-Detector](https://red-flair-detector.herokuapp.com/).
![](images/image%20(1).png)

2. Open the reddit post belongin to [r/india](https://www.reddit.com/r/india/) subreddit. Copy the full URL of the post. 


3. Paste the Link in the Url Box and click submit.
![](images/image%20(2).png)

4. This will redirect you to [Flairs Detected](https://red-flair-detector.herokuapp.com/Flairs_Detected) Page. Here it will display your submitted URL on the top, and the flair that has been predected. By clicking on the link which is highlighted in blue, it would re-direct to the URL which was submitted earlier. You might need to re-fresh the pages one or twice to load the content from Heroku Servers.
![](images/image%20(3).png)

### Automated Testing....

1. Go to the link [Automated Testing](https://red-flair-detector.herokuapp.com/automated_testing).
![](images/image%20(21).png)

2. Upload the .txt file containing valid URL's and click Upload.

3. A JSON file will start downloading after a few seconds.This JSON file will contain the URL's along with the flair detected. 

1.Open the app at 
## Tools Used
* Python3
* Sci-kit Learn
* NLTK
* FLASK
* Flask-WTF
* D3.JS
* Xgboost
* Praw
* Jupyter
* HTML/CSS
* Pandas 
* Numpy
* Heroku
* Flask-JSON
* Werkzeug

## File Information--->Details about each file or folder in the directory
* Reddit-Flair-Detector: It contains all the files and directories.
  * app.py : The Main Python file for Flask Based Web App.
  * forms.py : A Python file for taking input from the user using Flask-WTF library.
  * model : A Pickled-version of ML model which is used to make predictions.
  * model.py : A Python file for predicting Flair.
  * nltk.txt : A txt file for Heroku for downloading "stopwords","wordnet","punkt" which are used for data cleaning.
  * Procfile : A file which contains the command which are required to run the flask based app on Heroku.
  * requirements.txt : A txt file for Heroku to satisfy the requirements to run the web app.
  * tfidf : A Pickled-version of TF-IDF VECTORIZER for converting words into vectors.
* Data : It contains all the data used in the project.
  * csv_files : It contains the data in .csv files.
* images : It contains all the images of the web app.
* others : It contains the .ipynb files which are used for scraping data, cleaning data, combining data, training various models and analysing data. 
* static : It contains the .css files for the web-app.
* templates : It contains the .html files for the web-app.

## Steps To Run Red-Flair
### Hosting Web App On Local Host
1. Clone The Repository.
```bash
git clone https://github.com/Shoumik3011/Reddit-Flair-Detector.git
```
2. change directory to Reddit-Flair-Detector.
```bash
cd Reddit-Flair-Detector
```
3. Follow this [tutorial](http://www.storybench.org/how-to-scrape-reddit-with-python/) to get client id,etc. of Reddit.
4. Open model.py and enter the information like client id,etc. in get_flair().
5. Run the app.py file.
```bash
python app.py
```
### For Re-training the model or data-analysis or data-scarping or data-combining. <a link="re"/>
1. Clone The Repository.
```bash
git clone https://github.com/Shoumik3011/Reddit-Flair-Detector.git
```
2. change directory to Reddit-Flair-Detector.
```bash
cd Reddit-Flair-Detector
```
3. Copy and Paste the .ipynb files from ./others/  to ./data/csv_files
```bash
cp ./others/<file>.ipynb ./Data/csv files
```
4. Open Jupyter 
``` bash
jupyter notebook
```
5. Go the the .ipynb file in /Data/csv files and select Cell > "Run All".
6. Copy paste the "model" and "tfidf" files back to /Reddit-Flair-Detector for using it on the web app.

## Dependicies
* Flask==1.0.2
* Flask-WTF==0.14.2
* nltk==3.4
* praw==6.3.1
* prawcore==1.0.1
* Jinja2==2.10
* gunicorn==19.3.0
* pickleshare==0.7.5
* scikit-image==0.14.2
* scikit-learn==0.20.3
* numpy==1.16.2
* pandas==0.24.2
* Werkzeug==0.16.1
* Flask_JSON==0.3.4

## Project Approach
### Data Acquisition 
For data acquisition I've used the method..
####  Using Praw Library :
Using Python Praw library, I was able to scrape for eleven flairs, using a simple API calls. The code for data scraping is saved in [Reddit Data Collection.ipynb](/Flair%20Detector/Reddit Data Collection.ipynb) and the data is in [redddata.csv](/Data/csv%20files/reddata.csv).

### Model
I've followed the following steps to ceate a model to predict flairs.
#### 1.Data Combining 
I've divided data of each flair into testing and training with the division being 20:80. 
The code of data-combining can be found [here](/Flair%20Detector/combine.ipynb) and the training data, testing data which is used to build the model can be found [here](/Data/csv%20files/data_train.csv) and [here](/Data/csv%20files/data_test.csv).

#### 2.Data Cleaning
* I've followed the following steps to clean the text of the posts.
 * Convert words to Lowercase.
 * Tokenize the word using word_tokenize.
 * Removed the stop-words.
 * Removed the punctuation.
 * Lematization using WordNetLemmatizer.
* I have used the same procedure to clean the post of new test cases on the web-app.

#### 3. Convert words to Vectors
* I've used Tf-Idf Vectorizer from Sklearn.
* I've also exported the vectorizer to be used in the web app.

#### 4. Model And Feature Selection.
* I've trained models using different classfiers and features.
##### Classifiers No.:
1. SVC
2. DecisionTreeClassifier
3. LogisticRegression
4. RandomForestClassifier
5. XGBClassifier

##### Results :

* Features : Title 

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.8873239436619719| 0.4884937238493724|
|2|0.9577464788732394| 0.3880753138075314|
|3|0.724830464267084| 0.4884937238493724|
|4|0.9577464788732394| 0.47384937238493724|
|5|0.6674491392801252| 0.44037656903765693| 

* Features : URL

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.4590505998956703| 0.3985355648535565|
|2|0.4809598330725091| 0.3797071129707113|
|3|0.4428794992175274| 0.39644351464435146|
|4|0.4809598330725091| 0.3891213389121339|
|5|0.45539906103286387| 0.39330543933054396| 
 

* Features : Body 

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.3075117370892019| 0.23326359832635984|
|2|0.32785602503912364| 0.2395397489539749|
|3|0.2540427751695357| 0.24476987447698745|
|4|0.32785602503912364| 0.2510460251046025|
|5|0.28351591027647366| 0.23744769874476987|


* Features : Title+Body 

| Classfiers No.| Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.9290558163797601| 0.5240585774058577|
|2|0.9754825247782994| 0.37343096234309625|
|3|0.7556077203964527| 0.5313807531380753|
|4|0.9754825247782994| 0.49372384937238495|
|5|0.7112676056338029| 0.49581589958158995|


* Features : Body+URL 

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.9264475743348983| 0.5575313807531381|
|2|0.985133020344288| 0.42887029288702927|
|3|0.7496087636932708| 0.5700836820083682|
|4|0.985133020344288| 0.5449790794979079|
|5|0.7378716744913928| 0.5753138075313807|

* Features : Title+URL 

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.5878977569118414| 0.4299163179916318
|2|0.634585289514867| 0.399581589958159|
|3|0.5179968701095462| 0.44142259414225943|
|4|0.634585289514867| 0.4361924686192469|
|5|0.548774126238915| 0.4320083682008368|

* Features : Title+Body+URL 

| Classfier No. | Accuracy on 5 Fold Cross-Validation on Training Set | Accuracy on Testing Set |
|:--------- |:------------|:-------------|
|1|0.8951486697965572| 0.5428870292887029|
|2|0.9778299426186751| 0.4581589958158996|
|3|0.7516953573291602| 0.5658995815899581|
|4|0.9778299426186751| 0.5219665271966527|
|5|0.6987480438184663| 0.5313807531380753|

* As I've got the best accuracy by using  Title+Body+URL as a feature and using SVC as the classfier hence I'l be using SVC model and Title+Body+URL as features to detect flairs on the web app.
* The code for data cleaning, model training and the results can be found [here](/Flair%20Detector/model.ipynb).

### Web-App
* The web-app is made using flask-library.
* It uses Flask-WTF forms to input the URL from user.
* It passes the URL to [model.py](/model.py)
* model.py uses the praw library to scrape the post from reddit and uses the cleaning, vectorizer and model from training processes to predict the flair of posts.
* Templates of the web app can be found [here](/templates).

## Analysis of Data
* Table of number of posts in each flair category in the data that is analysed.

| Flair     | No.of Posts |
|:--------- |:------------|
| Political | 246         |
| Non-Political | 6026 |
|[R]eddiquette|1176|
|AskIndia|5399|
|Science/Technology|1169|
|Policy/Economy|1205|
|Finance/Business|171|
|Sports|430|
|Food|305|
|Photography|507|
|AMA|210|

### Flair Wise Analysis [Link](http://red-flair-detector.herokuapp.com/data_ana1)
* Multi-Bar Chart for analysing average/median, scores/comments of posts belonging to different flairs.
![](images/image%20(4).png)

* Bar charts for analysing hour of the day at which post of different flairs are posted.
![](images/image%20(5).png)
![](images/image%20(6).png)
![](images/image%20(7).png)
![](images/image%20(8).png)

### Content Analysis [Link](http://red-flair-detector.herokuapp.com/data_ana2)
* Bar Charts for analysis frequency of words in the title of posts in different flairs categories. 
![](images/image%20(16).png)
![](images/image%20(17).png)
![](images/image%20(18).png)
![](images/image%20(19).png)

## Sources
* For Data-Scraping:
  * http://www.storybench.org/how-to-scrape-reddit-with-python/
* For D3.js Bar Charts:
  * http://bl.ocks.org/jonahwilliams/2f16643b999ada7b1909
  * https://bl.ocks.org/curran/af72fd9c1fb61d2133d273cd8a3ca557
  
## References
* https://github.com/parasmehan123/RedFlair

  
