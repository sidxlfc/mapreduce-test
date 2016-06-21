from flask import Flask, render_template, redirect
import os

global app
app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/execute')
def execute():

	#toreturn = os.popen("cat /home/ubuntu/hduser/newdata.csv | /home/ubuntu/hduser/mapper.py | sort -k1,1 | /home/ubuntu/hduser/reducer.py").read()
	os.system("/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D mapred.map.tasks=3 -D mapred.reduce.tasks=1 -input /input/* -output /out2/ -mapper /home/ubuntu/hduser/mapper.py -file /home/ubuntu/hduser/mapper.py -reducer /home/ubuntu/hduser/reducer.py -file /home/ubuntu/hduser/reducer.py")

	toreturn = os.popen("hdfs dfs -cat /out2/part-00000").read()
	
	return render_template("index.html", todisplay = toreturn)

if __name__ == "__main__":
    app.run()

'''port = os.getenv('PORT', '8000')
if __name__== "__main__":
    app.run(host="ec2-54-200-173-41.us-west-2.compute.amazonaws.com", port=int(port))'''