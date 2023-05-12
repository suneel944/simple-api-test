from uplink import Consumer, Path, get
from uplink.decorators import error_handler, response_handler

from src.service.handlers.error import handle_exception
from src.service.handlers.response import check_for_status
from src.utils.file_mainpulation import readJson

_config = readJson("configs/config.json")


def get_base_url(server):
    return _config["json_place_holder"][server]["base_url"]


class JsonPlaceHolder(Consumer):
    """Json place holder api service"""

    @response_handler(check_for_status)  # response handler
    @error_handler(handle_exception)  # error handler
    @get("/posts")  # api construct
    def get_all_posts(self):
        """Retrieves all posts"""

    @response_handler(check_for_status)  # response handler
    @error_handler(handle_exception)  # error handler
    @get("/albums/{num}")  # api construct
    def get_specific_album(self, num: Path):
        """Retrieves specific album based on the index path parameter

        Args:
            num (Path): specifc content to pick from ex: 1
        """

    @response_handler(check_for_status)  # response handler
    @error_handler(handle_exception)  # error handler
    @get("/photos")  # api construct
    def get_photos(self):
        """Retrieves photos"""

    @response_handler(check_for_status)  # response handler
    @error_handler(handle_exception)  # error handler
    @get("/users/{num}")  # api construct
    def get_specific_user(self, num: Path):
        """Retrieves specific user based on the index path parameter

        Args:
            num (Path): specifc content to pick from ex: 1
        """

    @response_handler(check_for_status)  # response handler
    @error_handler(handle_exception)  # error handler
    @get("/comments")  # api construct
    def get_comments(self):
        """Retrieves comments"""
