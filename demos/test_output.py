from disco.core import Job, result_iterator

def map(line, params):
    for word in line.split():
        yield word,1

def reduce(iter, params):
    from disco.util import kvgroup
    for word, counts in kvgroup(sorted(iter)):
        yield word, sum(counts)

'''
def mongodb_output(stream,partition,url,params):
    return mongoDisco_output.MongoDBoutput(stream,params)
'''

if __name__ == '__main__':

    job = Job().run(input=["r"],
            map=map,
            reduce=reduce,
            map_input_stream = mongodb_input_stream
            reduce_output_stream=mongodb_output_stream)

    job.wait(show=True)
