# Import sys and tensorflow as tf
import tensorflow as tf, sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Test
def test(fn):
    # Read in the image_data
    image_data = tf.gfile.FastGFile(fn, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
        predictions = sess.run(softmax_tensor, \
                 {'DecodeJpeg/contents:0': image_data})
    
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]*100
            score = round(score)
            return('%s.\n\nAlgorithm confidence = %.5f' % (human_string, score))

def createdialog(self, tfoutput): # Generates output message box. 
        dialog = Gtk.MessageDialog(None, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Algorithm results")
        dialog.format_secondary_text(
            "Algorithm shows that the image is "+tfoutput+"%")
        dialog.run()
        print("INFO dialog closed")

        dialog.destroy()
