import subprocess

AWS_KEY = 'AKIAILUTTCA7JVVLRRZA'
AWS_SECRET = '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'

s3_path = 's3n://{0}:{1}@blaze-data/enron-email'.format(AWS_KEY, AWS_SECRET)
cmd = ['hadoop', 'distcp', s3_path, 'hdfs:///tmp/enron']
subprocess.call(cmd)
