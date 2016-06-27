import csv
import sys

def get_names(cluster_filename, metadata_filename):
    ''' Given a cluster output from motifcluster, print out the names of
    the nodes in the cluster. '''
    
    inds = {}
    with open(cluster_filename) as cluster:
        inds = [int(index) for index in cluster]

    with open(metadata_filename, 'rb') as metadata:
        reader = csv.DictReader(metadata)
        for row in reader:
            index = int(row["node_id"])
            if index in inds:
                sys.stdout.write('%d: %s\n' % (index, row["name"]))

if __name__ == '__main__':
    try:
        cluster_filename = sys.argv[1]
        metadata_filename = sys.argv[2]
    except:
        sys.stderr.write('USAGE: python get_names.py cluster_filename metadata_filename\n')        
    get_names(cluster_filename, metadata_filename)
