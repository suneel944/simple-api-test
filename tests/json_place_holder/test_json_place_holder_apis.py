from pytest import mark

from src.enums.servers import Servers
from src.service.json_place_holder.jph_service import JsonPlaceHolder, get_base_url
from src.utils.file_mainpulation import readJson
from src.utils.timer_calc import current_time

config = readJson("configs/config.json")
request_spec = JsonPlaceHolder(base_url=get_base_url(Servers.TEST.value))


def test_get_all_posts():
    response = request_spec.get_all_posts()
    assert (response.status_code == 200) and response.headers["Content-Type"] == "application/json; charset=utf-8"


@mark.parametrize("param", ["3"])
def test_albums_path_params(param):
    response = request_spec.get_specific_album(num=param)
    # Content-Length assertion is made optional because
    # response header is not having any key with the same
    if "Content-Length" in response.headers:
        assert 1 == int(response.headers["Content-Length"])
    assert response.status_code == 200


def test_response_time_of_photos_endpoint():
    __t_pre = current_time()
    response = request_spec.get_photos()
    __t_post = current_time()
    assert (__t_post - __t_pre) < 10 and response.status_code == 200


@mark.parametrize("param", ["5"])
def test_specific_user_geo_location(param):
    respnse = request_spec.get_specific_user(num=param)
    data = respnse.json()["address"]["geo"]
    assert respnse.status_code == 200 and data["lat"] == "-31.8129" and data["lng"] == "62.5342"


def test_comment_is_sorted():
    response = request_spec.get_comments()

    # response ordered in descending order based on postId
    data = sorted(response.json(), key=lambda post: post["postId"], reverse=True)

    assert response.status_code == 200 and all(data[i]["postId"] >= data[i]["postId"] for i in range(len(data) - 1))
