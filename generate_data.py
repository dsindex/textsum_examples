#!/bin/env python

import sys
import os

import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('input_dir', 'sample', 'input directory path')
tf.app.flags.DEFINE_string('data_path', 'test-0', 'output file path')


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
writer = tf.python_io.TFRecordWriter(FLAGS.data_path)
for i, file in enumerate(files):
    content = open(os.path.join(FLAGS.input_dir, file), "r").read()
    example = tf.train.Example(
        features = tf.train.Features(
            feature = {
                'abstract': tf.train.Feature(bytes_list=tf.train.BytesList(value=[content])),
                'article': tf.train.Feature(bytes_list=tf.train.BytesList(value=[content]))
            },
        )
    )
    serialized = example.SerializeToString()
    writer.write(serialized)

