import send_requests
def get_tracknumber():
    track_number = send_requests.post_neworder()
    return track_number.json()["track"]

def test_track_order():
    track_number = get_tracknumber()
    get_response = send_requests.get_info(track_number)
    assert get_response.status_code == 200