from gaiasdk import sdk
import logging

def MyAwesomeJob(args):
    for arg in args:
        logging.info("Key: " + str(arg.key) + "; Value: " + str(arg.value))

def main():
    logging.basicConfig(level=logging.INFO)
    # Instead of sdk.InputType.TextFieldInp you can also use sdk.InputType.TextAreaInp
    # for a text area or sdk.InputType.BoolInp for boolean input.
    argParam = sdk.Argument("Type in your username:", sdk.InputType.TextFieldInp, "username")
    myjob = sdk.Job("MyAwesomeJob", "Do something awesome", MyAwesomeJob, None, [argParam])
    sdk.serve([myjob])
