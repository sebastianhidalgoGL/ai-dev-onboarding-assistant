from streamLitService import StreamLitService
from llamaIndexService import llamaIndexService
def main():
    llamaIndexServiceInstance = llamaIndexService()
    streamLitServiceInstance = StreamLitService(llamaIndexServiceInstance)
    streamLitServiceInstance.run()

if __name__ == "__main__":
    main()