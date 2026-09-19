import uvicorn


if __name__ == "__main__":
    uvicorn.run("config:app", port="0.0.0.0", port=8000, reload=True)