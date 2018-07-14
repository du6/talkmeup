import os
import ctypes

#Make sure libgrader.so is presented
_grader = ctypes.CDLL(os.getcwd() + '/ai/libgrader.so')
_grader.grade.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_int]
_grader.grade.restype = ctypes.POINTER(ctypes.c_int)


# ML_grade: Wrapper function for the Machine Learning-based grader
#
# ARGUMENTS ---
# path (string): Video file path
# path_length (int): Length of the file path string
# control (int): use 0 to enable all AI rubrics
#
# RETURN ------
# results (fixed size int arrary[32]):
# results[0] =  0: Success
#            = -1: Something went wrong. Try re-run the function.
# results[1]~[8]: Score for the 8 rubrics listed below:
# Index  |   Metric    |   Range
#   1     Smile           0 = No smile ... 5 = Alot smile
#   2     Speech rate     0 = < 80 words, 1 = 80~100 words, 2 = 100~120 words
#                         3 = 120~140 words, 4 = 140~160 words, 5 = > 160 words
#                         (Note: 1,2 = too slow, 5 = too fast, 3 or 4 is good)
#   3     Emotion         0 = Emitonness ... 5 = Very emotional
#   4     Filler words    0 = Many filler words ... 5 = Little filler words
#   5     Eye contact     0 = No eye contact, 1 = Have eye contact (Boolean)
#   6     Nervousness     0 = Very nervous ... 5 Not nervous at all
#   7     Pause           0 = Many pauses ... 5 Almost no pause detected
#   8     Clearness       0 = Very unclear ... 5 Very clear
# results[9]~[31]: reserved for debug, do not use.
#
def ML_grade(path, path_length, control):
    global _grader
    results = _grader.grade(ctypes.c_char_p(path.encode('utf-8')), ctypes.c_int(path_length), ctypes.c_int(control))
    return results
