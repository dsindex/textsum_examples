# textsum

- description
  - test code for textsum
  - textsum
    - [Text summarization with TensorFlow](https://research.googleblog.com/2016/08/text-summarization-with-tensorflow.html)
	- [English Gigaword](https://catalog.ldc.upenn.edu/LDC2012T21)
    - reference paper [A Neural Attention Model for Abstractive Sentence Summarization](https://arxiv.org/abs/1509.00685)
      - an implementation using tensorflow, [neural-summary-tensorflow](https://github.com/carpedm20/neural-summary-tensorflow)
  
- pre-requesite and setting
  - see https://github.com/tensorflow/models/tree/master/textsum

- data format
  - how does data file look like?
  ```shell
  $ python check_data.py

  features {
    feature {
      key: "abstract"
      value {
        bytes_list {
          value: "<d> <p> <s> sri lanka closes schools as war escalates . </s> </p> </d>"
        }
      }
    }
    feature {
      key: "article"
      value {
        bytes_list {
          value: "<d> <p> <s> the sri lankan government on wednesday announced the closure of government schools with immediate effect as a military campaign against tamil separatists escalated in the north of the country . </s> <s> t
he cabinet wednesday decided to advance the december holidays by one month because of a threat from the liberation tigers of tamil eelam -lrb- ltte -rrb- against school children , a government official said . </s> <s> `` there are i
ntelligence reports that the tigers may try to kill a lot of children to provoke a backlash against tamils in colombo . </s> <s> `` if that happens , troops will have to be withdrawn from the north to maintain law and order here , \
'\' a police official said . </s> <s> he said education minister richard pathirana visited several government schools wednesday before the closure decision was taken . </s> <s> the government will make alternate arrangements to hold
 end of term examinations , officials said . </s> <s> earlier wednesday , president chandrika kumaratunga said the ltte may step up their attacks in the capital to seek revenge for the ongoing military offensive which she described
as the biggest ever drive to take the tiger town of jaffna . . </s> </p> </d>"
        }
      }
    }
    feature {
      key: "publisher"
      value {
        bytes_list {
          value: "AFP"
        }
      }
    }
  }
  ```
  - `ExampleGen()` is used in batch_reader.py
  ```python
  input_gen = self._TextGenerator(data.ExampleGen(self._data_path))
  ```

- test
```shell
$ ls
README.md  WORKSPACE  bazel-bin  bazel-genfiles  bazel-out  bazel-test_textsum	bazel-testlogs	check_data.py  data  textsum  test.sh

$ ./test.sh -v -v
...
running_avg_loss: 1.002997
running_avg_loss: 1.384698
running_avg_loss: 0.865053
...
```
