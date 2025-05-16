from src.services.streamLitService.streamLitService import StreamLitService
from src.services.llamaIndexService.llamaIndexService import llamaIndexService
def main():
    llamaIndexServiceInstance = llamaIndexService()
    streamLitServiceInstance = StreamLitService(llamaIndexServiceInstance)
    streamLitServiceInstance.run()

if __name__ == "__main__":
    main()