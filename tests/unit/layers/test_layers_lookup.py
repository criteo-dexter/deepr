"""Tests for layers.lookup"""

import numpy as np
import tensorflow as tf

import deepr as dpr


def test_layers_lookup():
    """Test for Lookup"""
    mapping = {"a": 0, "b": 1}
    table = dpr.layers.table_from_mapping(name="mapping", mapping=mapping)
    layer = dpr.layers.Lookup(lambda: table)
    result = layer(tf.constant([b"a", b"b", b"c"]))
    with tf.Session() as sess:
        sess.run(tf.tables_initializer())
        got = sess.run(result)
        np.testing.assert_equal(got, [0, 1, -1])
