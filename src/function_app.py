import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="hello", auth_level=func.AuthLevel.FUNCTION)
def hello(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing request...")

    print("hello")
    return func.HttpResponse("Hello Arulraj, I am function app!")
    



