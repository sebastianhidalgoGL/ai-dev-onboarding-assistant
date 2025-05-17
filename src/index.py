from dotenv import load_dotenv
from src.services.streamLitService.stream_lit_service import StreamLitService
from src.services.llamaIndexService.llama_index_service import LlamaIndexService

def main():
    llamaIndexServiceInstance = LlamaIndexService()
    streamLitServiceInstance = StreamLitService(llamaIndexServiceInstance)
    streamLitServiceInstance.run()

if __name__ == "__main__":
    load_dotenv()
    main()
