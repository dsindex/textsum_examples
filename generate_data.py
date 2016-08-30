#!/bin/env python

import sys
import os

import tensorflow as tf

# Special tokens
PARAGRAPH_START = '<p>'
PARAGRAPH_END = '</p>'
SENTENCE_START = '<s>'
SENTENCE_END = '</s>'
UNKNOWN_TOKEN = '<UNK>'
PAD_TOKEN = '<PAD>'
DOCUMENT_START = '<d>'
DOCUMENT_END = '</d>'

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('input_dir', 'sample', 'input directory path')
tf.app.flags.DEFINE_string('data_path', 'sample-0', 'output file path')


'''
features {
  feature {
      key: "abstract"
      value {
        bytes_list {
          value: "...."
        }
      }
  }
  feature {
      key: "article"
      value {
        bytes_list {
          value: "...."
        }
      }
  }
}
'''

files = os.listdir(FLAGS.input_dir)
# python_io : https://www.tensorflow.org/versions/r0.10/api_docs/python/python_io.html
writer = tf.python_io.TFRecordWriter(FLAGS.data_path)
for i, file in enumerate(files):
    fid = open(os.path.join(FLAGS.input_dir, file), 'r')
    for line in fid :
        line = line.strip()
        if line == "" :
            continue
        try : key, val = line.split('\t',1)
        except : continue
        #key = DOCUMENT_START + ' ' + PARAGRAPH_START + ' ' + SENTENCE_START + ' ' + key + ' ' + SENTENCE_END + ' ' + PARAGRAPH_END + ' ' + DOCUMENT_END
        #val = DOCUMENT_START + ' ' + PARAGRAPH_START + ' ' + SENTENCE_START + ' ' + val + ' ' + SENTENCE_END + ' ' + PARAGRAPH_END + ' ' + DOCUMENT_END
        example = tf.train.Example(
            features = tf.train.Features(
                feature = {
                    'abstract': tf.train.Feature(bytes_list=tf.train.BytesList(value=[key])),
                    'article': tf.train.Feature(bytes_list=tf.train.BytesList(value=[val]))
                },
            )
        )
        serialized = example.SerializeToString()
        writer.write(serialized)
    fid.close()
writer.close()
